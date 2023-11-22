<template>
  <div class="container col-8" id="container">
    <div class="card" id="card">
      <div class="card-body">
        <p class="card-text">{{ article.id }}번 글</p>
        
        <!-- 제목, 작성,수정일, 글내용 -->
        <h1 class="card-title">제목: {{ article.title }}</h1>
        <div>
          <p class="card-text text-end">작성: {{ article.created_at?.substr(0,10) }} {{ article.created_at?.substr(11,8) }}</p>
          <p class="card-text text-end">수정: {{ article.updated_at?.substr(0,10) }} {{ article.created_at?.substr(11,8) }}</p>
        </div>
        <p class="card-text" id="article-content">내용: {{ article.content }}</p>
        <hr>

        <!-- 댓글작성 폼 -->
        <form @submit.prevent="createComment" class="mb-3 row">
          <div class="col-10 col-md-11 mb-3">
            <label for="content"></label>
            <input type="text" placeholder="댓글을 입력하세요" id="content" v-model="content" class="form-control">
          </div>
          <div class="col-2 col-md-1" id="dm-button">
            <button class="btn btn-primary mt-2"><img src="../assets/dm_icon.png" alt="dm"></button>
          </div>
        </form>

        <!-- 댓글목록 -->
        <div v-if="article.comment_set?.length > 0">
          <div v-for="comment in article.comment_set" :key="comment.id" class="card mt-3">
            <div class="card-body">
              <p class="card-text">익명: {{ comment.content }}</p>
              <p class="card-text">comment.id: {{ comment.id }}</p>
              <div>
                <button @click="deleteComment(comment.id)" class="btn btn-danger">삭제</button>
              </div>
            </div>
          </div>
        </div>
        <div v-else>
          <p>아직 댓글이 없습니다.</p>
        </div>
        
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
img {
  width: 15px;
}

#dm-button {
  margin-top: 15px;
  padding-left: 1px;
}

#article-content {
  width: 70%;
  padding-top: 30px;
}

#container {
  margin-top: 60px;
}

</style>