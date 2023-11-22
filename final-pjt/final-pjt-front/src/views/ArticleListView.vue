<template>
  <div class="container mt-5">
    <h1 class="mb-4">글 목록</h1>
    <div v-for="article in sortedArticles" :key="article.pk" class="card mb-3">
      <div class="card-body d-flex justify-content-between align-items-center">
        <h5 class="card-title col-8">
          <span>{{ article.pk }}. </span>
          <RouterLink
            :to="{ name: 'articleListItem', params: { article_pk: article.pk } }"
            class="text-decoration-none"
            v-if="article.title.length < 15"
          >
            {{ article.title }}
          </RouterLink>
          <RouterLink
            :to="{ name: 'articleListItem', params: { article_pk: article.pk } }"
            class="text-decoration-none"
            v-if="article.title.length >= 15"
          >
            {{ article.title.substr(0, 15) }}...
          </RouterLink>
        </h5>

        <!-- 작성일 -->
        {{ article.created_at.substr(5, 5) }}<span class="d-none d-sm-block"> {{ article.created_at.substr(11, 5) }}</span>
        
        <!-- 댓글갯수 -->
        <span class="card-text">
          <img src="../assets/comments.png" alt="댓글">
          {{ article.comment_count }}
        </span>
          
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue';
import axios from 'axios';
import { useRoute, RouterLink, RouterView } from 'vue-router';
import { useArticleStore } from '@/stores/article';
import ArticleListItem from '@/components/ArticleListItem.vue';

const store = useArticleStore();
const sortedArticles = ref([]);

const articleDetail = ref([]);
const API_URL = 'http://127.0.0.1:8000';
const route = useRoute();

const sortArticles = () => {
  sortedArticles.value = [...store.articles].sort((a, b) => b.pk-a.pk);
}

onMounted(() => {
  store.getArticles();
  sortArticles();
});

watch(() => store.articles, () => {
  sortArticles();
});


</script>

<style scoped>
.card {
  width: 100%;
  margin-bottom: 1rem;
}

.card-title {
  font-size: 1.25rem;
}

.card-text {
  font-size: 1rem;
  color: #6c757d;
}

img {
  width: 15px;
}
</style>
