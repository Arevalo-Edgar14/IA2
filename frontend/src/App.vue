<template>
  <div class="main-div">
    <Sidebar
      :darkMode="darkMode"
      :toggleSidebar="toggleSidebar"
      :openSidebar="openSidebar"
      :toggleDarkMode="toggleDarkMode"
    />
    <router-view class="home" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Sidebar from '@/components/sidebar/Sidebar.vue';
// import '@/plugins/chart';

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
      this.doShowSidebar(value);
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

  doShowSidebar(value: boolean): void {
    const sidebar = document.body.querySelector('.sidebar');
    if (value) {
      sidebar?.classList.remove('close');
    } else {
      sidebar?.classList.add('close');
    }
  }

  openSidebar(): void {
    this.showSidebar = true;
  }

  toggleSidebar(): void {
    this.showSidebar = !this.showSidebar;
  }

  toggleDarkMode(): void {
    this.darkMode = !this.darkMode;
  }

  mounted(): void {
    this.setDarkMode(this.darkMode);
    this.doShowSidebar(this.showSidebar);
  }
}
</script>
