<template>
  <div class="container" id="container">
    <h1 class="mb-4 text-center"><img src="../assets/logo.png" alt="로고"></h1>
    <form @submit.prevent="login" class="col-md-6 mx-auto">
      <div class="mb-3">
        <label for="username" class="form-label">아이디:</label>
        <input type="text" id="username" v-model.trim="username" class="form-control">
      </div>

      <div class="mb-3">
        <label for="password" class="form-label">비밀번호:</label>
        <input type="password" id="password" v-model.trim="password" class="form-control">
      </div>

      <button type="submit" class="btn btn-primary">로그인</button>
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
#container {
  margin-top: 100px;
}
</style>