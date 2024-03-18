<template>
  <el-row :gutter="20" justify="space-evenly" align="middle">
    <el-col :span="4" align="center">
      <el-text tag="b" size="large">Year Of Report</el-text>
      <el-select
        v-model="year"
        clearable
        filterable
        placeholder="SELECT"
        @change="getInfoList"
        @focus="loadYearOptions"
      >
        <el-option
          v-for="(item, index) in yearList"
          :key="index"
          :label="item"
          :value="item"
        />
      </el-select>
    </el-col>

    <el-col :span="4" align="center">
      <el-text tag="b" size="large">Project Group</el-text>
      <el-select
        v-model="group"
        clearable
        filterable
        placeholder="SELECT"
        @change="getInfoList"
        @focus="loadGroupOptions"
      >
        <el-option
          v-for="(item, index) in groupList"
          :key="index"
          :label="item"
          :value="item"
        />
      </el-select>
    </el-col>

    <el-col :span="4" align="center">
      <el-text tag="b" size="large">Device Name</el-text>
      <el-select
        v-model="device"
        clearable
        filterable
        placeholder="SELECT"
        @change="getInfoList"
        @focus="loadDeviceOptions"
      >
        <el-option
          v-for="(item, index) in deviceList"
          :key="index"
          :label="item"
          :value="item"
        />
      </el-select>
    </el-col>
  </el-row>
  <el-row :gutter="20" justify="space-evenly" align="middle">
    <el-col :span="4" align="center">
      <el-text tag="b" size="large">Internal No.</el-text>
      <!-- <el-tooltip placement="top">
                <template #content>
                    <span>{{failureType}}</span>
                </template> -->
      <!-- <el-select v-model="internalNo" style="width:300px;"  filterable placeholder='SELECT'> -->
      <el-select
        v-model="internalNo"
        clearable
        filterable
        placeholder="SELECT"
        @change="getInfoList"
        @focus="loadInternalNoOptions"
      >
        <el-option
          v-for="(item, index) in internalNoList"
          :key="index"
          :label="item"
          :value="item"
        />
      </el-select>
      <!-- </el-tooltip> -->
    </el-col>
    <el-col :span="4" align="center" wrap>
      <el-text tag="b" size="large">Stress Type</el-text>
      <el-select
        v-model="stressType"
        clearable
        filterable
        placeholder="SELECT"
        @change="getInfoList"
        @focus="loadStressTypeOptions"
        :filter-method="handleFilter"
      >
        <el-option
          v-for="(item, index) in stressTypeList"
          :key="index"
          :label="item"
          :value="item"
        />
      </el-select>
    </el-col>
  </el-row>
  <el-divider border-style="dashed" />
  <el-row>
    <el-table :data="infoData" style="width: 100%">
      <el-table-column type="expand">
        <template #default="props">
          <h2>Information:</h2>
          <div class="pre-line">{{ props.row.information }}</div>
          <h2>ShortReport:</h2>
          <div class="pre-line">{{ props.row.shortReport }}</div>
        </template>
      </el-table-column>

      <el-table-column label="Activity" prop="activity" />
      <el-table-column label="Link" prop="link">
        <template #default="scope">
          <el-link :href="scope.row.link">
            {{ scope.row.link }}
          </el-link>
        </template>
        <!-- \\szh0fs15.apac.bosch.com\AE_QMS_CN$\07_DPA\701_DPA\tap -->
      </el-table-column>
    </el-table>
  </el-row>
  <!-- 测试 -->
  <a href="file:\\\\\bosch.com\dfsrb\DfsCN\DIV"
    >click me, jump to the folder \DfsCN\DIV</a
  >
  <br />
  <a href="file:\\\\\szh0fs15.apac.bosch.com\AE_QMS_CN$\07_DPA\701_DPA\tap"
    >click me, jump to the folder 07_DPA\701_DPA\tap</a
  >
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

defineProps("ReportReferenceMain");

// 定义响应式数据
const year = ref("");
const group = ref("");
const device = ref("");
const internalNo = ref("");
const stressType = ref("");

const yearList = ref([]);
const groupList = ref([]);
const deviceList = ref([]);
const internalNoList = ref([]);
const stressTypeList = ref([]);
const infoData = ref([]);

// 定义方法
const loadYearOptions = () => {
  axios
    .get("/api/ASIC/MasterExcel/getYear", {
      params: {
        group: group.value,
        device: device.value,
        internalNo: internalNo.value,
        stressType: stressType.value,
      },
    })
    .then((response) => {
      yearList.value = response.data.data;
    });
};

const loadGroupOptions = () => {
  axios
    .get("/api/ASIC/MasterExcel/getGroup", {
      params: {
        year: year.value,
      },
    })
    .then((response) => {
      groupList.value = response.data.data;
      group.value = "";
      device.value = "";
      internalNo.value = "";
    });
};

const loadDeviceOptions = () => {
  axios
    .get("/api/ASIC/MasterExcel/getDevice", {
      params: {
        year: year.value,
        group: group.value,
        internalNo: internalNo.value,
        stressType: stressType.value,
      },
    })
    .then((response) => {
      deviceList.value = response.data.data;
    });
};

const loadInternalNoOptions = () => {
  axios
    .get("/api/ASIC/MasterExcel/getInternalNo", {
      params: {
        year: year.value,
        group: group.value,
        device: device.value,
        stressType: stressType.value,
      },
    })
    .then((response) => {
      internalNoList.value = response.data.data;
    });
};

const loadStressTypeOptions = () => {
  axios
    .get("/api/ASIC/MasterExcel/getStressType", {
      params: {
        year: year.value,
        group: group.value,
        device: device.value,
        internalNo: internalNo.value,
      },
    })
    .then((response) => {
      stressTypeList.value = response.data.data;
    });
};

const getInfoList = () => {
  axios
    .get("/api/ASIC/MasterExcel/getInfo", {
      params: {
        year: year.value,
        group: group.value,
        device: device.value,
        internalNo: internalNo.value,
        stressType: stressType.value,
      },
    })
    .then((response) => {
      infoData.value = response.data.data;
    });
};
</script>

<style>
.el-input,
.el-input--large {
  margin-top: 10px;
}

.el-row {
  margin-bottom: 40px;
}

.el-select {
  margin-top: 5px;
}

.pre-line {
  white-space: pre-line;
}
</style>
