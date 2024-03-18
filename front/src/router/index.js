import { createRouter, createWebHistory } from "vue-router";
import store from "../store";
import Container from "../components/Container.vue";
import LoadingView from "../components/Loading.vue";

// import CompareView from '../views/CompareView.vue'
import CompareMain from "../components/LabTools/Sensor/CompareMain.vue";
import SearchMain from "../components/LabTools/Sensor/SearchMain.vue";
//import SearchMainUpdate from "../components/LabTools/Sensor/SearchMainUpdate.vue";
//import SensorLogin from "@/components/LabTools/Sensor/Login.vue";

import LabToolsMenu from "../components/LabTools/LabToolsMenu.vue";

//import ReportReferenceMain from "@/components/LabTools/ASIC/ReportReferenceMain.vue";
import ReportReferenceMainUpdate from "@/components/LabTools/ASIC/ReportReferenceMainUpdate.vue";
import MasterExcelMain from "@/components/LabTools/ASIC/MasterExcelMain.vue";
import ASICLogin from "@/components/LabTools/ASIC/Login.vue";

import ManagementMenu from "../components/ManagementSystem/ManagementSystemMenu.vue";
import SensorFA from "@/components/ManagementSystem/Bussiness/SensorFA.vue";
import APTeamboard from "@/components/ManagementSystem/Bussiness/APTeamboard.vue";
import SensorTeamboard from "@/components/ManagementSystem/Bussiness/SensorTeamboard.vue";
import SectionTeamboard from "@/components/ManagementSystem/Bussiness/SectionTeamboard.vue";
import ICFA from "@/components/ManagementSystem/Bussiness/ICFA.vue";

//import CapacityAssessmentMain from "@/components/ManagementSystem/Capacity/AssessmentMain.vue";
import DoucumentsMenu from "../components/Documents/DocumentsMenu.vue";
import TrainingDocument from "@/components/ManagementSystem/Documents/Training.vue";
//import WI from "@/components/ManagementSystem/Equipment/WI.vue";
//import TPM from "@/components/ManagementSystem/Equipment/TPM.vue";

import EnrolmentandChecking from "@/components/ManagementSystem/Purchase/EnrolmentandChecking.vue";

import DataAnalysisMenu from "../components/DataAnalysis/DataAnalysisMenu.vue";

import GeneralToolsMenu from "../components/GeneralTools/GeneralToolsMenu.vue";

import Home from "../components/Home.vue";
import Dashboard from "../components/Dashboard.vue";
import Login from "../components/Login.vue";

const routes = [
  { path: "/", redirect: "/LabTools" },
  { path: "/home", component: Home },
  { path: "/login", component: Login },
  { path: "/dashboard", component: Dashboard, meta: { requiresAuth: true } },

  { path: "/", component: LoadingView },
  // LabTools
  {
    path: "/LabTools",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: LabToolsMenu,
          main: LoadingView,
        },
      },
      {
        path: "Slice",
        components: {
          menu: LabToolsMenu,
          main: SearchMain,
        },
      },
      {
        path: "Sensor/Search",
        components: {
          menu: LabToolsMenu,
          main: SearchMain,
        },
      },
      {
        path: "Sensor/UpdateSearch",
        components: {
          menu: LabToolsMenu,
          //main: SearchMainUpdate,
        },
      },
      {
        path: "Sensor/login",
        components: {
          menu: LabToolsMenu,
          //main: SensorLogin,
        },
      },
      {
        path: "Sensor/Compare",
        components: {
          menu: LabToolsMenu,
          main: CompareMain,
        },
      },
      {
        path: "ASIC/Reference",
        components: {
          menu: LabToolsMenu,
          //main: ReportReferenceMain,
        },
      },
      {
        path: "ASIC/UpdateReference",
        components: {
          menu: LabToolsMenu,
          main: ReportReferenceMainUpdate,
          meta: { requiresAuth: true },
        },
      },
      {
        path: "ASIC/login",
        components: {
          menu: LabToolsMenu,
          main: ASICLogin,
        },
      },
      {
        path: "ASIC/MasterExcel",
        components: {
          menu: LabToolsMenu,
          main: MasterExcelMain,
        },
      },
    ],
  },
  // ManagementSystem
  {
    path: "/ManagementSystem",
    // name: 'Compare',
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: ManagementMenu,
          main: LoadingView,
        },
      },
      {
        path: "Capacity/Assessment",
        components: {
          menu: ManagementMenu,
          //main: CapacityAssessmentMain,
        },
      },
    ],
  },
  // Bussiness
  {
    path: "/ManagementSystem",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: ManagementMenu,
          main: LoadingView,
        },
      },
      {
        path: "Bussiness/ICFA",
        components: {
          menu: ManagementMenu,
          main: ICFA,
        },
      },
      {
        path: "Bussiness/SensorFA",
        components: {
          menu: ManagementMenu,
          main: SensorFA,
        },
      },
      {
        path: "Bussiness/APTeamboard",
        components: {
          menu: ManagementMenu,
          main: APTeamboard,
        },
      },
      {
        path: "Bussiness/SensorTeamboard",
        components: {
          menu: ManagementMenu,
          main: SensorTeamboard,
        },
      },
      {
        path: "Bussiness/SectionTeamboard",
        components: {
          menu: ManagementMenu,
          main: SectionTeamboard,
        },
      },
    ],
  },
  // Documents
  {
    path: "/ManagementSystem",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: ManagementMenu,
          main: LoadingView,
        },
      },
      {
        path: "Documents/Training",
        components: {
          menu: ManagementMenu,
          main: TrainingDocument,
        },
      },
    ],
  },
  // Equipment
  {
    path: "/ManagementSystem",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: ManagementMenu,
          main: LoadingView,
        },
      },
      {
        path: "Equipment/WI",
        components: {
          menu: ManagementMenu,
          //main: WI,
        },
      },
      {
        path: "Equipment/TPM",
        components: {
          menu: ManagementMenu,
          //main: TPM,
        },
      },
    ],
  },
  // Purchase
  {
    path: "/ManagementSystem",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: ManagementMenu,
          main: LoadingView,
        },
      },
      {
        path: "Purchase/EnrolmentandChecking",
        components: {
          menu: ManagementMenu,
          main: EnrolmentandChecking,
        },
      },
    ],
  },
  // DataAnalysis
  {
    path: "/DataAnalysis",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: DataAnalysisMenu,
          main: LoadingView,
        },
      },
    ],
  },
  // GeneralTools
  {
    path: "/GeneralTools",
    component: Container,
    children: [
      {
        path: "",
        components: {
          menu: GeneralToolsMenu,
          main: LoadingView,
        },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
// 导航守卫
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // 判断是否登录，这里假设有一个名为 isAuthenticated 的状态
    if (!store.state.isAuthenticated) {
      next({
        path: "/login",
        query: { redirect: to.fullPath }, // 把要跳转的路由path作为参数，登录成功后跳转到该路由
      });
    } else {
      next();
    }
  } else {
    next();
  }
});
export default router;
