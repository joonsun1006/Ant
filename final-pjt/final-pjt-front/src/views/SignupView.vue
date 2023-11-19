<template>
  <div>
    <h1>회원가입 뷰</h1>
    <form @submit.prevent="signup">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password1">비밀번호 : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>

      <label for="password2">비밀번호 확인 : </label>
      <input type="password" id="password2" v-model.trim="password2"><br>

      <!-- 닉네임, 이메일, 나이, 돈, 월급 -->
      <label for="nickname">닉네임 : </label>
      <input type="text" id="nickname" v-model.trim="nickname"><br>
      
      <label for="email">이메일 : </label>
      <input type="text" id="email" v-model.trim="email"><br>

      <label for="age">나이 : </label>
      <input type="text" id="age" v-model.trim="age"><br>

      <label for="money">돈 : </label>
      <input type="text" id="money" v-model.trim="money"><br>

      <label for="salery">연봉 : </label>
      <input type="text" id="salery" v-model.trim="salary"><br>

      <input type="submit" value="SignUp">
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

</style>