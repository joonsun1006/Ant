<template>
  <div class="container d-flex justify-content-center align-items-center vh-100">
    <div class="text-center">
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
        <form @submit.prevent="createComment">
          <label for="content">내용 : </label>
          <input type="text" id="content" v-model="content">
          <button>댓글 작성</button>
        </form>
        <p
          v-for="comment in article.comment_set"
          :key="comment.id"
        >
        
        익명 : {{ comment.content }}
        <p>comment.id : {{ comment.id }}</p>
        <div>
          <button
            @click="deleteComment(comment.id)"
            
          >
            삭제
          </button>
        </div>
        </p>
      </div>
    </div>
  </div>


</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article'

const store = useArticleStore();
const route = useRoute();
const router = useRouter();
const article = ref([]);
const content = ref(null);
const API_URL = 'http://127.0.0.1:8000';
const token = ref(null);
token.value = store.token;

onMounted(() => {
  axios({
    method: 'get',
    url: `${API_URL}/articles/${route.params.article_pk}/`,
  })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    })
})


const createComment = () => {
  axios({
    method: 'post',
    url: `${API_URL}/articles/${route.params.article_pk}/comment/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${token.value}`
    }
  })
    .then((res) => {
      console.log(res.data)
      return axios({
        method: 'get',
        url: `${API_URL}/articles/${route.params.article_pk}/`,
      })
      .then((res) => {
        router.go();
        })
    })
}

const deleteComment = (comment_pk) => {
  console.log(comment_pk)
  axios({
    method: 'delete',
    url: `${API_URL}/articles/comment/${comment_pk}/`,
    headers: {
      Authorization: `Token ${token.value}`
    },
  })
    .then(() => {
      // 댓글 삭제 후, 해당 글의 정보를 다시 가져와서 댓글 목록을 업데이트
      return axios({
        method: 'get',
        url: `${API_URL}/articles/${route.params.article_pk}/`,
      });
    })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
}

</script>

<style scoped>

</style>