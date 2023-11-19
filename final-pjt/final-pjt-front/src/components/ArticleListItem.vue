<template>
  <div>
    <p>{{article.id}}번 글</p>
    <h1>제목: {{ article.title }}</h1>
    <hr>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>
    <hr>
    <p>내용: {{ article.content }}</p>
    <hr>
    <h3>댓글</h3>
    <form @submit.prevent="">
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="content">
      <button>댓글 작성</button>
      <!-- <p v-for="cmt in comments">{{ cmt.post }} {{ cmt.content }}</p> -->
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import { useArticleStore } from '@/stores/article'

const store = useArticleStore();
const route = useRoute();
const article = ref([]);
const content = ref(null);
const comments = ref([]);

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/articles/${route.params.article_pk}/`,
  })
    .then((res) => {
      console.log(res.data);
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    })
})

</script>

<style scoped>

</style>