<template>
  <el-row style="margin-top: 20px;">
    <el-col :span="12" :offset="1">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>Jenkins API Trigger</span>
        </div>
        <el-row type="flex" justify="center" style="margin-top: 30px;">
          <el-button type="primary" @click="triggerJenkins">Trigger Jenkins Build</el-button>
        </el-row>
      </el-card>
    </el-col>
  </el-row>
</template>



<script>
import { defineComponent } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus'; // 确保你已经正确导入了 ElMessage

export default defineComponent({
  methods: {
    triggerJenkins() {
      axios.get("/test", {
        params: {
          // 你的参数（如果有的话）
        }
      }).then((response) => {
        this.result = response.data.result;
        if (this.result && this.result.result === 'SUCCESS') {
          // 如果构建成功，显示成功消息
          ElMessage({
            message: 'Jenkins build run successfully!',
            type: 'success',
          });
        } else {
          // 如果构建不成功，显示错误消息
          ElMessage({
            message: 'Jenkins build did not run successfully.',
            type: 'error',
          });
        }
      }).catch((error) => {
        // 如果请求失败，显示错误消息
        ElMessage({
          message: `Error: ${error.message}`,
          type: 'error',
        });
      });
    },
  },
});
</script>



<style scoped>
.box-card {
  transition: 0.3s;
  cursor: pointer;
  text-align: center;
}
.box-card:hover {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}
</style>
