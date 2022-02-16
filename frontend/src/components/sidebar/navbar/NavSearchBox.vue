<template>
  <li class="search-box" @click="openSidebar">
    <i class="bx bx-search icon"></i>
    <input type="text" placeholder="Search..." />
  </li>
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';

@Options({
  name: 'NavSearchBox',
  props: {
    search: {
      required: true,
      type: String,
    },
    openSidebar: Function as PropOptions<() => void>,
  },
})
export default class NavSearchBox extends Vue {}
</script>
