<template>
  <!-- PART 4: Add your code here -->
  <div>
    {{ name }}
    <Counter
      :initial_count="episodes_seen"
    />
  </div>
</template>

<script>
import Counter from "./Counter.vue";

// PART 4: Add your code here
export default {
  components:{
    Counter
  },
  props:{
      id: Number,
      name: String,
      episodes_seen: Number
  }
};
</script>

<style>
</style>
