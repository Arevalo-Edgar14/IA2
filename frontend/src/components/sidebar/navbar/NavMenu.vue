<template>
  <div class="menu-bar">
    <div class="menu">
      <NavSearchBox :search="search" :openSidebar="openSidebar" />
      <NavLinks :links="links" />
    </div>

    <NavBottom :toggleDarkMode="toggleDarkMode" :darkMode="darkMode" />
  </div>
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';
import NavLinks from '@/components/sidebar/navbar/NavLinks.vue';
import Link from '@/types/Link';
import NavSearchBox from '@/components/sidebar/navbar/NavSearchBox.vue';
import NavBottom from '@/components/sidebar/navbar/NavBottom.vue';

@Options({
  name: 'NavMenu',
  components: {
    NavLinks,
    NavSearchBox,
    NavBottom,
  },
  props: {
    links: {
      required: true,
      type: Array as PropOptions<Link[]>,
    },
    toggleDarkMode: {
      require: true,
      type: Function as PropOptions<() => void>,
    },
    darkMode: {
      require: true,
      type: Boolean,
    },
    openSidebar: Function as PropOptions<() => void>,
  },
})
export default class NavMenu extends Vue {
  search = '';
}
</script>
