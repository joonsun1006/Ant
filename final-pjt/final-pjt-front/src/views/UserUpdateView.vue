<template>
  <div class="container" id="container">
    <h1 class="mb-4 text-center">프로필 수정</h1>

    <div class="card">
      <div class="card-body">
        <p class="card-text"><strong>회원 번호:</strong> {{ user.id }}</p>
        <p class="card-text"><strong>ID:</strong> {{ user.username }}</p>
        <p class="card-text"><strong>닉네임:</strong> {{ user.nickname }}</p>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="text" class="form-control" v-model="email" id="email">
        </div>
        <div class="form-group">
          <label for="age">나이</label>
          <input type="text" class="form-control" v-model="age" id="age">
        </div>
        <div class="form-group">
          <label for="money">자산</label>
          <input type="text" class="form-control" v-model="money" id="money">
        </div>
        <div class="form-group">
          <label for="salary">연봉</label>
          <input type="text" class="form-control" v-model="salary" id="salary">
        </div>
        <button @click="updateuser" class="btn btn-primary">수정하기</button>
      </div>
    </div>

    <div class="mt-4">
      <h2>가입한 상품 정보</h2>
      <RegisteredItem v-for="register in registered" :register="register" />
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
const token = ref(null)
token.value = store.token
const router = useRouter()
const email = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/detail/${route.params.user_pk}/`,
  })
    .then((res) => {
        console.log(res.data)
      user.value = res.data;
    //   registered.value = res.data.financial_products.split(',')
      email.value = res.data.email
      console.log(email.value)
      age.value = res.data.age
      money.value = res.data.money
      salary.value = res.data.salary
    })
    .catch((err) => {
      console.log(err);
    })
})

const updateuser = () => {
    axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/detail/${route.params.user_pk}/`,
        data: {
            email: email.value,
            age: age.value,
            money: money.value,
            salary: salary.value,
        },
        headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
        router.push({ name: 'user'})
    })
}

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

.form-group {
  margin-bottom: 20px;
}
</style>