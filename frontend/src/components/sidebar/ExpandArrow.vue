<template>
  <i class="bx bx-chevron-right toggle" @click="toggleSidebar"></i>
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';

@Options({
  name: 'ExpandArrow',
  props: {
    toggleSidebar: Function as PropOptions<() => void>,
  },
})
export default class ExpandArrow extends Vue {}
</script>
