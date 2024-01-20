<template>
    <div class="wrapper">
        <div class="sidebar">
            <h2>TODO</h2>
            <ul>
                <li>计划列表</li>
                <li>个人中心</li>
            </ul>
        </div>
        <div class="main_content">
            <div class="header">
            </div>

            <div class="main">
                <div class="laout">
                    <button type="button">
                        <div class="v-btn__content">
                            all
                        </div>
                    </button>
                    <button type="button">
                        <div class="v-btn__content">
                            complete
                        </div>
                    </button>
                    <button @click="store.commit('toggleAddTodoPopup')">
                        <div class="v-btn__content">
                            add
                        </div>
                    </button>


                </div>  
                <AddTodoPopup v-if="add_todo_popup"/>

                <TodoList v-if="!add_todo_popup"/>
            </div>

        </div>
    </div>
</template>
<script lang="js" setup>
import { computed } from "vue";
import { useStore } from 'vuex'
import {
    ArrowRightOutlined
} from '@ant-design/icons-vue';


import TodoService from '../service';
import TodoList from './TodoList.vue';
import AddTodoPopup from './AddTodoPopup.vue';


const store = useStore()
const add_todo_popup = computed(() => store.state.add_todo_popup);

</script>
<style>
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
}

.wrapper .sidebar ul li:hover {
    background-color: #594f8d;
}


.wrapper .sidebar ul li a {
    color: #bdb8d7;
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
    margin: 50px 10px 10px 10px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: #fff;
}

.wrapper .main_content .header {
    padding: 41px;
    font-size: 30px;
    color: #535050;
}

.wrapper .main_content .main .laout {
    display: flex;
    flex-direction: row;
    margin-bottom: 10px; /* 为了增加一些间距，可根据需要调整 */
}
</style>
  