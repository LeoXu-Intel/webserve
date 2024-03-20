<template>_
  <el-row style="margin-top: 20px;">
    <el-col :span="24">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>Jenkins API Trigger with Parameters</span>
        </div>
        <el-form ref="form" :model="parameters" label-width="120px">
          <el-row :gutter="20">
            <!-- sut1_conf 参数 -->
            <el-col :span="12">
              <el-form-item label="SUT1 Host">
                <el-input v-model="parameters.sut1_conf_host"></el-input>
              </el-form-item>
              <el-form-item label="board_platform">
                <el-input v-model="parameters.sut1_conf_board_platform"></el-input>
              </el-form-item>
              <el-form-item label="cpu_type">
                <el-input v-model="parameters.sut1_conf_cpu_type"></el-input>
              </el-form-item>
              <el-form-item label="cpu_corecount">
                <el-input v-model="parameters.sut1_conf_cpu_corecount"></el-input>
              </el-form-item>
              <el-form-item label="kernel_type">
                <el-input v-model="parameters.sut1_conf_kernel_type"></el-input>
              </el-form-item>
              <el-form-item label="pf1">
                <el-input v-model="parameters.sut1_conf_pf1"></el-input>
              </el-form-item>
              <el-form-item label="pf2">
                <el-input v-model="parameters.sut1_conf_pf2"></el-input>
              </el-form-item>
              <el-form-item label="pf3">
                <el-input v-model="parameters.sut1_conf_pf3"></el-input>
              </el-form-item>
              <el-form-item label="pf4">
                <el-input v-model="parameters.sut1_conf_pf4"></el-input>
              </el-form-item>
              <!-- 添加其他 sut1_conf 参数的表单项 -->
              <!-- ... -->
            </el-col>
            <el-col :span="12">
              <!-- sut2_conf 参数 -->
              <el-form-item label="SUT2 Host">
                <el-input v-model="parameters.sut2_conf_host"></el-input>
              </el-form-item>
              <el-form-item label="pf1">
                <el-input v-model="parameters.sut2_conf_pf1"></el-input>
              </el-form-item>
              <el-form-item label="pf2">
                <el-input v-model="parameters.sut2_conf_pf2"></el-input>
              </el-form-item>
              <el-form-item label="pf3">
                <el-input v-model="parameters.sut2_conf_pf3"></el-input>
              </el-form-item>
              <el-form-item label="pf4">
                <el-input v-model="parameters.sut2_conf_pf4"></el-input>
              </el-form-item>
              <!-- 添加其他 sut2_conf 参数的表单项 -->
              <!-- ... -->
            </el-col>
          </el-row>
          



        </el-form>
        
      </el-card>

      <el-row type="flex" justify="center" style="margin-top: 30px;">
          <el-button type="primary" @click="triggerJenkins">Submit</el-button>
        </el-row>
    </el-col>
  </el-row>
</template>

<script>
import { defineComponent, reactive } from 'vue';
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default defineComponent({
  setup() {
    const parameters = reactive({
        sut1_conf_host: "10.239.183.93",
        sut1_conf_board_platform: "Archer_City",
        sut1_conf_cpu_type: "SPR-SP",
        sut1_conf_cpu_corecount: "XCC",
        sut1_conf_kernel_type: "RT",
        sut1_conf_pf1: "ens787f2",
        sut1_conf_pf2: "-1",
        sut1_conf_pf3: "-1",
        sut1_conf_pf4: "-1",
       
        sut2_conf_host: "10.239.182.253",
        sut2_conf_pf1: "ens788f2",
        sut2_conf_pf2: "-1",
        sut2_conf_pf3: "-1",
        sut2_conf_pf4: "-1",
      // 初始化其他配置对象...
    });

const jenkinsParameters = {
  parameter: Object.keys(parameters).map(key => ({
    name: key,
    value: parameters[key],
  })),
};

    const triggerJenkins = () => {
      axios.post("/test_P", parameters)
        .then((response) => {
          // 处理响应
          ElMessage.success('Jenkins build triggered successfully!');
        })
        .catch((error) => {
          // 处理错误
          ElMessage.error(`Error: ${error.message}`);
        });
    };

    return {
      parameters,
      triggerJenkins,
    };
  },
});
</script>

<style scoped>
/* 你的样式 */
.box-card {
  transition: 0.3s;
  cursor: pointer;
  text-align: center;
}
.box-card:hover {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}
</style>
