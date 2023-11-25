<template>
    <div class="container">
        <canvas class="chart" id="chartCanvas"></canvas>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useArticleStore } from '@/stores/article'
import { Chart, registerables } from 'chart.js';
import { useRoute } from 'vue-router';

Chart.register(...registerables);

const store = useArticleStore()
const product = ref([])
const nomalrate = ref([])
const rate = ref([])
const route = useRoute()

let chart
let chartData = ref(null)

onMounted(() => {
    axios({
    method: 'get',
    url: `http://127.0.0.1:8000/finance/registered/${route.params.user_pk}`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res.data)
      res.data.forEach(item => {
        product.value.push(item.fin_prdt_nm)
        nomalrate.value.push(item.intr_rate_12)
        rate.value.push(item.intr_rate2_12)  
      });

      console.log(product.value)
      console.log(nomalrate.value)
      return res
    })
    .then((res) => {
      chartData.value = {
        labels: product.value,
        datasets: [
            {
                label: '기본 금리',
                // data: nomalrate.value
                data: nomalrate.value,
                backgroundColor: [
                  'rgba(255, 99, 132, 1)'
                ]
            },
            {
                label: '우대 금리',
                data: rate.value,
                backgroundColor: [
                  'rgba(54, 162, 235, 1)'
                ]
            }
        ]
        } 
        console.log(1, chartData.value)
    
        // const chartData = ref({
        // labels: ['a', 'b', 'c'],
        // datasets: [
        //     {
        //         label: '정기 금리',
        //         // data: nomalrate.value
        //         data: [10, 20, 30]
        //     }
        // ]
        // })  
        // return chartData
        const canvas = document.getElementById('chartCanvas');
        if (canvas) {
            chart = new Chart(canvas.getContext('2d'), {
                type: 'bar',
                // data: res.value.datasets,
                data: chartData.value,
                options: {
                    grouped: true
                }
            })
        }
    })
    .catch((res) => {
      console.log(res)
    })
  
})
</script>

<style scoped>
.container {
  border: 1px solid black;
}
.chart{
  width: 0%;
  margin: 10px;
}

</style>