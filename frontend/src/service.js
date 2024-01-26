import axios from 'axios';

const apiBaseUrl = '/api/todos';
const loginBaseUrl = '/api';

axios.defaults.withCredentials = true;

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
  },

  checkLoginStatus() {
    return axios.get(`${loginBaseUrl}/check-login-status`);
  },

  signOut() {
    return axios.post(`${loginBaseUrl}/sign-out`);
  }
};
