<template>
  <tr @click="goDetail(saving.id)" class="table-row">
    <td>{{ saving.dcls_month }}</td>
    <td>{{ saving.kor_co_nm }}</td>
    <td>{{ saving.fin_prdt_nm }}</td>
    <td>{{ saving.intr_rate_6 }}</td>
    <td>{{ saving.intr_rate_12 }}</td>
    <td>{{ saving.intr_rate_24 }}</td>
    <td>{{ saving.intr_rate_36 }}</td>
  </tr>
</template>

<script setup>

import { useRouter } from 'vue-router';
defineProps({
  saving: Object
})
const router = useRouter()
const goDetail = function (saving_pk) {
  router.push({name:'dnsdetail', params:{dns_pk:saving_pk}})
}
</script>

<style scoped>
.table-row:hover {
  background-color: black; /* 호버 효과 배경색 */
  cursor: pointer;
}

</style>