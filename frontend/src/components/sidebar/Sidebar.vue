<template>
  <div id="nav">
    <nav class="sidebar close">
      <header>
        <div class="image-text">
          <Logo :cla="cla" :img="img" :alt="alt" />
          <EmphasizedNonEmphasized
            :emphasized="emphasized"
            :nonEmphasized="nonEmphasized"
          />
        </div>
        <!-- ExpandArrow -->
        <i class="bx bx-chevron-right toggle"></i>
      </header>

      <!-- NavMenu -->
      <div class="menu-bar">
        <div class="menu">
          <!-- NavSearchBox -->
          <li class="search-box">
            <i class="bx bx-search icon"></i>
            <input type="text" placeholder="Search..." />
          </li>
          <!-- NavLinks -->
          <ul class="menu-links">
            <li class="nav-link" v-for="(link, i) in links" :key="i">
              <router-link :to="link.to">
                <i :class="link.icon"></i>
                <span class="text nav-text">{{ link.name }}</span>
              </router-link>
            </li>
          </ul>
        </div>

        <!-- NavBottom -->
        <div class="bottom-content">
          <!-- LogOut -->
          <li class="">
            <a href="#">
              <i class="bx bx-log-out icon"></i>
              <span class="text nav-text">Logout</span>
            </a>
          </li>
          <!-- Mode -->
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
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';
import Link from '@/types/Link';
import Logo from '@/components/sidebar/Logo.vue';
import EmphasizedNonEmphasized from '@/components/sidebar/EmphasizedNonEmphasized.vue';

@Options({
  name: 'Sidebar',
  components: {
    Logo,
    EmphasizedNonEmphasized,
  },
  props: {
    darkMode: Boolean,
    toggleSidebar: Function as PropOptions<() => void>,
    toggleDarkMode: Function as PropOptions<() => void>,
    links: {
      required: true,
      type: Array as PropOptions<Link[]>,
    },
  },
})
export default class Sidebar extends Vue {
  cla = 'image';

  img = './logo.png';

  alt = 'logo';

  emphasized = 'IA2';

  nonEmphasized = 'Edgar Arevalo';
}
</script>
