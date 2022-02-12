<template>
  <span :class="cla">
    <img :src="getImgUrl" :alt="alt" />
  </span>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  name: 'Logo',
  props: {
    cla: String,
    img: String,
    alt: String,
  },
  computed: {
    getImgUrl() {
      const images = require.context('@/assets/', false, /\.png$/);
      return images(this.img);
    },
  },
})
export default class Logo extends Vue {}
</script>
