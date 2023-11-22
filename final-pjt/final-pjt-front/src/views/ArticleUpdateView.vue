<template>
  
    <div class="card">
      <div class="card-body">
        <p class="card-text">{{ article.id }}번 글</p>
        
        <!-- 제목, 작성,수정일, 글내용 -->
        <h1 class="card-title">제목: <input type="text" v-model="title"></h1>
 
        <p class="card-text" id="article-content">내용: <input type="text" v-model="content"></p>
        <hr> 
        <button @click="updatepost">수정하기</button>

        
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
const title = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${API_URL}/articles/${route.params.article_pk}/`,
  })
    .then((res) => {
      article.value = res.data;
      console.log(res.data)
      title.value = res.data.title
      content.value = res.data.content
    })
    .catch((err) => {
      console.log(err);
    })
})

const updatepost = () => {
    axios({
        method: 'put',
        url: `${API_URL}/articles/${route.params.article_pk}/`,
        data: {
        title: title.value,
        content: content.value,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      router.push({ name: 'articles' });
    })
    
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

</style>