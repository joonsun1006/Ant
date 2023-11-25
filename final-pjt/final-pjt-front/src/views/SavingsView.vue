<template>
  <div id="container">
    <nav>
      <RouterLink :to="{ name: 'deposit' }" class="nav-link">
        정기예금
      </RouterLink>
      <RouterLink :to="{ name: 'savings' }" class="nav-link">
        <span id="saving-color">정기적금</span>
      </RouterLink>
    </nav>

    <div id="under-container">

      <!-- 검색 -->
      <h2>검색하기</h2>
      <div class="custom-width mb-4">
        <label for="bankSelect" class="form-label">은행 선택</label>
        <select id="bankSelect" v-model="selected" @change="updateCityOptions" class="form-select">
          <option value="showall">전체보기</option>
          <option v-for="name in bankName" :value="name" :key="name">{{ name }}</option>
        </select>
      </div>
      <!-- 테이블 -->
      <table class="table table-bordered">
        <thead>
          <tr>
            <th class="theader">공시제출월</th>
            <th class="theader">금융 회사명</th>
            <th class="theader">상품명</th>
            <th class="theader">6개월 금리</th>
            <th class="theader">12개월 금리</th>
            <th class="theader">24개월 금리</th>
            <th class="theader">36개월 금리</th>
          </tr>
        </thead>
        <tbody>
          <SavingsItem v-for="saving in savings"
          :key="saving.id"
          :saving="saving" />
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import SavingsItem from '../components/SavingsItem.vue'
const selected = ref('')
const original_savings = ref([])
const savings = ref([])
const bankName = ref([])
onMounted(() => {
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/finance/savings/`
  }).then((res) => {
    savings.value = res.data
    original_savings.value = res.data
    bankName.value =  [...new Set(res.data.map(name=>name.kor_co_nm))]
  })
})
const updateCityOptions = function () {
  savings.value = original_savings.value.filter(item => item.kor_co_nm === selected.value)
  if (selected.value === 'showall'){
    savings.value = original_savings.value
  }
}
</script>

<style scoped>
#container {
  margin-top: 60px;
  margin-bottom: 100px;
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

#saving-color {
  color: #B5E61D;
}

.theader {
  background-color: rgb(235, 245, 235);;
}

#under-container {
  padding-left: 60px;
  padding-right: 60px;
}

.custom-width {
  width: 50%;
}
</style>