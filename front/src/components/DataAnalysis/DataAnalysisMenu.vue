<template>
    <el-row class="tac">
      <el-col >
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
        >
            <el-menu-item index="1">
                FA KPI
            </el-menu-item>
            <el-menu-item index="2">
                Weekly Teamboard
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
  