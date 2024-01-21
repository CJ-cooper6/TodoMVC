<template>
    <div class="overlay">
        <div class="modal">
            <div class="header">
                <div>
                    添加 Todo
                </div>
            </div>
            <div class="content">
                <div class="edit-item">
                    <span class="icon-edit">
                        <EditOutlined />
                    </span>
                    <input v-model="newTodo" placeholder="Title" class="todo-input" />
                </div>
                <div class="button-container">
                    <button @click="addTodo" class="add-button">添加</button>
                    <button @click="store.commit('toggleAddTodoPopup')" class="close-button">取消</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="js" setup>
import { ref } from 'vue';
import TodoService from '../service';
import { useStore } from 'vuex'
import {
    EditOutlined

} from '@ant-design/icons-vue';

const newTodo = ref('');
const store = useStore()

const addTodo = () => {
    if (newTodo.value) {
        TodoService.addTodo({ title: newTodo.value })
            .then(() => {
                newTodo.value = '';
                store.commit('toggleAddTodoPopup')
            })
            .catch(error => {
                console.error('增加todo失败:', error);
            });
    }
};

</script>

<style scoped>
.modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    width: 30%;
    height: 40%;
}

.header {
    display: flex;
    flex-wrap: wrap;
    padding: 5px;
    align-items: center;
    font-size: 21px;
    font-weight: 700;

}

.content {
    margin: 30px 10px 10px 10px;
}

.edit-item {
    display: flex;
}

.todo-input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-right: 8px;
    flex-grow: 1;
    font-size: 16px;
}

.add-button,
.close-button {
    padding: 8px;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin: 10px;
}

.add-button {
    background-color: #4caf50;
}

.close-button {
    background-color: rgb(241, 34, 34);

}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* 半透明黑色背景 */
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 999;
    /* 确保在最上层 */
}

.icon-edit {
    display: flex;
    font-size: 22px;
    margin: 6px 8px;
    color: rgba(0, 0, 0, .54);
}

.button-container {
    position: fixed;
    top: 80%;
    left: 39%;
    display: flex;
}
</style>
  