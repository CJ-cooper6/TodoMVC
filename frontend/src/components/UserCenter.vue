<template>
  <div class="user-profile">
    <a-avatar :size="200" src="https://www.antdv.com/assets/logo.1ef800a8.svg" />
    <div class="content">
      <div class="text">
        姓名：
      </div>
      <div class="content-input">
        <a-input v-model:value="name" placeholder="请输入姓名">
      <template #prefix>
        <user-outlined />
      </template>
    </a-input>
      </div>
    </div>
    <div class="content">
      <div class="text">
        昵称：
      </div>
      <div class="content-input">
        <a-input v-model:value="name">
      <template #prefix>
        <user-outlined />
      </template>
    </a-input>
      </div>
    </div>
    <div class="content">
      <div class="text">
        电话：
      </div>
      <div class="content-input">
        <a-input v-model:value="name">
      <template #prefix>
        <user-outlined />
      </template>
    </a-input>
      </div>
    </div>
    <div class="content">
      <div class="text">
        邮箱：
      </div>
      <div class="content-input">
        <a-input v-model:value="name">
      <template #prefix>
        <user-outlined />
      </template>
    </a-input>
      </div>
    </div>

    <a-button class="save-button" type="primary">保存</a-button>

  </div>
</template>

<script setup>
import Navbar from './Navbar.vue';
import { ref } from 'vue';

import {
    UserOutlined,
} from '@ant-design/icons-vue';

const user_info = ref([]);
const name = ref("aa");

</script>

<style scoped>
.save-button {
  margin-top: 30px;
  background-color: green;
}

.content {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.content .text {
  width: 50px;
}

.user-profile {
  max-width: 800px;
  margin: auto;
}

</style>
