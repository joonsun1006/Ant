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
  </div>
  <button @click="addOrDelete">추가 제거</button>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article'
const store = useArticleStore()
const route = useRoute()
const DnS = ref({})
const addOrDelete = function () {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/finance/dnsaddordelete/${store.userId}/${route.params.dns_pk}/`
  })
  .then((res) => {
    console.log(res)
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
})
</script>
<style scoped>
#container {
  margin-top: 60px;
}

.table th,
.table td {
  border: none;
}

.table th {
  width: 30%;
}

</style>