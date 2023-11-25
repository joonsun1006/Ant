<template>
  <div class="container" id="container">
    <h1 class="mb-4">게시글 생성 페이지</h1>
    <form @submit.prevent="submitData">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input type="text" id="title" v-model="title" class="form-control">
      </div>

      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea id="content" v-model="content" class="form-control"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Create</button>
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
input {
  width: 100%;
}

textarea {
  width: 100%;
  height: 30em;
  resize: none;
}

#container {
  margin-top: 100px;
}

</style>