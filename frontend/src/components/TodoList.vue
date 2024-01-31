<template>
  <div class="todo-app">
    <ul class="todo-list">
      <li v-for="(todo, index) in todo_items" :key="todo.id" class="todo-item" :class="getTodoItemClass(todo.completed)">
        <div class="todo-title">{{ todo.title }}</div>
        <div class="todo-due-by">{{ todo.end_time }}</div>
        <button @click="changeTodoStatus(index)" :class="getButtonClass(todo.completed)">
          {{ getButtonText(todo.completed) }}
        </button>
        <div class="spacer"></div>
        <div class="todo-buttons">
          <button @click="editTodo(todo.id)" class="edit-button">编辑</button>
          <button @click="deleteTodo(todo.id)" class="delete-button">
            删除
          </button>
        </div>
      </li>
    </ul>

    <div class="pagination">
      <a-pagination v-model:current="pagination.currentPage" v-model:pageSize="pagination.pageSize" :total="total"
        :showSizeChanger="true" :pageSizeOptions="['5', '10', '20']" @change="fetchTodos()" />
    </div>
  </div>
</template>


<script lang="js" setup>
import { ref, reactive, computed, onMounted } from "vue";
import TodoService from "../service";
import EventBus from '../eventbus';

const todo_items = ref([]);
const total = ref(0);
const pagination = reactive({
  pageSize: 10, // 每页显示的数量
  currentPage: 1, // 当前页码
});

const totalPage = computed(() => Math.ceil(total.value / pagination.pageSize));

const changeTodoStatus = (index) => {
  const todoId = todo_items.value[index].id;
  const todoStatus = !todo_items.value[index].completed;
  TodoService.changeTodoStatus(todoId, todoStatus)
  .then(() => {
    todo_items.value[index].completed = !todo_items.value[index].completed;
  })
  .catch((error) => {
        console.error("更新状态失败:", error);
      });
};

const fetchTodos = () => {
  TodoService.getTodos(pagination.pageSize, pagination.currentPage)
    .then((response) => {
      const data = response.data;
      todo_items.value = data.todo_items;
      total.value = data.total;
    })
    .catch((error) => {
      console.error("获取失败:", error);
    });
};

const fetchTodosWithStatus = () => {
  TodoService.getTodosWithStatus(pagination.pageSize, pagination.currentPage, true)
    .then((response) => {
      const data = response.data;
      todo_items.value = data.todo_items;
      total.value = data.total;
    })
    .catch((error) => {
      console.error("获取失败:", error);
    });
};

const editTodo = (todoId) => {
  const newText = prompt("重新输入一个todo:");
  if (newText !== null) {
    TodoService.updateTodo(todoId, { title: newText })
      .then(() => {
        fetchTodos();
      })
      .catch((error) => {
        console.error("更新失败:", error);
      });
  }
};

const deleteTodo = (todoId) => {
  if (confirm("确定删除?")) {
    TodoService.deleteTodo(todoId)
      .then(() => {
        fetchTodos();
      })
      .catch((error) => {
        console.error("删除失败:", error);
      });
  }
};

const getButtonClass = (completed) => {
  return {
    "button-completed-true": completed === true,
    "button-completed-false": completed === false,
  };
};

const getTodoItemClass = (completed) => {
  return {
    "todo-item-true": completed === true,
    "todo-item-false": completed === false,
  };
};


const getButtonText = (completed) => {
  return completed === true ? "已完成" : "未完成";
};

const nextPage = () => {
  if (pagination.currentPage < totalPage.value) {
    pagination.currentPage++;
    fetchTodos();
  }
};

const prevPage = () => {
  if (pagination.currentPage > 1) {
    pagination.currentPage--;
    fetchTodos();
  }
};

onMounted(() => {
  fetchTodos();
  EventBus.on('update-todolist', fetchTodos);
  EventBus.on('fillter-todolist', fetchTodosWithStatus);
});

</script>

<style scoped>
.todo-app {
  font-family: "Arial", sans-serif;
  background-color: #fff;
  border-color: #fff;
  color: rgba(0, 0, 0, 0.87);
}

.todo-app .todo-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.todo-app .todo-list .todo-item {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
  padding: 10px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 16px;
}

.todo-app .todo-list .todo-item .todo-title {
  width: 40%;
}

.todo-app .todo-list .todo-item .todo-due-by {
  width: 34%;
}

.todo-app .todo-list .todo-item .todo-status {
  font-size: 15px;
  font-weight: 550;
  width: 7%;
}

.todo-app .todo-list .todo-item .todo-buttons {
  width: 10%;
  display: flex;
  justify-content: space-between;
}

.spacer {
  flex-grow: 1;
}

.edit-button,
.delete-button {
  padding: 8px;
  background-color: #2196f3;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.button-completed-true,
.button-completed-false {
  width: 7%;
  font-size: 15px;
  font-weight: 550;
  height: 24px;
  border-radius: 15px;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: 0.5s cubic-bezier(0.42, 0, 0.58, 1);
}

.button-completed-true {
  background-color: #3cd1c2;
}

.button-completed-false {
  background-color: #ffaa2c;
}

.pagination {
  display: flex;
  justify-content: flex-end;
  padding-top: 10px;
  margin-top: 10px;
  background-color: #fafafa;
}

.todo-item-true {
  border-left: 4px solid #3cd1c2;
}

.todo-item-false {
  border-left: 4px solid #ffaa2c;
}
</style>