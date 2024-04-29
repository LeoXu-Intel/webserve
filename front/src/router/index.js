import { createRouter, createWebHistory } from "vue-router";
import Login from '../components/Login.vue'; // 导入登录组件

import Container from "../components/Container.vue";
import LoadingView from "../components/Loading.vue";
import History from "../components/History/History.vue";

import Aotu_Config from "../components/LabTools/Sensor/Aotu_Config.vue";
import Test_Case_Overview from "../components/LabTools/Sensor/Test_Case_Overview.vue";
import Env_Config from "../components/LabTools/Sensor/Env_Config.vue";

// 定义路由数组
const routes = [
  { path: '/', redirect: '/login' }, // 将根路径重定向到登录
  { path: '/login', component: Login }, // 添加登录路由

  // LabTools
  {
    path: "/LabTools",
    component: Container,
    children: [
      // Sensor 相关路由
      {
        path: "Sensor/Env_Config",
        component: Env_Config, // 注意这里不是 components
      },
      {
        path: "Sensor/Test_Case_Overview",
        component: Test_Case_Overview, // 注意这里不是 components
      },
      {
        path: "Sensor/Aotu_Config",
        component: Aotu_Config, // 注意这里不是 components
      },
    ],
    meta: { requiresAuth: true }, // 添加元数据标记需要认证
  },
  // 历史记录路由
  {
    path: "/History",
    component: History,
    meta: { requiresAuth: true }, // 假设历史记录页也需要认证
  },
  // Loading 视图路由（如果需要的话）
  {
    path: "/loading",
    component: LoadingView,
  },
  // 其他路由...
];

// 创建路由器实例
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// 全局前置守卫
router.beforeEach((to, from, next) => {
  // 检查路由是否需要认证
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 如果用户未登录，则重定向到登录页面
    if (!isLoggedIn()) {
      next('/login');
    } else {
      next(); // 如果已登录，继续导航
    }
  } else {
    next(); // 对于不需要认证的路由，直接放行
  }
});

// 检查用户是否已登录的函数
function isLoggedIn() {
  // 这里的逻辑可能需要根据实际的登录逻辑进行调整
  return localStorage.getItem('isUserLoggedIn') === 'true';
}

// 导出路由器实例
export default router;
