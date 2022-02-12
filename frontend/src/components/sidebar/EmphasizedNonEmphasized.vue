<template>
  <div class="text logo-text">
    <span class="name">{{ emphasized }}</span>
    <span class="profession">{{ nonEmphasized }}</span>
  </div>
</template>

<script>
import { Options, Vue, PropOptions } from 'vue-class-component';

@Options({
  name: 'EmphasizedNonEmphasized',
  props: {
    emphasized: String,
    nonEmphasized: String,
  },
})
export default class EmphasizedNonEmphasized extends Vue {}
</script>
