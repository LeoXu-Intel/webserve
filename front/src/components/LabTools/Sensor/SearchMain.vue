<template>
    <el-row>
      <el-col :span="16">
        <el-space direction="vertical" justify="center" >
          <el-space :size="40">
            <el-card class="box-card" style="width: 18vw; height: 7vw;">
               <el-row justify="center">
                 <el-col :span="24">
                   <el-text tag="b" >Number 1</el-text>
                   <el-input
                     v-model="number1"
                     placeholder="Enter first number"
                       />
                </el-col>
               </el-row>
            </el-card>

            <el-card class="box-card" style="width: 18vw; height: 7vw;">
               <el-row justify="center">
                 <el-col :span="24">
                   <el-text tag="b" >Number 2</el-text>
                   <el-input
                     v-model="number2"
                     placeholder="Enter second number"
                       />
                </el-col>
               </el-row>
            </el-card>

            <el-button type="primary" @click="calculateSum">Calculate</el-button>

            <el-card class="box-card" style="width: 18vw; height: 7vw;">
               <el-row justify="center">
                 <el-col :span="24">
                   <el-text tag="b" >Result</el-text>
                   <el-input
                     v-model="result"
                     placeholder="Result will be displayed here"
                     disabled
                       />
                </el-col>
               </el-row>
            </el-card>
          </el-space>
        </el-space>
      </el-col>
    </el-row>   
</template>

<script >
import { ref,defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'Addition',
  data(){
    return{
      number1: '',
      number2: '',
      result: '',
    }
  },
  methods:{
    calculateSum(){
      axios.get("/api/test",{
        params:{
          number1: this.number1,
          number2: this.number2
        }
      }).then((response)=>{
        this.result = response.data.result;
      })
    },
  },
});
</script>

<style scoped>
.result  {
  margin-top: 5vh;
}

.bottom-left-container {
  position: fixed;
  bottom: 5%;
  left: 51%;
  margin: 16px; /* 可根据需要调整边距 */
}

.centered-card {
  text-align: center; /* 设置卡片中的文本居中 */
}

.centered-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%; /* 让内容占据整个卡片高度 */
}
</style>
