<template>
  <div>
    <canvas ref="plotRef" id="plot" />
  </div>
</template>

<script lang="ts">
import { Options, PropOptions, Vue } from 'vue-class-component';
import {
  Chart,
  ChartConfiguration, ChartData, ChartOptions,
  ChartTypeRegistry,
  registerables,
  ScatterControllerChartOptions, ScatterDataPoint
} from 'chart.js';
import { computed, ref } from 'vue';
import Point from '@/types/Point';

Chart.register(...registerables);

@Options({
  name: 'PlotChart',
})
export default class PlotChart extends Vue {
  labels: Array<string> = [] ;

  colors: Array<string> = [] ;

  bounds = 1;

  title = 'Perceptron';

  points = ref<Array<Array<ScatterDataPoint>>>([[], []]);

  // plotData: Array<number> = [];
  plotData: ChartData<'scatter'> = {
    datasets: [
      {
        label: 'Type 1',
        // data: [0],
        data: this.points.value[0],
        // radius: 4,
        backgroundColor: 'rgb(255, 99, 132)',
      },
      {
        label: 'Type 2',
        data: [1],
        // data: points.value[1],
        pointStyle: 'triangle',
        // radius: 5,
        backgroundColor: 'rgb(99, 132, 255)',
      },
    ],
  };

  charOptions = ChartOptions<'scatter'>({
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: this.title,
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
  });

  plot = undefined;

  mounted() {
    this.createChart({
      datasets: [
        {
          data: this.plotData,
          backgroundColor: this.colors
        }
      ],
      labels: this.labels
    });
  }

  createChart(chartData: ChartData<'scatter'>) {
    // const canvas = document.getElementById('plot') as HTMLCanvasElement
    const canvas = this.$refs.plotRef as HTMLCanvasElement;
    const config: ChartConfiguration = {
      type: 'scatter',
      data: chartData,
      options: this.charOptions
    };
    this.plot = new Chart(canvas, config);
  }
}
</script>
