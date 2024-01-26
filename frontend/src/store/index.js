import { createStore } from 'vuex';

export default createStore({

  state: {
    add_todo_popup: false,
    isAuthenticated: false,
  },

  mutations: {
    toggleAddTodoPopup(state) {
        state.add_todo_popup = !state.add_todo_popup
        console.log(state.add_todo_popup)
      },
    
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
      },
  },

  actions: {
    checkAuthentication({ commit }) {
      // 在这里进行认证状态的检查，可以发送请求到后端验证用户的登录状态等
      const isAuthenticated = True; // 根据后端返回的数据设置认证状态
      commit('setAuthentication', isAuthenticated);
    }
  },
  getters: {
  
  },
});