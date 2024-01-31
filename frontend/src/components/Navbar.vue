<template>
  <div class="wrapper">
    <div class="sidebar">
      <h2>TODO</h2>
      <ul>
        <li @click="store.commit('jumpTodoList')">计划列表</li>
        <li @click="store.commit('jumpUserCenter')">个人中心</li>
      </ul>
    </div>
    <div class="main_content">
      <div class="header">
        <DropDown :user="userInfo" />
      </div>

      <div class="main">
        <div class="laout">
          <div class="button-icon">
            <div class="icon-bank-out">
              <AppstoreOutlined @click="toggleFetchTodos()" />
            </div>
          </div>
          <div class="button-icon">
            <div class="icon-check-circle">
              <CheckCircleOutlined @click="toggleGetTodosWithStatus()" />
            </div>
          </div>
          <div class="spacer"></div>

          <div class="button-icon">
            <div class="icon-plus-circle">
              <PlusCircleOutlined @click="store.commit('toggleAddTodoPopup')" />
            </div>
          </div>
        </div>
        <AddTodoPopup v-if="add_todo_popup" />
        <TodoList v-if="whither=='todo-list'"/>
        <UserCenter v-if="whither=='user-center'"/>
      </div>
    </div>
  </div>
</template>
<script lang="js" setup>
import { computed } from "vue";
import { useStore } from 'vuex'
import {
    ArrowRightOutlined,
    CheckCircleOutlined,
    PlusCircleOutlined,
    AppstoreOutlined

} from '@ant-design/icons-vue';


import TodoService from '../service';
import TodoList from './TodoList.vue';
import UserCenter from './UserCenter.vue';
import AddTodoPopup from './AddTodoPopup.vue';
import DropDown from "./dropDown.vue";
import EventBus from '../eventbus';


const store = useStore();
const toggleGetTodosWithStatus = () => {
    EventBus.emit('fillter-todolist');
};

const toggleFetchTodos = () => {
     EventBus.emit('update-todolist');
};

const add_todo_popup = computed(() => store.state.add_todo_popup);
const whither = computed(() => store.state.whither);

const userInfo = {
  name: 'root',
  age: 30
};
</script>
<style scoped>
a {
  text-decoration: none;
}

.wrapper {
  display: flex;
}

.wrapper .sidebar {
  width: 15%;
  min-height: 100vh;
  background-color: #4b4276;
}

.wrapper .sidebar h2 {
  color: #fff;
  text-transform: uppercase;
  text-align: center;
  margin-bottom: 30px;
}

.wrapper .sidebar ul li {
  color: #fff;
  padding: 15px;
  border-bottom: 1px solid #bdb8d7;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  cursor: pointer;
  text-decoration: none;
  list-style: none;
}

.wrapper .sidebar ul li:hover {
  background-color: #594f8d;
}

.wrapper .sidebar ul li a {
  color: #fff;
  display: block;
}

.wrapper .sidebar ul li:hover a {
  color: #fff;
}

.wrapper .sidebar ul li a .fas {
  width: 25px;
}

.wrapper .main_content {
  flex-grow: 1;
  background: #fafafa;
}

.wrapper .main_content .main {
  margin: 25px 24px 24px 24px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.wrapper .main_content .header {
  height: 50px;
  font-size: 30px;
  color: #535050;
  background-color: #4b4276;
}

.wrapper .main_content .main .laout {
  display: flex;
  flex-direction: row;
  margin-bottom: 10px;
  justify-content: space-between;
  align-items: center;
  margin-left: 10px;
}

.icon-check-circle {
  color: green;
  cursor: pointer;
}

.icon-bank-out {
  color: #9652ff;
  cursor: pointer;
}

.icon-plus-circle {
  color: rgb(0, 119, 255);
  margin-right: 20px;
}

.button-icon {
  display: flex;
  font-size: 24px;
  justify-content: center;
  margin: 6px 8px;
}

.spacer {
  flex-grow: 1;
}
</style>
