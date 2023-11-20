<template>
  <h1>게시판 뷰(목록+제목+게시글생성까지만)</h1>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="text-center">
      <ArticleListView />
      <button @click="router.push({name: 'articleCreate'})">글쓰기</button>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import ArticleListView from '@/views/ArticleListView.vue';

const router = useRouter();

</script>

<style scoped>

</style>