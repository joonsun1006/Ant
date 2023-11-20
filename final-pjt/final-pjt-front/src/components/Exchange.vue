<template>
  <div>
    <h1>환율계산기</h1>
    <div>
      <select v-model="selected">
        <option v-for="key in Object.keys(exchange)">{{ key }}</option>
      </select>
      <label for="won"> 원화 </label>
      <input type="number" :value="won" @change="wonChange" id="won">


    </div>
    <label for="foreign"> 대상 </label>
    <input type="number" :value="foreign" @change="foreignChange" id="foreign">

  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useArticleStore } from '@/stores/article'
const exchange = ref({})
const selected = ref('')
const won = ref(0)
const foreign = ref(0)

onMounted(() => {
  axios({
    url: `http://127.0.0.1:8000/finance/exchange-rate/`
  })
    .then((res) => {
      exchange.value = res.data
    })
})



const wonChange = function (event) {
  won.value = event.target.value
  console.log(won.value, exchange.value[selected.value])
  foreign.value = won.value / exchange.value[selected.value]
  foreign.value = foreign.value.toFixed(2)
}

const foreignChange = function (event) {
  foreign.value = event.target.value
  console.log(won.value, foreign.value)
  won.value = foreign.value * exchange.value[selected.value]
  won.value = won.value.toFixed(2)
}
</script>

<style lang="scss" scoped></style>