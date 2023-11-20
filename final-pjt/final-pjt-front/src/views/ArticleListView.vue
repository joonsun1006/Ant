<template>
  <div>
    <h1>글 목록</h1>
    <div
      v-for="article in store.articles"
      :key="article.pk"
      :article="article"
    >
      {{ article.pk }}
      <RouterLink 
        :to="{ name: 'articleListItem', params: { article_pk: article.pk } }"
      >
        {{ article.title }}
      </RouterLink>
      [{{ article.comment_count }}]
      <hr>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import ArticleListItem from '@/components/ArticleListItem.vue';

const store = useArticleStore();

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

</style>