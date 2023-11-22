<template>
  <div id="app">
    <header>
      <nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">
      <div class="container-fluid ">
        <div>
          <RouterLink :to="{ name: 'home' }" class="navbar-brand"><img src="./assets/naver_favicon.png" alt="logo" id="logo"></RouterLink>
        </div>
        
        
        <!-- 화면 작아질 때 햄버거 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        

        <div class="collapse navbar-collapse justify-content-center" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <RouterLink :to="{ name: 'articles' }" class="nav-link nav-hover nav-spacing">
              게시판
            </RouterLink>

            <RouterLink :to="{ name: 'exchange' }" class="nav-link nav-hover nav-spacing">
              환율
            </RouterLink>

            <RouterLink :to="{ name: 'map' }" class="nav-link nav-hover nav-spacing">
              지도
            </RouterLink>

            <RouterLink :to="{ name: 'deposit' }" class="nav-link nav-hover nav-spacing">
              예적금
            </RouterLink>

          </div>
        </div>
        
        <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            
          <!-- 로그인 안돼있을 때 -->
          <RouterLink :to="{ name: 'login' }" class="nav-link active nav-hover" aria-current="page"
            v-if="!store.isLogin"
          >로그인
          </RouterLink>
          
          <RouterLink :to="{ name: 'signup' }" class="nav-link nav-hover"
            v-if="!store.isLogin"
          >회원가입
          </RouterLink>
            
            
          <!-- 로그인 돼있을 때 -->
          <RouterLink :to="{ name: 'user', params:{ user_pk : store.userId } }" class="nav-link nav-hover"
            v-if="store.isLogin"
          >프로필
          </RouterLink>
          
          <RouterLink :to="{ name: 'home' }" class="nav-link nav-hover"
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
  <footer class="bg-dark text-light text-center py-3">
    <div class="container-fluid">
      <p>&copy; 2023 우리의 금융 사이트. All Rights Reserved.</p>
    </div>
  </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useArticleStore } from '@/stores/article';

const store = useArticleStore();



</script>

<style scoped>
.nav-link.nav-hover:hover {
  background-color: gray;
  color: #000;
}

.nav-link {
  font-weight: bold;
  font-size: large;
}

#logo {
  width: 30px;
}

#profile {
  width: 25px;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

footer {
  margin-top: auto;
}

/* nav {
  height: 7rem;
} */

/* 768픽셀 이상인 화면에서만 간격을 주도록 하는 미디어 쿼리 */
@media (min-width: 992px) {
  .nav-spacing {
    margin-right: 70px;
  }
}

</style>
