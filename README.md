# Take-home Assignment - Fall 2020

![Hack4Impact McGill Logo](./hack4impact-logo-text-long.png)

This challenge is intended to expose you to some elements of our most common technical stack: a [Vue](https://vuejs.org/) frontend, and a Flask backend.

[Flask](<https://en.wikipedia.org/wiki/Flask_(web_framework)>) is a lightweight Python framework that is useful for building web applications. The Flask [documentation](http://flask.palletsprojects.com/en/1.1.x/) contains lots of useful information, including a quick-start guide. The following resources may be helpful for learning Python:

- [Python3 Tutorial](https://docs.python.org/3.7/tutorial/index.html)
- [Python Documentation](https://docs.python.org/3.7/)

The following resources may be helpful for learning Vue:

[The Official Vue Documentation](https://vuejs.org/v2/guide/) is very beneficial to go through to get a complete understanding on Vue fundamentals; reading about [Single File Components](https://vuejs.org/v2/guide/single-file-components.html) will be useful for this assignment in particular. It may also be beneficial to get comfortable diving into [Javascript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) as part of this exercise.

Reading the following will help you get a sense of the big picture when it comes to developing APIs/writing server side code, and how it fits in the context of a larger web application:

- [How the Web Works](https://medium.freecodecamp.org/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c) - Read all 3 parts, especially part 3!
- [An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) - An in-depth look at how HTTP works
- [HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) - Overview of the different HTTP methods and what they do
- [Basics of HTTP](https://egghead.io/courses/understand-the-basics-of-http)

This project will be broken down into multiple parts. After you finish this project, you must submit it by following the instructions below.

_This exercise is due before Saturday, September 19th at 11:59PM EST. If you can't figure everything out or have spent over 10 hours total, just submit what you have! We prioritize effort over your current skills and knowledge. That being said, if you've completed the entire challenge show off your creativity by adding some extra features in!_

Submit either a link to your forked GitHub repository or a zipped folder with all of your code to hack4impact@mcgilleus.ca.

For any questions, feel free to email albert.kragl@mail.mcgill.ca.

## Setup

First, fork this repository (using the fork button on the top right of the repository page). This copies this repository over to your account. Now you should have a repository with the name `<yourusername>/takehome-assignment`.

> Note: for Windows, we recommend installing either the [Git command line for Windows](https://gitforwindows.org/) or using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

We suggest doing the following from your terminal/command line. Once you've forked this repository, [clone](https://confluence.atlassian.com/bitbucket/clone-a-repository-223217891.html) it onto your computer (click the green button saying "Clone or Download", choose http, and copy and paste in the location `<url>`) and go into it:

```
$ git clone <url>
$ cd takehome-assignment
```

_Note: if you get an error after running the `git` command, make sure to install git [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)._

Now open a second terminal and navigate to this cloned repository.
In one of the terminals, type `cd backend` then follow the [backend instructions](backend/README.md).
In the other, type `cd vue-frontend` then follow the [frontend instructions](frontend/README.md).

[Postman](https://www.getpostman.com/) or [Advanced REST Client](https://install.advancedrestclient.com/install) will be useful for testing your backend as you go. These are applications that can send various types of HTTP requests to specified endpoints. Click on the links to download whichever one you prefer. Note that the Postman examples are about a different scenario, but they should help you to use it.

For this assignment, we don't recommend using Eclipse; instead, we recommend using either [VSCode](https://code.visualstudio.com/download) or [Atom](https://atom.io/) as your code editor.

# Exercise

The following exercise will have you learn and apply some Vue and Flask to build a tool to keep track of your progress in multiple TV shows. Check the README in the `backend` folder for more detailed instructions!

## Flask

### Part 1 - Already Done

```bash
GET /shows

# example - try going to this link in your browser!
http://127.0.0.1:8080/shows
```

This should return a properly formatted [JSON](https://www.w3schools.com/whatis/whatis_json.asp) response that contains a list of all the `shows` in the mockdb. If you call this endpoint **after starting the server**, you should get this response in Postman/ARC:

```
{
  "code": 200,
  "message": "",
  "result": {
    "shows": [
      {
        "id": 1,
        "name": "Game of Thrones",
        "episodes_seen": 0
      },
      {
        "id": 2,
        "name": "Naruto",
        "episodes_seen": 220
      },
      {
        "id": 3,
        "name": "Black Mirror",
        "episodes_seen": 3
      }
    ]
  },
  "success": true
}
```

### Part 2

Define the endpoint:

```
GET /shows/<id>
```

This should retrieve a single show that has the `id` provided from the request. For example, `GET http://127.0.0.1:8080/shows/1` would return:

```
{
  "code": 200,
  "message": "",
  "result": {
    "id": 1,
    "name": "Game of Thrones",
    "episodes_seen": 0
  },
  "success": true
}
```

If there doesn't exist a show with the provided `id`, return a `404` HTTP status code with a descriptive `message`. Remember to make use of the provided mockdb methods!

_Use Part 5, which has been completed for you, to figure out how to write this endpoint!_

## Part 3

Define the endpoint:

```
POST /shows
```

This endpoint should create a new show. Each request should also send a `name`, and `episodes_seen` parameter in the request's `body`. The `id` property will be created automatically in the mockdb.

> **Note:** you will need to use either Postman or ARC to make a POST request! URLs typed into a browser window will always send a GET request, which don't contain a request body.

A successful request should return a status code of `201` and return the newly created show (in the same format as Part 2).

If any of the required parameters aren't provided, **do not** create a new show in the db and return a `422` with a useful `message`. In general, your messages should provide the user/developer useful feedback on what they did wrong and how they can fix it.

This is how you can send `body` parameters from Postman. Make sure you don't mistake this for query parameters (which would look something like `/shows?param1=val1&param2=val2`)!
![Postman POST](backend/docs/postman_post.png)

## Part 4

Define the endpoint:

```
PUT /shows/<id>
```

Here we need to provide a show's `id` since we need to specify which show to update. The `body` for this request should contain the same attributes as the `POST` request from Part 3.

However, the difference with this `PUT` request is that only values with the provided keys (`name`, `episodes_seen`) will be updated, and any parameters not provided will not change the corresponding attribute in the show being updated.

You do not need to account for `body` parameters provided that aren't `name`, or `episodes_seen`.

If the show with the provided `id` cannot be found, return a `404` and a useful `message`.

If you do find the show, return it in the same way you did in Part 3 with the updated values.

## Part 5 - Already Done

Define the endpoint:

```
DELETE /shows/<id>
```

This will delete the show with the associated `id`. Return a useful `message`, although nothing needs to be specified in the response's `result`.

If the show with the provided `id` cannot be found, return a `404` and a useful `message`.

## Part 6 (Bonus!)

Extend the first `/shows` endpoint by adding the ability to query the shows based on the number of episodes they have. You should _not_ use a URL parameter like you did in Part 2. Instead, use a [query string parameter](https://en.wikipedia.org/wiki/Query_string). If no query string parameter is passed, the endpoint should still return all shows as before.

If `minEpisodes` is provided as a query string parameter, only return the shows which have that number or more episodes seen. Use what you've learned so far to figure out what you could return if there are no shows matching the query parameter.

For this exercise, you can ignore any query string parameters other than `minEpisodes` and you may assume that the provided parameter will be an integer represented as a string of digits.

In Postman, you can supply query string parameters writing the query string into your request url or by hitting the `Params` button next to `Send`. Doing so will automatically fill in the request url.

The following should happen:

```
GET /shows?minEpisodes=3

{
  "code": 200,
  "message": "",
  "result": {
    "shows": [
      {
        "id": 2,
        "name": "Naruto",
        "episodes_seen": 220
      },
      {
        "id": 3,
        "name": "Black Mirror",
        "episodes_seen": 3
      }
    ]
  },
  "success": true
}
```

## Vue

Check the README in the `vue-frontend` folder for more detailed instructions!

### Part 1

Goal: Get familiar with Vue syntax, component structure, and passing props.

Tasks:

- Open up the `Home` component in `src/components`

- Send a `complete` prop (property) into the `Instructions` component that determines whether or not to display a second line of text ([Hint 1](https://vuejs.org/v2/guide/conditional.html) and [Hint 2](https://vuejs.org/v2/guide/components-props.html#Passing-Static-or-Dynamic-Props))

### Part 2

Goal: Get familiar with the Vue router.

Tasks:

- Go to `src/router` and open up the `index.js` file. You'll see there is already a route defined for `/`, which is mapped to the `Home` component
- Create a new route for the `Counter` component, and verify that it works by going to that link in your browser

### Part 3

Goal: Get familiar with component state.

Tasks:

- Open up the `Counter` component in `src/components`
- Display the value of the current count
- Create two buttons: one that increments the count and one that decrements it ([Hint](https://vuejs.org/v2/guide/events.html))

### Part 4

Goal: Use nested components and props.

Tasks:

- The code given in Part 5 will be useful for rendering the code you write below

- Open the empty `Show` component and add properties for `id`, `name`, and `episodes_seen`
- In the template section of the `Show` component, display the show name
- In the same template section, render a `Counter` component. Modify the `Counter` component to take the initial count as a prop, and use this value for `count` in the initial state. Look at the `Home` component to see how to import a component.
- Pass the number of episodes watched as a prop to `Counter`. Notice how you nested the `Counter` component within the `Show` component!
- To check that this works, just look at your running app. You should see 3 show names, each of which should have a counter next to it.

### Part 5 - Already Done

Goal: Get familiar with rendering lists and javascript array functions.

Tasks:

- In the `Home` component, an initial list of shows has already been provided in the `data()` function
- Display each show by passing each show's attributes as props to a `Show` component
- Useful to read over: [List Rendering in Vue](https://vuejs.org/v2/guide/list.html)

### Part 6 (Bonus!)

Goal: Get familiar with user input.

Tasks:

- In `Home.vue`, make an input and a submit button that adds a new show to the state (set the new show's `id` to the next integer, and the `episodes_seen` to 0)
- Note: If your button refreshes the whole page, throw in a button type: `<button type="button" ...`
