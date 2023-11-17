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

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article';

const store = useArticleStore();

const signup = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signup(payload);
};

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);



</script>

<style scoped>

</style>