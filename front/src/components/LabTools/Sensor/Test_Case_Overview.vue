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
        <label for="selection1">Platform:</label>
        <select id="selection1" v-model="selection1Model"  @change="logChange('selection1Model', $event.target.value)">
          <option value="SP1">SP1</option>
          <option value="SP2">SP2</option>
          <!-- 更多选项 -->
        </select>
      </div>

      <div class="input-group">
        <label for="selection2">Test_Cycle_Name:</label>
        <select id="selection2" v-model="selection2Model"  @change="logChange('selection2Model', $event.target.value)">
          <option value="Test_Cycle_1">Test_Cycle_1</option>
          <option value="Test_Cycle_2">Test_Cycle_2</option>
          <!-- 更多选项 -->
        </select>
      </div>

    </div>

    <div class="row">

      <div class="input-group">
        <label for="selection3">Cycle_Config:</label>
        <select id="selection3" v-model="selection3Model"  @change="logChange('selection3Model', $event.target.value)">
          <option value="Cycle_Config_1">Cycle_Config_1</option>
          <option value="Cycle_Config_2">Cycle_Config_2</option>
          <!-- 更多选项 -->
        </select>
      </div>

      <div class="input-group">
        <label for="selection4">Test_Domain:</label>
          <el-select id="selection4" v-model="selection4Model" multiple placeholder="请选择"  @change="logChange('selection4Model', $event)">
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
      style="width: 80%"
      :row-class-name="tableRowClassName"
      :default-sort = "{prop: 'ID', order: 'descending'}"
    >
    <el-table-column
      prop="ID"
      label="ID"
      sortable
      width="200">
    </el-table-column>
    <el-table-column
      prop="Title"
      label="Title"
      sortable
      width="200">
    </el-table-column>
    <el-table-column
      prop="Domain_Detail"
      label="DomainDetail"
      sortable
      width="300">
    </el-table-column>
    <el-table-column
      prop="Automation_Marker"
      label="Automation Marker"
      sortable
      width="300">
    </el-table-column>
    <el-table-column
      prop="Automation_Statues"
      label="Automation Statues"
      sortable
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
import { mapState, mapMutations } from 'vuex';
export default {
  data() {
    return {
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
          ID: '1',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        }, {
          ID: '2',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: '3',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: '4',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: '5',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: '6',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: '7',
          Title: 'Title',
          Domain: 'Domain',
          Domain_Detail: 'Domain Detail',
          Automation_Marker: 'Automation Marker',
          Automation_Statues: 'Automation Statues',
          Automation_Comment: 'Automation Comment'     
        },{
          ID: '8',
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
  computed: {
    ...mapState({
      selection1: state => state.selections.selection1,
      selection2: state => state.selections.selection2,
      selection3: state => state.selections.selection3,
      selection4: state => state.selections.selection4,
    }),
    // 提供 getter 和 setter 的计算属性
    selection1Model: {
      get() {
        return this.selection1;
      },
      set(value) {
        this.setSelection({ key: 'selection1', value });
      }
    },
    selection2Model: {
      get() {
        return this.selection2;
      },
      set(value) {
        this.setSelection({ key: 'selection2', value });
      }
    },
    selection3Model: {
      get() {
        return this.selection3;
      },
      set(value) {
        this.setSelection({ key: 'selection3', value });
      }
    },
    selection4Model: {
      get() {
        return this.selection4;
      },
      set(value) {
        this.setSelection({ key: 'selection4', value });
      }
    },
  },

  methods: {
    ...mapMutations({
      setSelection: 'setSelection'
    }),
    logChange(fieldName, value) {
      this.setSelection({ key: fieldName, value });
    },
    navigateToOtherPage() {
      this.$router.push('/LabTools/Sensor/Env_Config');
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
