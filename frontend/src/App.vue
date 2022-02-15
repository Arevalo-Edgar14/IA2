<template>
  <div class="main-div">
    <Sidebar
      :darkMode="darkMode"
      :toggleSidebar="toggleSidebar"
      :toggleDarkMode="toggleDarkMode"
    />
    <router-view class="home" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Sidebar from '@/components/sidebar/Sidebar.vue';

@Options({
  name: 'App',
  components: {
    Sidebar,
  },
  watch: {
    darkMode(value) {
      this.setDarkMode(value);
    },
    showSidebar(value) {
      this.closeSideBar(value);
    },
  },
})
export default class App extends Vue {
  showSidebar = false;

  darkMode =
    localStorage.getItem('preferredDarkMode') !== null
      ? localStorage.getItem('preferredDarkMode') === 'true'
      : window.matchMedia &&
        window.matchMedia('(prefers-color-scheme: dark)').matches;

  setDarkMode(value: string | boolean | null): void {
    localStorage.setItem('preferredDarkMode', String(value));

    if (value) {
      document.body.classList.add('darker');
      document.documentElement.setAttribute('data-mode', 'dark');
    } else {
      document.body.classList.remove('darker');
      document.documentElement.removeAttribute('data-mode');
    }
  }

  closeSideBar(value: boolean): void {
    const sidebar = document.body.querySelector('.sidebar');
    if (value) {
      // show
      sidebar?.classList.remove('close');
    } else {
      // close
      sidebar?.classList.add('close');
    }
  }

  toggleSidebar(): void {
    this.showSidebar = !this.showSidebar;
  }

  toggleDarkMode(): void {
    this.darkMode = !this.darkMode;
  }

  mounted(): void {
    this.setDarkMode(this.darkMode);
    this.closeSideBar(this.showSidebar);
  }
}
</script>
