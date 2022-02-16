<template>
  <div class="text header-text">
    <span class="emphasized">{{ emphasized }}</span>
    <span class="nonemphasized">{{ nonEmphasized }}</span>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  name: 'EmphasizedNonEmphasized',
  props: {
    emphasized: String,
    nonEmphasized: String,
  },
})
export default class EmphasizedNonEmphasized extends Vue {}
</script>
