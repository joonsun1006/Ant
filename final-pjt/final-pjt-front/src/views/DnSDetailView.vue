<template>
  <div class="container" id="container">
    <h1>금융 상품 상세 정보</h1>
    <div class="table-responsive mt-3">
      <table class="table table-borderless">
        <tbody>
          <tr>
            <th scope="row">공시제출월</th>
            <td>{{ DnS.dcls_month }}</td>
          </tr>
          <tr>
            <th scope="row">금융 회사명</th>
            <td>{{ DnS.kor_co_nm }}</td>
          </tr>
          <tr>
            <th scope="row">상품명</th>
            <td>{{ DnS.fin_prdt_nm }}</td>
          </tr>
          <tr>
            <th scope="row">금융상품 코드</th>
            <td>{{ DnS.fin_prdt_cd }}</td>
          </tr>
          <tr>
            <th scope="row">가입 제한</th>
            <td>{{ DnS.join_member }}</td>
          </tr>
          <tr>
            <th scope="row">가입 방법</th>
            <td>{{ DnS.join_way }}</td>
          </tr>
          <tr>
            <th scope="row">우대 조건</th>
            <td>{{ DnS.spcl_cnd }}</td>
          </tr>
          <tr>
            <th scope="row">기타 유의사항</th>
            <td>{{ DnS.etc_note }}</td>
          </tr>
          <tr>
            <th scope="row">저축 금리 유형</th>
            <td>{{ DnS.intr_rate_type_nm }}</td>
          </tr>
          <tr v-if="DnS.type === 1">
            <th scope="row">예적금 타입</th>
            <td>예금</td>
          </tr>
          <tr v-if="DnS.type === 2">
            <th scope="row">예적금 타입</th>
            <td>적금</td>
          </tr>
          <tr v-if="DnS.max_limit">
            <th scope="row">적금 최고 한도</th>
            <td>{{ DnS.max_limit }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <button @click="addOrDelete" class="add-remove-button">
      {{ buttonText }}
    </button>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article'
const store = useArticleStore()
const route = useRoute()
const router = useRouter()
const DnS = ref({})
const buttonText = ref('추가');
const user = ref(null)
const registered = ref(null)
const addOrDelete = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/finance/dnsaddordelete/${store.userId}/${route.params.dns_pk}/`
  })
    .then((res) => {

      if (buttonText.value === '추가') {
        buttonText.value = '제거';
        alert('추가되었습니다.');
        router.push({name: 'user', params: {user_pk : store.userId}}  )
      }
      else if (buttonText.value === '제거') {
        buttonText.value = '추가';
        alert('제거되었습니다.');
      }
    })
}
onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/finance/detail/${route.params.dns_pk}/`
  })
    .then((res) => {
      DnS.value = res.data
    })
  if (store.isLogin) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/detail/${store.userId}/`,
    })
      .then((res) => {
        user.value = res.data;
        if (res.data.financial_products === '') {
          registered.value = null
        }
        else {
          registered.value = res.data.financial_products.split(',')
        }
        if (registered.value.includes(String(DnS.value.id))) {
          buttonText.value = '제거';
        }
        else {
          buttonText.value = '추가';
        }
      })
  }
})
</script>
<style scoped>
#container {
  margin-top: 100px;
}

.table th,
.table td {
  border: none;
}

.table th {
  width: 30%;
}

.add-remove-button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.add-remove-button:hover {
  background-color: #45a049;
}
</style>