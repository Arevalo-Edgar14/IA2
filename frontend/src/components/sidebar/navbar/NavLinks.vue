<template>
  <ul class="menu-links">
    <li class="nav-link" v-for="(link, i) in links" :key="i">
      <router-link :to="link.to">
        <i :class="link.icon"></i>
        <span class="text nav-text">{{ link.name }}</span>
      </router-link>
    </li>
  </ul>
</template>

<script lang="ts">
import Link from '@/types/Link';
import { Options, Vue, PropOptions } from 'vue-class-component';

@Options({
  name: 'NavLinks',
  props: {
    links: {
      required: true,
      type: Array as PropOptions<Link[]>,
    },
  },
})
export default class NavLinks extends Vue {}
</script>
