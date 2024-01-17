import { createRouter, createWebHashHistory } from 'vue-router';

import Navbar from '../components/Navbar.vue';
import Auth from '../views/Auth.vue';

const routes = [
  {
    path: '/',
    redirect: '/login', 
  },
  {
    path: '/home',
    name: 'Home',
    component: Navbar,
  },
  {
    path: '/login',
    name: 'Login',
    component: Auth,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;