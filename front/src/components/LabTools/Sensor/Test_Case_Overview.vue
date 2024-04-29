<template>
<div style="display: flex; width: 100%; justify-content: center;">
  <el-steps  finish-status="success" simple style="width: 70%; margin-top: 5px;">
    <el-step title="Test Case Overview"></el-step>
    <el-step title="Environment Configuration"></el-step>
    <el-step title="Aotumation Configuration"></el-step>
  </el-steps>
</div>

  <div class="search-form">
    <div class="row">

      <div class="input-group">
        <label for="select1">Platform:</label>
        <select id="select1" v-model="selection1"  @change="logChange('selection1', $event.target.value)">
          <option value="SP1">SP1</option>
          <option value="SP2">SP2</option>
          <!-- 更多选项 -->
        </select>
      </div>

      <div class="input-group">
        <label for="select2">Test_Cycle_Name:</label>
        <select id="select2" v-model="selection2"  @change="logChange('selection2', $event.target.value)">
          <option value="Test_Cycle_1">Test_Cycle_1</option>
          <option value="Test_Cycle_2">Test_Cycle_2</option>
          <!-- 更多选项 -->
        </select>
      </div>

    </div>

    <div class="row">

      <div class="input-group">
        <label for="select3">Cycle_Config:</label>
        <select id="select3" v-model="selection3"  @change="logChange('selection3', $event.target.value)">
          <option value="Cycle_Config_1">Cycle_Config_1</option>
          <option value="Cycle_Config_2">Cycle_Config_2</option>
          <!-- 更多选项 -->
        </select>
      </div>

      <div class="input-group">
        <label for="select4">Test_Domain:</label>
          <el-select v-model="selection4" multiple placeholder="请选择"  @change="logChange('selection4', $event)">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
      </div>
    </div>

    <div class="row button-row">
      <button @click="search">Search</button>
    </div>

  </div>

  
   <!-- 查询结果列表 -->
   <div style="display: flex; justify-content: center; align-items: center; margin-top: 0px;">
    <el-table
      :data="tableData"
      height="300"
      border
      style="width: 80%"
      :row-class-name="tableRowClassName"
    >
    <el-table-column
      prop="ID"
      label="ID"
      width="200">
    </el-table-column>
    <el-table-column
      prop="Title"
      label="Title"
      width="200">
    </el-table-column>
    <el-table-column
      prop="Domain_Detail"
      label="DomainDetail"
      width="300">
    </el-table-column>
    <el-table-column
      prop="Automation_Marker"
      label="Automation Marker"
      width="300">
    </el-table-column>
    <el-table-column
      prop="Automation_Statues"
      label="Automation Statues"
      width="300">
    </el-table-column>
    <el-table-column
      prop="Automation_Comment"
      label="Automation Comment"
      width="300">
    </el-table-column>
  </el-table>
   </div>

  <!-- 跳转按钮 -->
  <div class="button-container">
    <button @click="navigateToOtherPage">Next</button>
  </div>

</template>



<script>

export default {
  data() {
    return {
      selection1: [], // 确保这是一个数组
      selection2: [], // 确保这是一个数组
      selection3: [], // 确保这是一个数组
      selection4: [], // 确保这是一个数组
      options: [{
          value: 'QAT',
          label: 'QAT'
        }, {
          value: 'DLB',
          label: 'DLB'
        }, {
          value: 'DSA',
          label: 'DSA'
        }, {
          value: 'Networking',
          label: 'Networking'
        }, {
          value: 'SRIOV',
          label: 'SRIOV'
        }],
        value1: [],
        value2: [],

       tableData: [{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        }, {
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: 'Test_ID',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },
        ]
    };
  },
  methods: {
    logChange(fieldName, value) {
    console.log(`Value of ${fieldName} changed to: `, value);
  },
    
    navigateToOtherPage() {
      this.$router.push({
        path: '/LabTools/Sensor/Env_Config',
        query: {
          selection1: this.selection1,
          selection2: this.selection2,
          selection3: this.selection3,
          selection4: JSON.stringify(this.selection4) // 因为是数组，所以使用JSON.stringify转换为字符串
        }
  });
    },
    tableRowClassName({ rowIndex }) {
      return rowIndex === 0 ? 'first-row' : '';
    },
    search() {
      // 在这里执行搜索逻辑
      console.log('执行搜索', this.selection1, this.selection2, this.selection3, this.selection4);
    }
  },
};
</script>

<style>
.el-table__header-wrapper tr th {
  background-color: #0056b3 !important; /* 使用 !important 来确保样式的优先级 */
  color: white; /* 可以设置字体颜色为白色，如果需要的话 */
}

.button-container {
  display: flex;
  justify-content: flex-end; /* 将按钮对齐到右边 */
  margin-right: 85px; /* 右边距20px */
}

.button-container button {
  margin-top: 1%;
  padding: 10px 35px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.button-container button:hover {
  background-color: #0056b3;
}
</style>


<style scoped>
@import "vue-multiselect/dist/vue-multiselect.css";


.search-form {
  max-width: 90%;
  margin: 10px auto;
  padding: 10px;
  border: 3px solid #f7f6f6;
  border-radius: 10px;
  background: #ffffff;
}

.row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.input-group {
  display: flex;
  flex-direction: column;
  margin: 0 20px;
  width: calc(50% - 20px); /* 减去间距的一半 */
}

.input-group label {
  margin-bottom: 10px;
  font-weight: bold;

}

.input-group select{
  padding: 0px;
  border: 2px solid #e6e6e6;
  border-radius: 4px;
  width: 100%; /* 选择框宽度调整为100% */
  font: 1em sans-serif;
  height: 33px;
  
}


.button-row {
  display: flex;
  justify-content: flex-end;
  margin-top: 0px; /* 增加按钮与上方元素的间距 */
}

.row button {
  margin-top:1% ;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.row button:hover {
  background-color: #0056b3;
}

</style>
