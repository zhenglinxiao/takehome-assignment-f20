<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions v-bind:complete="true"/>
    <!-- PART 4: Modify the Show component to accept all of these props -->
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />
    <p><br></p>
    <input type="text" v-model="newshow" placeholder="Enter show name">
    <button type="button" v-on:click="addshow(newshow)">Submit</button>
    <p><br></p>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ]
    };
  },
  methods:{
    addshow: function(newshow){
      this.shows.push({
        id: 4,
        name: newshow,
        episodes_seen: 0
      });
    }
  }
};
</script>

<style>
</style>
