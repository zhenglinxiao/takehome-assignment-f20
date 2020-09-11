from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['POST'])
def create_show():
    info = request.json
    if "name" not in info:
        if "episodes_seen" not in info:
            return create_response(status=422, message="Parameters missing")
        return create_response(status=422, message="Name parameter missing")
    elif "episodes_seen" not in info:
        return create_response(status=422, message="Episodes seen parameter missing")
    id = db.create('shows', info)["id"]
    return create_response(data=db.getById('shows',int(id)), status=201)

@app.route("/shows/<id>", methods=['POST'])
def modify_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    info = dict()
    if "name" in request.json:
        info["name"] = request.json["name"]
    if "episodes_seen" in request.json:
        info["episodes_seen"] = request.json["episodes_seen"]
    db.updateById('shows', int(id), info)
    return create_response(data=db.getById('shows', int(id)))

@app.route("/shows", methods=['GET'])
def get_all_shows():
    min_episodes = request.args.get('minEpisodes')
    if min_episodes is None:
        return create_response({"shows": db.get('shows')})
    else:
        display_shows = dict()
        display_shows['shows'] = []
        for show in db.get('shows'):
            if show['episodes_seen'] >= int(min_episodes):
                display_shows['shows'].append(show)
        if len(display_shows['shows']) == 0:
            return create_response(status=200, message="No such shows found")
        return create_response(data=display_shows)

@app.route("/shows/<id>", methods=['GET'])
def get_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response(data=db.getById('shows',int(id)))

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
