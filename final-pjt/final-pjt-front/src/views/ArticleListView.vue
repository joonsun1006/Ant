<template>
  <div>
    <h1>아티클 리스트</h1>
    <RouterLink 
      v-for="article in store.articles"
      :key="article.pk"
      :article="article"
      :to="{ name: 'articleListItem', params: { article_pk: article.pk } }"
    >
      Article 개별 항목
      <hr>
    </RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import ArticleListItem from '@/components/ArticleListItem.vue';

const store = useArticleStore();

</script>

<style scoped>

</style>