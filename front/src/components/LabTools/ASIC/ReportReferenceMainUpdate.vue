<template>
    <el-row :gutter="10" justify="space-around" align="middle">
        
        
         <!-- 这个是针对的Category -->
         <el-col :span="4" align="center">
            <el-text tag="b" size="large">Category</el-text>
            <el-input
               v-model="category"
               aria-placeholder="Enter category"
            />
            <!-- <el-select  v-model="category" filterable placeholder="SELECT" @change="searchDeviceType"  @blur="handleBlur">
                <el-option
                    v-for="(item,index) in categoryList"
                    :key = "index"
                    :label = "item"
                    :value = "item"
                />
            </el-select> -->
        </el-col>
 
        <!-- 这个是针对的Device Type -->
        <el-col :span="4" align="center">
            <el-text tag="b" size="large">Device Type</el-text>
            <el-input
               v-model="deviceType"
               aria-placeholder="Enter deviceType"
            />
            <!-- <el-select v-model="deviceType" filterable placeholder="SELECT"  @change="searchFailureType">
                <el-option
                    v-for="(item,index) in deviceTypeList"
                    :key = "index"
                    :label = "item"
                    :value = "item"
                />
            </el-select> -->
        </el-col>

        <!-- 这个是针对的Failure Type -->
        <el-col :span="5" align="center">
            <el-text tag="b" size="large">Failure Type</el-text>
            <el-input
               v-model="failureType"
               aria-placeholder="Enter failureType"
            />
            <!-- <el-select v-model="failureType" filterable placeholder="SELECT" 
            @change="searchRiskLevelAndCode" style="width:300px"  placement="bottom">
                <el-option
                    v-for="(item,index) in failureTypeList"
                    :key = "index"
                    :label = "item"
                    :value = "item"
                />
            </el-select> -->
        </el-col>



        <!-- 这个是针对Risk Level -->
        <el-col :span="4" align="center">
            <el-text tag="b" size="large">Risk Level</el-text>
            <el-input
               v-model="riskLevel"
               aria-placeholder="Enter riskLevel"
            />
            <!-- <el-select v-model="riskLevel" filterable placeholder="SELECT" @change="searchReference">
                <el-option
                    v-for="(item,index) in riskLevelList"
                    :key = "index"
                    :label = "item"
                    :value = "item"
                />
            </el-select> -->
        </el-col>


    </el-row>


    <el-divider border-style="dashed" />
    
    <!-- 针对code -->
    <el-row :gutter="10" justify="space-evenly" align="middle">
        <el-col :span="6" align="center">
            <el-text tag="b" size="large">Code</el-text>
            <el-input v-model="code" :readonly="false" />
        </el-col>

    <!-- 针对Finding -->
    <el-col :span="12" align="center" >
        <el-text tag="b" size="large">Finding</el-text>
        <el-input 
            v-model="finding" 
            :readonly="false"
            size="large"
            :autosize="{ minRows: 2, maxRows: 4 }"
            type="textarea"
        />
        </el-col>
    </el-row>


    <el-divider border-style="dashed" />

    <!-- 针对Criteria -->
    <el-row justify="space-evenly" align="middle">
        <el-col :span="20" align="center" >
           <el-text tag="b" size="large">Criteria</el-text>
            <el-input 
                v-model="criteria" 
                :readonly="false"
                size="large"
                :autosize="{ minRows: 5, maxRows: 8 }"
                type="textarea"
            /> 
        </el-col>
    </el-row>

    <el-divider border-style="dashed" />


    <!-- 针对Assessment -->
    <el-row justify="space-evenly" align="middle">
        <el-col :span="20" align="center" >
           <el-text tag="b" size="large">Assessment</el-text>
            <el-input 
                v-model="assessment" 
                :readonly="false"
                size="large"
                :autosize="{ minRows: 5, maxRows: 8 }"
                type="textarea"
            /> 
        </el-col>

        <el-divider border-style="dashed" />
    
    <!-- 添加按钮     -->
    <el-row justify="end">
      <el-button @click="addNewContent" type="primary" >Add New Content</el-button>
      <el-button @click="deleteReference" type="danger">
      Delete Reference
    </el-button>
    </el-row>


    </el-row>
</template>




<script>


import {ref, defineComponent} from 'vue';
import axios, { formToJSON } from 'axios';
// import clipboard from 'clipboard.js-master'
import { ElNotification } from 'element-plus';
// import { th } from 'element-plus/es/locale';



