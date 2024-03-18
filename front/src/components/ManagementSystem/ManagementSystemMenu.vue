<template>
  <el-row class="tac">
    <el-col >
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo">
        <el-sub-menu index=1>
          <template #title>
            <el-icon><location /></el-icon>
            <span>Test1</span>
          </template>
          <el-menu-item index="1-1">Test1-1</el-menu-item>
          <el-menu-item index="1-2">Test1-2</el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="2">
          <template #title>
            <el-icon><location /></el-icon>
            <span>Test2</span>
          </template>
  
          <!-- 使用 el-sub-menu 替代 el-menu -->
          <el-sub-menu index="2-1">
            <template #title>Test2-1</template>
            <el-menu-item index="2-1-1" style="text-align: center;">
              <router-link to="/ManagementSystem/Equipment/WI">2-1-1</router-link>
            </el-menu-item>
            <el-menu-item index="2-1-2">
              <router-link to="/ManagementSystem/Equipment/TPM">2-1-2</router-link>
            </el-menu-item>
          </el-sub-menu>

        <el-menu-item index="2-2">Test2-2</el-menu-item>
        <el-menu-item index="2-3">Test2-3</el-menu-item>
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
  