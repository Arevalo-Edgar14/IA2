<template>
  <ScatterChart
    ref="chartRef"
    :chartData="testData"
    :options="options"
    @click="shuffleData"
  />
</template>

<script lang="ts">
import { ScatterChart, ExtractComponentData } from 'vue-chart-3';
import { Chart, ChartData, ChartOptions, registerables } from 'chart.js';
import { defineComponent, computed, ref } from 'vue';
// import { shuffle } from 'lodash';

Chart.register(...registerables);

export default defineComponent({
  name: 'Home',
  components: { ScatterChart },
  setup() {
    const data = ref([30, 40, 60, 70, 5]);
    const chartRef = ref<ExtractComponentData<typeof ScatterChart>>();

    const options = ref<ChartOptions<'doughnut'>>({
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Chart.js Doughnut Chart',
        },
      },
    });

    const testData = computed<ChartData<'doughnut'>>(() => ({
      labels: ['Paris', 'Nîmes', 'Toulon', 'Perpignan', 'Autre'],
      datasets: [
        {
          data: data.value,
          backgroundColor: [
            '#77CEFF',
            '#0079AF',
            '#123E6B',
            '#97B0C4',
            '#A5C8ED',
          ],
        },
      ],
    }));

    function shuffleData() {
      // data.value = shuffle(data.value);
      console.log(1);
      console.log(chartRef.value);
      console.log(chartRef.value?.chartInstance);
      console.log(chartRef.value?.chartInstance.scales.x.getValueForPixel);
      chartRef.value?.chartInstance.toBase64Image();
    }

    return {
      testData,
      shuffleData,
      chartRef,
      options,
    };
  },
});
</script>
