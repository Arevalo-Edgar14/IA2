<template>
  <div id="nav">
    <nav class="sidebar close">
      <header>
        <div class="image-text">
          <span class="image">
            <img src="logo.png" alt="" />
          </span>
          <div class="text logo-text">
            <span class="name">IA2</span>
            <span class="profession">Machine Learning</span>
          </div>
        </div>
        <i class="bx bx-chevron-right toggle"></i>
      </header>

      <div class="menu-bar">
        <div class="menu">
          <li class="search-box">
            <i class="bx bx-search icon"></i>
            <input type="text" placeholder="Search..." />
          </li>
          <ul class="menu-links">
            <li class="nav-link" v-for="(link, i) in links" :key="i">
              <router-link :to="link.to">
                <i :class="link.icon"></i>
                <span class="text nav-text">{{ link.name }}</span>
              </router-link>
            </li>
          </ul>
        </div>

        <div class="bottom-content">
          <li class="">
            <router-link to="/">
              <i class="bx bx-log-out icon"></i>
              <span class="text nav-text">Logout</span>
            </router-link>
          </li>
          <li class="mode">
            <div class="sun-moon">
              <i class="bx bx-moon icon moon"></i>
              <i class="bx bx-sun icon sun"></i>
            </div>
            <span class="mode-text text">Dark mode</span>

            <div class="toggle-switch">
              <span class="switch"></span>
            </div>
          </li>
        </div>
      </div>
    </nav>
  </div>
  <!-- <router-view /> -->
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';
import Link from '@/types/Link';

@Options({
  props: {
    darkMode: Boolean,
    toggleSidebar: { type: Function },
    toggleDarkMode: { type: Function },
    links: {
      required: true,
      type: Array as PropOptions<Link[]>,
    },
  },
})
export default class Sidebar extends Vue {}
</script>
