<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="submitData">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title"><br><br>

      <label for="content">내용 : </label>
      <textarea id="content" v-model="content"></textarea><br>

      <button @submit.prevent="submitData">create</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article.js'

const store = useArticleStore();
const title = ref('');
const content = ref('');

const submitData = function () {
  const article = {
    title: title.value,
    content: content.value,
  }
  store.createArticle(article);
  title.value = '';
  content.value = '';
};


</script>

<style scoped>

</style>