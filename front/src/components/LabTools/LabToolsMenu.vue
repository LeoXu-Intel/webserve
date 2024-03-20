  <template>
    <el-row class="tac">
      <el-col >
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
        >
          <el-sub-menu index="1">
            <template #title>
              <el-icon><location /></el-icon>
              <span>Test1</span>
            </template>
              <el-menu-item index="1-1">Test1-1</el-menu-item>
              <el-menu-item index="1-2">Test1-2</el-menu-item>
              <el-menu-item index="1-3">Test1-3</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <el-icon><location /></el-icon>
              <span>Test2</span>
            </template>
            <el-menu-item index="2-1">
              <router-link to="/LabTools/Sensor/JenkinsAPI_N">Jenkins API-1</router-link>
            </el-menu-item>
            <el-menu-item index="2-2">
              <router-link to="/LabTools/Sensor/JenkinsAPI_P">Jenkins API-2</router-link>
            </el-menu-item>
            <el-menu-item index="2-3">
              <router-link to="/LabTools/Sensor/Compare">Test2-3</router-link>
            </el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="3">
            <template #title>
              <el-icon><location /></el-icon>
              <span>Test3</span>
            </template>
            <el-menu-item index="3-1">
              <router-link to="/LabTools/ASIC/Reference">Test3-1</router-link>
            </el-menu-item>
            <el-menu-item index="3-2">
              <router-link to="/LabTools/ASIC/login">Test3-2 </router-link>
            </el-menu-item>
            <el-menu-item index="3-3">
              <router-link to="/LabTools/ASIC/MasterExcel">Test3-3</router-link>
            </el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-col>
    </el-row>
  </template>
  
  <script lang="ts" setup>
  import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
  } from '@element-plus/icons-vue'

  </script>
  
