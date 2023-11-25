
<template>
  <div>
    <header>
      <div  class="position relative">
        <nav class="navbar bg-body-tertiary sticky-top">
          <div class="container-fluid -5">
            <a class="navbar-brand logo" href="/"><img src="./assets/logo2.png" style="width: 40px; height: 40px;">&nbspFinew</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                  <li class="nav-item">
                    <a href="/" class="nav-link">Home</a>
                  </li>
                  <div v-if="!store.isLogin">
                    <li class="nav-item">
                      <a href="/signup" class="nav-link" v-if="!store.isLogin">회원가입</a>
                    </li>
                    <li class="nav-item">
                      <a href="/login" class="nav-link" v-if="!store.isLogin">로그인</a>
                    </li>
                  </div>
                  <div v-else>
                    <li class="nav-item">
                      <a href="/" @click.prevent="store.logout" class="nav-link">로그아웃</a>
                    </li>
                  </div>
                  <li class="nav-item">
                    <a href="/deposit" class="nav-link">예적금비교</a>
                  </li>
                  <li class="nav-item">
                    <a href="/exchange-rate" class="nav-link">환율계산기</a>
                  </li>
                  <li class="nav-item">
                    <a href="/map" class="nav-link">은행지도</a>
                  </li>
                  <li class="nav-item">
                    <a href="/articles" class="nav-link">게시판</a>
                  </li>
                  <li class="nav-item">
                    <RouterLink :to="{ name: 'user', params:{ user_pk : store.userId } }" class="nav-link nav-hover"
                      v-if="store.isLogin"
                    >프로필
                    </RouterLink>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </nav>
        <RouterView />
      </div>
    </header>
  </div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import { useArticleStore } from './stores/article'
  const store = useArticleStore()
</script>


<style scoped>

</style>