<template>
  <div>
    <h1>클릭한 해당 아티클 리스트 아이템</h1>
    <p>x번 글</p>
    <p>제목: </p>
    <hr>
    <p>작성일: </p>
    <p>수정일: </p>
    <hr>
    <p>내용: </p>
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