<template>
  <div>
    <p>Number of episodes seen: {{ count }}.</p>
    <button v-on:click="count++">Increment</button>
    <button v-on:click="count--">Decrement</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: this.initial_count
    };
  },
  props:{
    initial_count: Number
  }
};
</script>

<style>
</style>
