import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  // const count = ref(0)
  // const doubleCount = computed(() => count.value * 2)
  // function increment() {
  //   count.value++
  // }

  const articles = ref([]);
  const API_URL = 'http://127.0.0.1:8000';
  const token = ref(null);
  const router = useRouter();

  const getArticles = () => {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
    })
      .then((res) => {
        articles.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      })
  }

  const createArticle = ({ title, content }) => {
    axios({
      method: 'post',
      url: `${API_URL}/articles/`,
      data: {
        title,
        content,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      // router.push({ name: 'home' });
    })
  }

  const signup = (payload) => {
    const { username, password1, password2 } = payload;

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        const password = password1;
        login({ username, password });
        console.log(res);
        // router.push({ name: 'home' });
      })
      .catch((err) => {
        console.log(err);
      })
  };

  const login = (payload) => {
    const { username, password } = payload;
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key;
        console.log(res);
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err);
      })
  };


  const isLogin = computed(() => {
    if(token.value === null) {
      return false;
    } else {
      return true;
    }
  });


  return { articles, getArticles, createArticle, API_URL, signup, login, token, isLogin }
}, { persist: true })
