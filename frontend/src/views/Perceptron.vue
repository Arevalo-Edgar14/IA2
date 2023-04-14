<template>
  <div class="Perceptron">
    <h1>This is the Perceptron page</h1>
    <PlotChart />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import PlotChart from '@/components/chart/PlotChart.vue';

@Options({
  name: 'Perceptron',
  components: {
    PlotChart,
  },
})
export default class Perceptron extends Vue {}
</script>
