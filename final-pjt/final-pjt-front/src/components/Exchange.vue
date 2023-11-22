<template>
  <div id="container" class="container">
    <h1 class="mb-4">환율 계산기</h1>
    <div class="mb-3">
      <label for="currency" class="form-label">통화 선택</label>
      <select v-model="selected" class="form-select">
        <option v-for="key in Object.keys(exchange)">{{ key }}</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="won" class="form-label">원화</label>
      <div class="input-group">
        <input type="number" :value="won" @input="wonChange" class="form-control" id="won">
        <span class="input-group-text">원</span>
      </div>
    </div>
    <div class="mb-3">
      <label for="foreign" class="form-label">대상</label>
      <div class="input-group">
        <input type="number" :value="foreign" @input="foreignChange" class="form-control" id="foreign">
        <span class="input-group-text">{{ selected }}</span>
      </div>
    </div>
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
  foreign.value = won.value / exchange.value[selected.value]
  foreign.value = foreign.value.toFixed(2)
}

const foreignChange = function (event) {
  foreign.value = event.target.value
  won.value = foreign.value * exchange.value[selected.value]
  won.value = won.value.toFixed(2)
}
</script>

<style scoped>
#container {
  margin-top: 60px;
}
</style>