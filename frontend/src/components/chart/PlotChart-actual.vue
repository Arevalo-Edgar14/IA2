<template>
  <!-- @click="addPoint"
    @contextmenu="addPoint" -->
  <ScatterChart
    ref="chartRef"
    @click="addPoint"
    :chartData="chartData"
    :options="options"
    css-clases="chart-container"
  />
</template>

<script lang="ts">
import Point from '@/types/Point';
import {
  Chart,
  ChartData,
  ChartOptions,
  ChartTypeRegistry,
  registerables,
  ScaleOptionsByType,
} from 'chart.js';
import { getRelativePosition, drawPoint } from 'chart.js/helpers';
import { computed, defineComponent, readonly, ref } from 'vue';
import { ExtractComponentData, ScatterChart } from 'vue-chart-3';

Chart.register(...registerables);

export default defineComponent({
  name: 'PlotChart',
  components: { ScatterChart },
  setup() {
    const points = ref<Array<Array<Point>>>([[], []]);
    const chartRef = ref<ExtractComponentData<typeof ScatterChart>>();

    const bounds = 1;

    const width = 400;

    const height = 400;

    // onClick: function (element, dataAtClick) {
    //   console.log(element, dataAtClick, this);
    // let valueX;
    // let valueY;
    // for (const scaleKey in this.scales) {
    //   const scaleRef: ScaleOptionsByType<ChartTypeRegistry[
    //   ChartType]['scales']> = this.scales[scaleKey];
    //   console.log(scaleKey, scaleRef);
    //   if (scaleRef.isHorizontal() && scaleKey === 'x-axis-1') {
    //     valueX = scaleRef.getValueForPixel(element.x);
    //   } else if (scaleKey === 'y-axis-1') {
    //     valueY = scaleRef.getValueForPixel(element.y);
    //   }
    // }
    // console.log(valueX, valueY);
    // scaleRef.getValueForPixel()
    // valueX = scaleRef.getValueForPixel(element.x);
    // if (scaleRef.isHorizontal() && scaleKey === 'x-axis-1') {
    //   valueX = scaleRef.getValueForPixel(element.offsetX);
    // } else if (scaleKey == 'y-axis-1') {
    //   valueY = scaleRef.getValueForPixel(element.offsetY);
    // }
    // },
    const options = ref<ChartOptions<'scatter'>>({
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Perceptron',
        },
      },
      scales: {
        x: {
          min: -bounds,
          max: bounds,
          position: 'center',
        },
        y: {
          min: -bounds,
          max: bounds,
          position: 'center',
        },
      },
    });

    const chartData = computed<ChartData<'scatter'>>(() => ({
      datasets: [
        {
          label: 'Type 1',
          data: [0],
          // data: points.value[0],
          radius: 4,
          backgroundColor: 'rgb(255, 99, 132)',
        },
        {
          label: 'Type 2',
          data: [1],
          // data: points.value[1],
          pointStyle: 'triangle',
          radius: 5,
          backgroundColor: 'rgb(99, 132, 255)',
        },
      ],
    }));

    function addPoint(event: MouseEvent, other: any): void {
      // prevent right click menu to be display
      console.log(event, other);
      event.preventDefault();

      const clickType = event.button;
      if (!(clickType === 2 || clickType === 0)) return;

      // setButtonType(clickType);
      console.log(chartRef.value);
      const chartInstance = chartRef.value?.chartInstance;
      console.log(chartInstance);
      const canvas = chartInstance?.canvas;
      // const canvasPosition = getRelativePosition(event, chartInstance);

      // console.log(canvasPosition);
      // console.log(chartRef.value?.chartInstance.scales.x.getValueForPixel);
    }

    return {
      chartData,
      chartRef,
      options,
      addPoint,
    };
  },
});
</script>
