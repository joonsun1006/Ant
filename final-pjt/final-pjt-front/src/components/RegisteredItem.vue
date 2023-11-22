<template>

    <div v-if="product.type === 1" @click="goDetail(register)">
      <p >●(정기예금){{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
    </div>
    <div v-if="product.type === 2" @click="goDetail(register)">
      <p >●(정기적금){{ product.kor_co_nm }} - {{ product.fin_prdt_nm }}</p>
    </div>

</template>

<script setup>
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article'
const props = defineProps({
  register: String
})
const product = ref('')
const router = useRouter()
const goDetail = function (product_pk) {
  router.push({name:'dnsdetail', params:{dns_pk:product_pk}})
}
onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/finance/detail/${props.register}/`
  })
    .then((res) => {
      product.value = res.data
    })
})

</script>

<style lang="scss" scoped></style>