<template>
  <div id="container">
    <nav>
      <RouterLink :to="{ name: 'deposit' }" class="nav-link">
        <span id="deposit-color">정기예금</span>
      </RouterLink>
      <RouterLink :to="{ name: 'savings' }" class="nav-link">
        정기적금
      </RouterLink>
    </nav>

    <!-- 검색 -->
    <h2>검색하기</h2>
    <p>검색 조건을 입력하세요</p>

    <!-- 테이블 -->
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>공시제출월</th>
          <th>금융 회사명</th>
          <th>상품명</th>
          <th>6개월 금리</th>
          <th>12개월 금리</th>
          <th>24개월 금리</th>
          <th>36개월 금리</th>
        </tr>
      </thead>
      <tbody>
        <DepositItem v-for="deposit in deposits"
          :key="deposit.id"
          :deposit="deposit" />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import DepositItem from '../components/DepositItem.vue'

const deposits = ref([])

onMounted(() => {
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/finance/deposit/`
  }).then((res) => {
    deposits.value = res.data
  })
})
</script>

<style scoped>
#container {
  margin-top: 60px;
}

nav {
  margin-bottom: 30px;
}
.nav-link {
  text-decoration: none;
  font-weight: bold;
  font-size: 16px;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-link:hover {
  background-color: whitesmoke;
}

#deposit-color {
  color: #B5E61D;
}


</style>