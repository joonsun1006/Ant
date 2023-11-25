<template>
  <div class="container" id="container">
    <h1 class="mb-4 text-center">회원가입</h1>
    <form @submit.prevent="signup">
      <div>
        <label for="username" class="form-label"></label>
        <input type="text" placeholder="아이디" id="username" v-model.trim="username" class="form-control">
      </div>

      <div>
        <label for="password1" class="form-label"></label>
        <input type="password" placeholder="비밀번호" id="password1" v-model.trim="password1" class="form-control">
      </div>

      <div class="mb-3">
        <label for="password2" class="form-label"></label>
        <input type="password" placeholder="비밀번호 확인" id="password2" v-model.trim="password2" class="form-control">
      </div>

      <div>
        <label for="nickname" class="form-label"></label>
        <input type="text" placeholder="닉네임" id="nickname" v-model.trim="nickname" class="form-control">
      </div>
      
      <div class="mb-3">
        <label for="email" class="form-label"></label>
        <input type="text" placeholder="이메일" id="email" v-model.trim="email" class="form-control">
      </div>

      <p id="money-info">자산정보</p>
      <div>
        <label for="age" class="form-label"></label>
        <input type="text" placeholder="나이" id="age" v-model.trim="age" class="form-control">
      </div>
      
      <div>
        <label for="money" class="form-label"></label>
        <input type="text" placeholder="자산" id="money" v-model.trim="money" class="form-control">
      </div>
      
      <div class="mb-3">
        <label for="salery" class="form-label"></label>
        <input type="text" placeholder="연봉" id="salery" v-model.trim="salary" class="form-control">
      </div>
      
      <button type="submit" class="btn btn-primary">SignUp</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article';

const store = useArticleStore();

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const nickname = ref(null);
const email = ref(null);
const age = ref(null);
const money = ref(null);
const salary = ref(null);

const signup = function() {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
  };
  store.signup(payload);
};
</script>

<style scoped>
#money-info {
  padding-top: 20px;
  margin-bottom: -15px;
}

#container {
  margin-top: 70px;
}
</style>