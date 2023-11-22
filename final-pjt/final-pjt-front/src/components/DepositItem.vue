<template>
  <tr @click="goDetail(deposit.id)" class="table-row">
    <td>{{ deposit.dcls_month }}</td>
    <td>{{ deposit.kor_co_nm }}</td>
    <td>{{ deposit.fin_prdt_nm }}</td>
    <td>{{ deposit.intr_rate_6 }}</td>
    <td>{{ deposit.intr_rate_12 }}</td>
    <td>{{ deposit.intr_rate_24 }}</td>
    <td>{{ deposit.intr_rate_36 }}</td>
  </tr>
</template>

<script setup>

import { useRouter } from 'vue-router';

const router = useRouter()
defineProps({
  deposit: Object
})
const goDetail = function (deposit_pk) {
  router.push({name:'dnsdetail', params:{dns_pk:deposit_pk}})
}
</script>

<style scoped>
.table-row:hover {
  background-color: black; /* 호버 효과 배경색 */
  cursor: pointer;
}

</style>