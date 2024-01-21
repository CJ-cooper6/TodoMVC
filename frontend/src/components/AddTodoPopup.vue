<template>
    <div class="overlay">
        <div class="modal">
            <div class="header">
                <div>
                    添加Todo
                </div>
            </div>
            <div class="content">
                <input v-model="newTodo" placeholder="New Todo" class="todo-input" />
                <button @click="addTodo" class="add-button">添加</button>
                <button @click="store.commit('toggleAddTodoPopup')" class="add-button">取消</button>
            </div>
        </div>
    </div>
</template>

<script lang="js" setup>
import { ref } from 'vue';
import TodoService from '../service';
import { useStore } from 'vuex'

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

<style>
.todo-input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-right: 8px;
    flex-grow: 1;
}

.add-button {
    padding: 8px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer;
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

.header {
    display: flex;
    flex-wrap: wrap;
    padding: 16px;
    align-items: center;
}
</style>
  