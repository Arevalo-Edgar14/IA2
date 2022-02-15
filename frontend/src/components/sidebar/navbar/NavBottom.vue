<template>
  <div class="bottom-content">
    <LogOut />

    <Mode :toggleDarkMode="toggleDarkMode" :darkMode="darkMode" />
  </div>
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';
import LogOut from '@/components/sidebar/navbar/LogOut.vue';
import Mode from '@/components/sidebar/navbar/Mode.vue';

@Options({
  name: 'NavBottom',
  components: {
    LogOut,
    Mode,
  },
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
export default class NavBottom extends Vue {}
</script>
