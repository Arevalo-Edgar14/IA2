<template>
  <nav class="sidebar">
    <header>
      <div class="image-text">
        <Logo :cla="cla" :img="img" :alt="alt" />
        <EmphasizedNonEmphasized
          :emphasized="emphasized"
          :nonEmphasized="nonEmphasized"
        />
      </div>
      <ExpandArrow :toggleSidebar="toggleSidebar" />
    </header>

    <NavMenu
      :links="links"
      :toggleDarkMode="toggleDarkMode"
      :darkMode="darkMode"
    />
  </nav>
</template>

<script lang="ts">
import { Options, Vue, PropOptions } from 'vue-class-component';
import Logo from '@/components/sidebar/Logo.vue';
import EmphasizedNonEmphasized from '@/components/sidebar/EmphasizedNonEmphasized.vue';
import ExpandArrow from '@/components/sidebar/ExpandArrow.vue';
import NavMenu from '@/components/sidebar/navbar/NavMenu.vue';

@Options({
  name: 'Sidebar',
  components: {
    Logo,
    EmphasizedNonEmphasized,
    NavMenu,
    ExpandArrow,
  },
  props: {
    darkMode: Boolean,
    toggleDarkMode: Function as PropOptions<() => void>,
    toggleSidebar: Function as PropOptions<() => void>,
  },
})
export default class Sidebar extends Vue {
  cla = 'image';

  img = './logo.png';

  alt = 'logo';

  emphasized = 'IA2';

  nonEmphasized = 'Edgar Arevalo';

  links = [
    {
      name: 'home',
      to: '/',
      icon: 'bx bx-home-alt icon',
    },
    // {
    //   name: "perceptron",
    //   to: "/perceptron",
    //   icon: "bx bx-pie-chart-alt icon",
    // },
    {
      name: 'about',
      to: '/about',
      icon: 'bx bx-heart icon',
    },
  ];
}
</script>
