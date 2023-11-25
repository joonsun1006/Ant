import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {

  const router = useRouter();
  const API_URL = 'http://127.0.0.1:8000';
  const articles = ref([])
  const token = ref(null)
  const userId = ref(null)

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
      router.push({ name: 'articles' });
    })
  }

  const signup = (payload) => {
    const { username,email, password1, password2,
      nickname, age, money,
      salary
    } = payload;

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, email, password1, password2,
        nickname, age, money,
        salary,
      }
    })
      .then((res) => {
        const password = password1;
        login({ username, password });
        // router.push({ name: 'home' });
      })
      .catch((err) => {
        alert('필수 정보를 입력해주세요!');
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
        axios({
          method:'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
        .then((res2) => {
          userId.value = res2.data.pk
          router.push({ name: 'home' })
        })
      })
      .catch((err) => {
        alert('잘못된 입력입니다!');
      })
  };


  const isLogin = computed(() => {
    if(userId.value === null) {
      return false;
    } else {
      return true;
    }
  });

  const logout = () => {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        userId.value = null
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const passwordchange = (payload) => {
    const {new_password1, new_password2} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      data: {
        new_password1, new_password2,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res.data)
      })
      .catch((err) => {
        console.log(new_password1, new_password2)
        console.log(err)
      })
  }
  

  return {
    articles, getArticles, createArticle,
    API_URL, signup, login,
    token, isLogin, logout, userId, passwordchange

  }
}, { persist: true })
