import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import UserView from '@/views/UserView.vue'
import UserUpdateView from '@/views/UserUpdateView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleListItem from '@/components/ArticleListItem.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import Exchange from '@/components/Exchange.vue'
import Map from '@/components/Map.vue'
import Test from '@/components/Test.vue'
import TestMap from '@/components/TestMap.vue'
import DepositView from '@/views/DepositView.vue'
import SavingsView from '@/views/SavingsView.vue'
import DnSDetailView from '@/views/DnSDetailView.vue'
import ChartView from '@/views/ChartView.vue'
import { useArticleStore } from '@/stores/article'

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
      path: '/user/:user_pk',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (to.params.user_pk != store.userId) {
          return { name: 'home'}
        }
      }
    },
    {
      path: '/userupdate/:user_pk',
      name: 'userupdate',
      component: UserUpdateView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        // console.log(to.params)
        // console.log(store.userId)
        if (to.params.user_pk != store.userId) {
          return { name: 'home'}
        }
      }
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
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/testmap',
      name: 'testmap',
      component: TestMap
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/savings',
      name: 'savings',
      component: SavingsView
    },
    {
      path: '/dnsdetail/:dns_pk',
      name: 'dnsdetail',
      component: DnSDetailView
    },
    {
      path: '/articleupdate/:article_pk',
      name: 'articleupdate',
      component: ArticleUpdateView
    },
    {
      path: '/chart',
      name: 'chart',
      component: ChartView
    },
  ]
})

export default router
