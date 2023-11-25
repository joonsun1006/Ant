<template>
    <dialog @click="closeModal">
        <p><strong>비밀번호 변경</strong><input type="text" v-model="new_password1"></p>
        <p><strong>비밀번호 확인</strong><input type="text" v-model="new_password2"></p>
        <button @click="passwordchange" >변경하기</button>
        <button @click="close">취소</button>
    </dialog>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore();
const new_password1 = ref(null)
const new_password2 = ref(null)



const passwordchange = () => {

  if (new_password1.value != new_password2.value) {
    alert("비밀번호가 일치하지 않습니다!");
  } else if (new_password1.value == null || new_password2.value == null) {
    alert("비밀번호를 입력해 주세요!")
  } else if (new_password1.value.length < 8) {
    alert("비밀번호를 8자 이상 입력해 주세요!")
  } else {
    const payload = {
      new_password1: new_password1.value,
      new_password2: new_password2.value,
    };

    store.passwordchange(payload);
    const dialog = document.querySelector("#open");
    dialog.close();
    alert("비밀번호가 변경 되었습니다.");
    new_password1.value = "";
    new_password2.value = "";
  }
};

const close = () => {
    const dialog = document.querySelector("#open");
                dialog.close();
}

const closeModal = (e) => {
  if (e.target.nodeName === "DIALOG") {
    document.querySelector('dialog').close();
  }
};

</script>

<style  scoped>

</style>