import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import axios from 'axios';

// 设置axios的默认基础URL
axios.defaults.baseURL = "http://10.239.183.54:8082";

// 创建Vue应用实例
const app = createApp(App);

// 将axios添加到全局属性中，这样在组件内可以通过this.$axios来使用
app.config.globalProperties.$axios = axios;

// 引入全局变量
import global from './components/global.vue';
// 注册全局变量
app.config.globalProperties.global = global;

// 使用Vuex、Vue Router和ElementPlus
app.use(store).use(router).use(ElementPlus);

// 挂载Vue应用实例到HTML文档中的#app元素上
app.mount('#app');
