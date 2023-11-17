<template>
  <div>
    <h1>게시판 뷰(목록+제목+게시글생성까지만)</h1>
    <ArticleListView />
    <button @click="router.push({name: 'articleCreate'})">게시글 생성</button>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import ArticleListView from '@/views/ArticleListView.vue';

const router = useRouter();

</script>

<style scoped>

</style>