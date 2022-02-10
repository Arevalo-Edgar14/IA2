<template>
  <Sidebar
    v-if="showSidebar"
    :darkMode="darkMode"
    :toggleSidebar="toggleSidebar"
    :toggleDarkMode="toggleDarkMode"
    :links="links"
  />
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div> -->
  <router-view />
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Sidebar from "@/components/sidebar/Sidebar.vue";

@Options({
  components: {
    Sidebar,
  },
  methods: {
    toggleSidebar() {
      this.showSidebar = !this.showSidebar;
    },
    toggleDarkMode() {
      this.darkMode = !this.darkMode;
    },
  },
})
export default class App extends Vue {
  data() {
    return {
      showSidebar: true,
      darkMode: !window.matchMedia("(prefers-color-scheme: light)").matches,
      links: [
        {
          name: "home",
          to: "/",
          icon: "bx bx-home-alt icon",
        },
        // {
        //   name: "perceptron",
        //   to: "/perceptron",
        //   icon: "bx bx-pie-chart-alt icon",
        // },
        {
          name: "about",
          to: "/about",
          icon: "bx bx-heart icon",
        },
      ],
    };
  }
}
</script>

