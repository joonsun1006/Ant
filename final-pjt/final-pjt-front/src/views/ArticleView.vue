<template>
  <div class="container" id="container">
    <h1 class="display-4 text-center mb-5">자유 게시판</h1>
    <div class="card mx-auto mb-5">
      <div class="card-body">
        <button @click="router.push({name: 'articleCreate'})" class="btn btn-primary">글쓰기</button>
        <ArticleListView />
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import ArticleListView from '@/views/ArticleListView.vue';

const router = useRouter();

</script>

<style scoped>
.card {
  width: 100%;
  max-width: 50rem;
  margin: 0 auto;
}

#container {
  margin-top: 100px;
  margin-bottom: 90px;
}

</style>