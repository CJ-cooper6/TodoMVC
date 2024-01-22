import axios from 'axios';

const apiBaseUrl = 'http://localhost:5000/api/todos';
const loginBaseUrl = 'http://localhost:5000/api';

export default {
  getTodos(pageSize, currentPage) {
    return axios.get(apiBaseUrl, {
      params: { 
        pageSize,
        currentPage,
      },
    });
  },

  addTodo(todo) {
    return axios.post(apiBaseUrl, todo);
  },

  updateTodo(todoId, data) {
    return axios.put(`${apiBaseUrl}/${todoId}`, data);
  },

  deleteTodo(todoId) {
    return axios.delete(`${apiBaseUrl}/${todoId}`);
  },

  changeTodoStatus(todoId, todoStatus) {
    return axios.post(`${apiBaseUrl}/${todoId}`,{
      todoStatus: todoStatus,
    });
  },

  loginSubmit(data) {
    return axios.post(`${loginBaseUrl}/login`, data);
  }
};
