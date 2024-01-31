import { createRouter, createWebHistory } from 'vue-router';

import Navbar from '../components/Navbar.vue';
import Auth from '../views/Auth.vue';
import TodoService from "../service";

const routes = [
  {
    path: '/',
    redirect: '/login', 
  },
  {
    path: '/home',
    name: 'Home',
    component: Navbar,
    meta: {
      requiresAuth: true // 表示该路由需要身份验证
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Auth,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 设置全局前置守卫
router.beforeEach(async (to, from, next) => {
  // 检查路由是否需要登录权限
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const stasus = await checkLogin()
    if (!stasus) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

const checkLogin = async () => {
  try {
    const response = await TodoService.checkLoginStatus();
    if (response.status === 200) {
      return true;
    } else {
      return false;
    }
  } catch (err) {
    console.log(err);
    return false;
  }
};


export default router;