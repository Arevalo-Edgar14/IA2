<template>
  <li class="">
    <a href="#">
      <i class="bx bx-log-out icon"></i>
      <span class="text nav-text">Logout</span>
    </a>
  </li>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  name: 'LogOut',
  components: {},
  props: {},
})
export default class LogOut extends Vue {}
</script>
