<template>
  <ScatterChart
    ref="chartRef"
    @click="addPoint"
    @contextmenu="addPoint"
    :chartData="chartData"
    :options="chartOptions"
    css-clases="chart-container"
  />
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import { ScatterChart, ExtractComponentData } from 'vue-chart-3';
import { Chart, registerables } from 'chart.js';
import { getRelativePosition } from 'chart.js/helpers';
import Point from '@/types/Point';
import { computed, ref } from 'vue';

Chart.register(...registerables);

@Options({
  name: 'PlotChart',
  components: {
    ScatterChart,
  },
  watch: {
    point: {
      deep: true,
      handler: function (newPoint) {
        this.point = newPoint;
        if (this.buttonType) {
          this.points[1] = [...this.points[1], newPoint];
        } else {
          this.points[0] = [...this.points[0], newPoint];
        }
      },
    },
    // setup(){
    //   const chartRef = ref<ExtractComponentData<typeof ScatterChart>>();
    //   return {chartRef};
    // },
  },
})
export default class PlotChart extends Vue {
  chartRef = ref<ExtractComponentData<typeof ScatterChart>>();
  // chartRef = ref();

  bounds = 1;

  width = 400;

  height = 400;

  points: Array<Array<Point>> = [[], []];

  buttonType = false;

  point: Point = { x: 0, y: 0 };

  chartOptions = {
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
        min: -this.bounds,
        max: this.bounds,
        position: 'center',
      },
      y: {
        min: -this.bounds,
        max: this.bounds,
        position: 'center',
      },
    },
  };

  chartData = computed(() => ({
    datasets: [
      {
        label: 'Type 1',
        data: this.points[0],
        radius: 4,
        backgroundColor: 'rgb(255, 99, 132)',
      },
      {
        label: 'Type 2',
        data: this.points[1],
        pointStyle: 'triangle',
        radius: 5,
        backgroundColor: 'rgb(99, 132, 255)',
      },
    ],
  }));

  setButtonType(type: number): void {
    this.buttonType = false; // type 1
    if (type === 2) {
      this.buttonType = true; // type 2
    }
  }

  addPoint(event: MouseEvent): void {
    // prevent right click menu to be display
    event.preventDefault();

    const clickType = event.button;
    if (!(clickType === 2 || clickType === 0)) return;

    this.setButtonType(clickType);
    console.log(this.chartRef.value);
    // console.log(this.chartRef);
    // console.log(this.chartRef.value);

    // console.log(this.chartRef.value?.chartInstance);
    // console.log(this.chartRef.value);
    // console.log(this.chartRef.value?.chartInstance);
    // const canvasPosition = getRelativePosition(
    //   event,
    //   this.chartRef.value.chartInstance
    // );
    // console.log(canvasPosition);
    // Substitute the appropriate scale IDs
    // const dataX = this.chartRef.value.chartInstance.scales.x.getValueForPixel(
    //   canvasPosition.x
    // );
    // const dataY = this.chartRef.value.chartInstance.scales.y.getValueForPixel(
    //   canvasPosition.y
    // );
    // this.point = { x: dataX, y: dataY };
  }
}
</script>
