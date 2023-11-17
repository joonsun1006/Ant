<template>
  <div>
    <h1>로그인 뷰</h1>
    <form @submit.prevent="login">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">비밀번호 : </label>
      <input type="password" id="password" v-model.trim="password"><br>

      <input type="submit" value="LogIn">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article'

const store = useArticleStore();

const login = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.login(payload);
}

const username = ref(null);
const password = ref(null);

</script>

<style scoped>

</style>