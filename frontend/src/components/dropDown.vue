<template>
<div class="drop-down">
  <a-dropdown :arrow="true">
    <a class="ant-dropdown-link" @click.prevent>
      {{ user.name }}
      <DownOutlined />
    </a>
    <template #overlay>
      <a-menu @click="onClick">
        <a-menu-item key="out">
          <a href="javascript:;">退出登陆</a>
        </a-menu-item>
      </a-menu>
    </template>
  </a-dropdown>
  </div>
</template>
<script lang="js" setup>
import DownOutlined from '@ant-design/icons-vue';
import { defineProps } from 'vue';
import TodoService from "../service";
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
  user: Object
});

const onClick = ({key}) => {
  if (key === "out") {
    TodoService.signOut()
      .then(() => {
       router.push('/login');
      })
      .catch((error) => {
        console.error("退出登陆失败:", error);
      });
  }
};
</script>

<style scoped>

.drop-down {
    color: #fff;
    display: flex;
    justify-content: flex-end;
    font-size: 14px;
    padding: 15px 50px;
}

</style>