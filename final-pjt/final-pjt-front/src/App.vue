<template>
  <div id="container">
    <header>
      <div class="position relative">
        <nav class="navbar bg-body-tertiary sticky-top" style="background-color: #E6E6E6 !important;">
          <div class="container-fluid -5">
            <a class="navbar-brand logo" href="/"><img src="./assets/logo2.png" style="width: 40px; height: 40px;"></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
                <div v-if="!store.isLogin">
                  <button @click="login" data-bs-dismiss="offcanvas" class="btn btn-primary">로그인</button> | 
                  
                  <button @click="signup" data-bs-dismiss="offcanvas" class="btn btn-success">회원가입</button>
                </div>
                <div v-else>
                  <button @click.prevent="store.logout" data-bs-dismiss="offcanvas" class="btn btn-danger">로그아웃</button>
                </div>

                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                  <li class="nav-item">
                    <a href="/" class="nav-link">Home</a>
                  </li>

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
    <footer class="bg-dark text-light text-center py-3">
      <div class="container-fluid">
        <p>&copy; 2023 개미의 안식처. All Rights Reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
  import { RouterLink, RouterView, useRouter } from 'vue-router'
  import { useArticleStore } from './stores/article'
  
  
  const store = useArticleStore()
  const router = useRouter()

  const login = function () {
    router.push({name: 'login'} )
  }

  const signup = function () {
    router.push({ name: 'signup' })
  }

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
  width: 50px;
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
  position: fixed;
  bottom: 0;
  width: 100%;
  z-index: 1000;
}


/* 992픽셀 이상인 화면에서만 간격을 주도록 하는 미디어 쿼리 */
@media (min-width: 992px) {
  .nav-spacing {
    margin-right: 70px;
  }
}

#container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: rgb(248, 233, 233);
}


</style>