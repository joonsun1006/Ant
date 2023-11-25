<template>
  <div class="container" id="container">
    <h1 class="mb-4 text-center">Profile</h1>
    <div class="button-group">
      <button @click="router.push({ name: 'userupdate', params: { user_pk: userId } })" class="btn btn-primary">회원 수정하기</button>
      <button @click="changePassword" class="btn btn-secondary">비밀번호 변경</button>
    </div>

    <div class="card">
      <div class="card-body">
        <p class="card-text"><strong>회원 번호:</strong> {{ user.id }}</p>
        <p class="card-text"><strong>ID:</strong> {{ user.username }}</p>
        <p class="card-text"><strong>Email:</strong> {{ user.email }}</p>
        <p class="card-text"><strong>닉네임:</strong> {{ user.nickname }}</p>
        <p class="card-text"><strong>나이:</strong> {{ user.age }}</p>
        <p class="card-text"><strong>자산:</strong> {{ user.money }}</p>
        <p class="card-text"><strong>연봉:</strong> {{ user.salary }}</p>
      </div>
    </div>

    <div class="mt-5">
      <h2 class="text-center mb-4">가입한 상품 정보</h2>
      <div v-if="registered">
        <div
          v-for="(register, index) in registered"
          :key="index"
          class="registered-item"
        >
          <RegisteredItem :register="register" />
        </div>
      </div>
      <div v-else>
        <div class="no-products">
          <p class="text-center">가입한 상품이 없습니다.</p>
        </div>
      </div>
    </div>
    <div class="mb-5 rec-margin text-center">
      <hr class="mb-5">
      <h2 class="text-center mb-5">당신을 위한 추천 상품</h2>
      <p class="text-center">
        <p class="text-center">지금까지의 투자와 당신의 프로필을 고려하여</p>
        <p class="text-center"><strong>알파고</strong>가 추천하는 <span id="font-styling">최적의 투자 상품</span>입니다.</p>
        <p class="text-center">유사한 투자자들이 가장 많이 선택한 상품을 아래에서 확인하세요!</p>
      </p>
      <img src="../assets/alphago.jpg" alt="알파고">
      <div class="recommendation-container">
        <div class="recommendation-card" @click="goDetail(recommend.id)">
          <div class="recommendation-header">
            <h3 class="recommendation-title">★ {{ recommend.kor_co_nm }} - {{ recommend.fin_prdt_nm }} ★</h3>
          </div>
        </div>
      </div>
    </div>
    <ChartView />
  </div>
  <PasswordChangeView id="open"/>

</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import RegisteredItem from '@/components/RegisteredItem.vue'
import ChartView from '@/views/ChartView.vue'
import PasswordChangeView from './PasswordChangeView.vue'

const changePassword = () => {
  const dialog = document.querySelector("#open");
  dialog.showModal();
};

const store = useArticleStore()
const route = useRoute()
const router = useRouter()
const user = ref({})
const registered = ref(null)
const recommend = ref('')
const image = ref('')
const goDetail = function (deposit_pk) {
  router.push({name:'dnsdetail', params:{dns_pk:deposit_pk}})
}
onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/detail/${route.params.user_pk}/`,
  })
    .then((res) => {
      user.value = res.data;
      if (res.data.financial_products === '') {
        registered.value = null
      }
      else {
        registered.value = res.data.financial_products.split(',')
      }
    })
    .catch((err) => {
      console.log(err);
    })
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/finance/recommend/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      recommend.value = res.data
    })
})
</script>

<style scoped>
.container {
  max-width: 800px;
}

.card {
  width: 100%;
  max-width: 400px;
  margin: auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-body {
  text-align: left;
  padding: 20px;
}

#container {
  margin-top: 100px;
  margin-bottom: 100px;
}

.registered-items {
  margin-top: 20px;
}

.registered-item {
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.registered-item:hover {
  background-color: #e0e0e0;
  cursor: pointer;
}

.no-products {
  padding: 20px;
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  text-align: center;
}

.button-group {
  margin-bottom: 20px;
  text-align: center;
}

.btn {
  margin-right: 10px;
}

.recommendation-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.recommendation-card {
  background-color: #ffffff;
  border: 1px solid #ddd;
  padding: 20px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
  cursor: pointer;
}

.recommendation-card:hover {
  background-color: #f5f5f5;
}

.recommendation-header {
  text-align: center;
}

.recommendation-title {
  margin: 0;
  color: #007bff;
}

.rec-margin {
  margin-top: 100px;
}

#font-styling {
  font-weight: bold;
  font-size: 20px;
}

</style>