<template>
  <div class="user-profile">
    <a-avatar :size="200" src="https://www.antdv.com/assets/logo.1ef800a8.svg" />
    <div class="content">
      <div class="text">
        姓名：
      </div>
      <div class="content-input">
        <a-input v-model:value="user_info.username" placeholder="请输入姓名">
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
        <a-input v-model:value="user_info.nickname">
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
        <a-input v-model:value="user_info.email">
    </a-input>
      </div>
    </div>

    <a-button class="save-button" type="primary" @click="updateUserInfo()">保存</a-button>

  </div>
</template>

<script setup>
import Navbar from './Navbar.vue';
import { ref, onMounted } from 'vue';
import TodoService from "../service";
import EventBus from '../eventbus';
import { message } from 'ant-design-vue';

import {
    UserOutlined,
} from '@ant-design/icons-vue';

const user_info = ref([]);

const fetchUserInfo = () => {
  TodoService.getUserInfo()
    .then((response) => {
      console.log(response.data);
      const data = response.data;
      user_info.value = data;
    })
    .catch((error) => {
      console.error("获取用户信息失败:", error);
    });
};

const updateUserInfo = () => {
  console.log("uuu", user_info.value);
  TodoService.updateUserInfo(user_info.value)
    .then((response) => {
      message.success('更新成功！');
      fetchUserInfo();
    })
    .catch((error) => {
      console.error("更新用户信息失败:", error);
    });
};

onMounted(() => {
  fetchUserInfo();
  EventBus.on('update-user-info', fetchUserInfo);
});

</script>

<style scoped>
.save-button {
  margin-top: 30px;
  background-color: green;
  margin-left: 60px;
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
  margin-top: 80px;
}

</style>
