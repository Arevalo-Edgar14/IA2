<template>
  <li class="mode">
    <div class="sun-moon">
      <i class="bx bx-sun icon sun" v-if="darkMode"></i>
      <i class="bx bx-moon icon moon" v-else></i>
    </div>
    <span class="mode-text text" v-if="darkMode">Dark mode</span>
    <span class="mode-text text" v-else>Light Mode</span>

    <div class="toggle-switch" @click="toggleDarkMode">
      <span class="switch"></span>
    </div>
  </li>
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';

@Options({
  name: 'Mode',
  components: {},
  props: {
    toggleDarkMode: {
      require: true,
      type: Function as PropOptions<() => void>,
    },
    darkMode: {
      require: true,
      type: Boolean,
    },
  },
})
export default class Mode extends Vue {}
</script>