export default defineComponent({
    name: 'ReportReferenceMain',

    data(){
        return {
            category: ref(''),
            deviceType:ref(''),
            failureType: ref(''),
            riskLevel: ref(''),
            code: ref(''),
            
            finding: ref(''),
            assessment: ref(''),
            criteria: ref(''),

            deviceTypeList:[],
            categoryList:[],
            failureTypeList:[],
            riskLevelList:[],
        }
    },

    methods:{
        addNewContent(){

            axios.get("/api/ASIC/Report/addNewContent",{
                params:{
                    category: this.category,
                    deviceType:this.deviceType,
                    failureType:this.failureType,
                    riskLevel:this.riskLevel,
                    code:this.code,
                    finding:this.finding,
                    criteria:this.criteria,
                    assessment:this.assessment

                }
            }).then((response)=>{
                const responseData = response.data;

                if (responseData.code === 0) {
                // 插入成功
                this.$message.success('添加成功');

                 // 清空数据属性
                this.category = '';
                this.deviceType = '';
                this.failureType = '';
                this.riskLevel = '';
                this.code = '';
                this.finding = '';
                this.criteria = '';
                this.assessment = '';
            } else {
              // 插入失败，根据实际情况处理错误
                 this.$message.error(`添加失败：${responseData.msg}`);
            }
            })
        },
        searchDeviceType(){
            axios.get("/api/ASIC/Report/getDeviceType",{
                params:{
                    category: this.category
                }
            }).then((response)=>{
                this.deviceTypeList=response.data.data
                this.failureType="";
                this.riskLevel = "";
                this.code = "";
                this.finding = "";
                this.assessment = "";
                this.criteria = "";
                this.criteriaHTML="";
                this.failureTypeList = "";
            })
        },

        searchFailureType(){
            axios.get("/api/ASIC/Report/getFailureType",{
                params:{
                    category: this.category,
                    deviceType:this.deviceType
                }
            }).then((response)=>{
                this.finding = "";
                this.assessment = "";
                this.criteria = "";
                this.criteriaHTML="";
                this.failureTypeList = response.data.data
            })
        },
        searchRiskLevelAndCode(){
            axios.get("/api/ASIC/Report/getRiskLevel",{
                params:{
                    failureType: this.failureType
                }
            }).then((response)=>{
                this.riskLevel = ""
                this.riskLevelList = response.data.data
            });
            axios.get("/api/ASIC/Report/getCode",{
                params:{
                    failureType: this.failureType
                }
            }).then((response)=>{
                this.code = response.data.data
                this.finding = "";
                this.assessment = "";
                this.criteria = "";
                this.criteriaHTML="";
            })
        },
        searchReference(){
            axios.get("/api/ASIC/Report/getReference",{
                params:{
                    failureType: this.failureType,
                    riskLevel: this.riskLevel
                }
            }).then((response)=>{
                // console.log(response.data.data.assessment)
                const reference = response.data.data
                this.finding = reference.finding
                this.assessment = reference.assessment
                this.riskLevel==reference.riskLevel.replace(/[\r\n]/g, '')
                if(this.riskLevel=='E1/2'){
                    //this.$message.success('E1/2');
                    this.criteriaHTML = `<span style="color: red; font-weight: bold;">Mandatory Complaint:</span>`;
                    this.criteria = reference.criteria;
                }
                else if(this.riskLevel=='E2/3'){
                    this.criteriaHTML = `<span style="color: red; font-weight: bold;">Case by Case Assessment:</span>`;
                    this.criteria = reference.criteria; 
                }
                else if(this.riskLevel=='E4'){
                    this.criteriaHTML = `<span style="color: red; font-weight: bold;">Good Criteria:</span>`;
                    this.criteria = reference.criteria;   
                }else{
                    this.criteria =reference.criteria  
                }
                
            });
        },
        deleteReference() {
  // 使用原生confirm函数创建确认对话框
  const isConfirmed = window.confirm('确定要删除吗？');

  if (isConfirmed) {
    // 用户点击了确认按钮，执行删除操作
    axios.get("/api/ASIC/Report/deleteContent", {
      params: {
        category: this.category,
        deviceType: this.deviceType,
        failureType: this.failureType,
        riskLevel: this.riskLevel
      }
    }).then((response) => {
      const responseData = response.data;

      if (responseData.data == '1' || responseData.data == '2') {
        // 删除成功
        this.$message.success('删除成功');
        // 清空数据属性
        this.category = '';
        this.deviceType = '';
        this.failureType = '';
        this.riskLevel = '';
        this.code = '';
        this.finding = '';
        this.criteria = '';
        this.assessment = '';

        window.location.reload();
      } else {
        // 删除失败，根据实际情况处理错误
        this.$message.error(`删除失败：数据库中不存在该值`);
      }
    });
  } else {
    // 用户点击了取消按钮，不执行删除操作
    this.$message.info('取消删除');
  }
},

        
    },
    
    created:function(){
        //axios.get("/api/ASIC/Report/getCategory")
        //.then((response)=>{
            //this.categoryList = response.data.data
        //})
    

    }


})



// 解决ERROR ResizeObserver loop completed with undelivered notifications.

//问题的

const debounce = (fn, delay) => {
  let timer = null;

  return function () {
    let context = this;

    let args = arguments;

    clearTimeout(timer);

    timer = setTimeout(function () {
      fn.apply(context, args);
    }, delay);
  };
};

// 解决ERROR ResizeObserver loop completed with undelivered notifications.

const _ResizeObserver = window.ResizeObserver;

window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
  constructor(callback) {
    callback = debounce(callback, 16);

    super(callback);
  }
};


</script>

<style>
.el-input,.el-input--large{
    margin-top:10px;
}

.el-select {
    margin-top:5px;
}

.custom-popper-class {
  left: auto !important;
  right: 0 !important;
}

</style>