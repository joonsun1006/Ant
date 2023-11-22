<template>
  <div class="container" id="container">
    <h1 class="mb-4 text-center">Profile</h1>

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

    <div class="mt-4">
      <h2>가입한 상품 정보</h2>
      <RegisteredItem v-for="register in registered"
    :register="register"
    />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article'
import RegisteredItem from '@/components/RegisteredItem.vue'
const store = useArticleStore();
const route = useRoute();
const user = ref({})
const registered = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/detail/${route.params.user_pk}/`,
  })
    .then((res) => {
      user.value = res.data;
      registered.value = res.data.financial_products.split(',')
    })
    .catch((err) => {
      console.log(err);
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
  margin-top: 60px;
}
</style>