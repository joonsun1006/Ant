import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import UserView from '@/views/UserView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleListItem from '@/components/ArticleListItem.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import Exchange from '@/components/Exchange.vue'
import Map from '@/components/Map.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/user',
      name: 'user',
      component: UserView
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticleView
    },
    {
      path: '/articleListItem/:article_pk',
      name: 'articleListItem',
      component: ArticleListItem
    },
    {
      path: '/articleCreate',
      name: 'articleCreate',
      component: ArticleCreateView
    },
    {
      path: '/exchange-rate',
      name: 'exchange',
      component: Exchange
    },
    {
      path: '/map',
      name: 'map',
      component: Map
    },
  ]
})

export default router
