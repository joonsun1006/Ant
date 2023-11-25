<template>
  <div id="container">
    <h1 class="mb-5 comment"><strong>개미의 안식처</strong></h1>
    <p class="comment pcomment">주식에 물린 개미들을 위해</p>
    <p class="comment pcomment">환율 계산기, 게시판, 지도, 예적금 상품(추천)</p>
    <p class="comment pcomment">서비스를 제공하고 있는 공간입니다</p>
    <div id="carousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="../assets/ca1.png" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="../assets/ca2.png" class="d-block w-100" alt="...">
        </div>
      <div class="carousel-item">
        <img src="../assets/ca3.png" class="d-block w-100" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</div>
  
</template>

<script setup>

</script>

<style scoped>

#container {
  padding-top: 60px;
  background-color: white;
}

.comment {
  margin-left: 120px;
  margin-bottom: 60px;

}

.pcomment {
  font-size: 18px;
}

#carousel {
  margin-bottom: 0;
}
</style>
