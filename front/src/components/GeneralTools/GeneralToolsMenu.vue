<template>
    <el-row class="tac">
      <el-col >
        <el-menu
          default-active="0"
          class="el-menu-vertical-demo"
        >
            <el-menu-item index="1">
                Test1
            </el-menu-item>
            <el-menu-item index="2">
                Test2
            </el-menu-item>
            <el-menu-item index="3">
              Test3
            </el-menu-item>


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
  