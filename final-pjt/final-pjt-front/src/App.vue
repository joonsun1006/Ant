<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid ">
        <RouterLink :to="{ name: 'home' }" class="navbar-brand">Home</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <RouterLink :to="{ name: 'articles' }" class="nav-link">
              게시판
            </RouterLink>

            <!-- 로그인 안돼있을 때 -->
            <RouterLink :to="{ name: 'login' }" class="nav-link active" aria-current="page"
              v-if="!store.isLogin"
            >로그인
            </RouterLink>
            <RouterLink :to="{ name: 'signup' }" class="nav-link"
              v-if="!store.isLogin"
            >회원가입
            </RouterLink>

            <!-- 로그인 돼있을 때 -->
            <RouterLink :to="{ name: 'user' }" class="nav-link"
              v-if="store.isLogin"
            >프로필
            </RouterLink>
            <RouterLink :to="{ name: 'home' }" class="nav-link"
              @click="store.logout"
              v-if="store.isLogin"
            >로그아웃
            </RouterLink>
          </div>
        </div>
      </div>
    </nav>
    <RouterView />
  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/article';

const store = useArticleStore();


</script>

<style scoped>

</style>
