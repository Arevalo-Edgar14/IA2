<template>
  <span :class="image">
    <img :src="logo" :alt="alt" />
  </span>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
  props: {
    image: String,
    logo: String,
    alt: String,
  },
})
export default class Logo extends Vue {}
</script>
