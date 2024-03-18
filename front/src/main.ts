import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// import installElementPlus from './plugins/element'
import axios from 'axios'

axios.defaults.baseURL="http://10.239.183.54:8082"

const app = createApp(App)

app.config.globalProperties.$axios = axios
import global from './components/global.vue' // 引入全局变量
app.config.globalProperties.global = global // 注册全局变量



app.use(store).use(router).use(ElementPlus).mount('#app')

// 这段代码的作用是初始化Vue.js应用，配置应用的路由、状态管理、UI组件库，设置默认的HTTP请求基础URL，并将应用实例挂载到HTML文档中的#app元素上，从而启动应用。


