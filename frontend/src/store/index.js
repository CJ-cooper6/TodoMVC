import { createStore } from 'vuex';

export default createStore({

  state: {
    add_todo_popup: false,
    isAuthenticated: false,
    whither: "todo-list",
  },

  mutations: {
    toggleAddTodoPopup(state) {
        state.add_todo_popup = !state.add_todo_popup
      },
    
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
      },

    jumpTodoList(state) {
      state.whither = "todo-list";
    },

    jumpUserCenter(state) {
      state.whither = "user-center";
    }
  },

  actions: {

  },
  getters: {
  
  },
});