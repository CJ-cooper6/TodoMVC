

import { createApp } from 'vue'
import Antd from 'ant-design-vue';
import App from './App.vue'
import router from './router';
import store from './store';

const app = createApp(App);
app.use(router);
app.use(Antd);
app.use(store);
app.mount('#app');

