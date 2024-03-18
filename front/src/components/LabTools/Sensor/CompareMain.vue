<template>
  <!-- 搜索区 -->
  <el-row align="middle">
    <el-col :span="4">
      <el-text tag="b" size="large"> Category </el-text>
    </el-col>

    <el-col :span="10">
      <el-space direction="vertical">
        <el-text tag="b" size="large"> Product1 </el-text>
        <el-select
          v-model="product1"
          clearable
          filterable
          placeholder="Select"
          @change="searchProduct1Pictures"
        >
          <el-option
            v-for="(item, index) in productList"
            :key="index"
            :label="item"
            :value="item"
          />
        </el-select>
      </el-space>
    </el-col>

    <el-col :span="10">
      <el-space direction="vertical">
        <el-text tag="b" size="large"> Product2 </el-text>
        <el-select
          v-model="product2"
          clearable
          filterable
          placeholder="Select"
          @change="searchProduct2Pictures"
        >
          <el-option
            v-for="(item, index) in productList"
            :key="index"
            :label="item"
            :value="item"
          />
        </el-select>
      </el-space>
    </el-col>
  </el-row>

  <el-divider />

  <!-- 展示区 -->
  <el-row
    v-for="(value, key, index) in product1Pictures"
    align="middle"
    justify="center"
  >
    <!-- 左侧文字 -->
    <el-col :span="4">
      <el-text tag="b" size="large" text-align="center">{{
        colName[index]
      }}</el-text>
    </el-col>

    <!-- 第一列图片 -->
    <el-col :span="10">
      <el-image
        style="width: 200px; height: 200px"
        :src="product1Pictures[key]"
        :preview-src-list="[product1Pictures[key]]"
        fit="scale-down"
      >
      </el-image>
    </el-col>

    <!-- 第二列图片 -->
    <el-col :span="10">
      <el-image
        style="width: 200px; height: 200px"
        :src="product2Pictures[key]"
        :preview-src-list="[product2Pictures[key]]"
        fit="scale-down"
      >
      </el-image>
    </el-col>
  </el-row>
</template>

<script>
import { defineComponent, ref } from "vue";
import axios from "axios";

export default defineComponent({
  name: "CompareMain",
  data() {
    return {
      colName: [
        "Package overview-top",
        "Package overview-bottom",
        "X-Ray overview(pin1 左上)",
        "dev board",
        "Overview after decap(OM)",
        "AISC OM view",
        "IR back side overview",
        "IR front side overview",
        "MEMS structure overview (SEM)",
        "功能区示意图 (if have)",
        "切片-1 (if have)",
        "切片-2（if have)",
        "预留位置-1",
        "预留位置-2",
        "预留位置-3",
        "预留位置-4",
      ],
      product1: ref(""),
      product2: ref(""),

      productList: [],
      product1Pictures: {
        PackageOverviewTop: "",
        PackageOverviewBottom: "",
        XRayOverview: "",
        DevBoard: "",
        OverviewAfterDecap_OM: "",
        AISC_OM_View: "",
        IRBackSideOverview: "",
        IRFrontSideOverview: "",
        MEMSStructureOverview_SEM: "",
        SchematicDiagramOfFunctionalArea: "",
        Slice1: "",
        Slice2: "",
        Placeholder1: "",
        Placeholder2: "",
        Placeholder3: "",
        Placeholder4: "",
      },
      product2Pictures: {
        PackageOverviewTop: "",
        PackageOverviewBottom: "",
        XRayOverview: "",
        DevBoard: "",
        OverviewAfterDecap_OM: "",
        AISC_OM_View: "",
        IRBackSideOverview: "",
        IRFrontSideOverview: "",
        MEMSStructureOverview_SEM: "",
        SchematicDiagramOfFunctionalArea: "",
        Slice1: "",
        Slice2: "",
        Placeholder1: "",
        Placeholder2: "",
        Placeholder3: "",
        Placeholder4: "",
      },
    };
  },
  methods: {
    
  },
  created: function () {
    // axios.get("/api/SocketsInfo/getProductList").then((response) => {
    //   this.productList = response.data.data;
    // });
  },
});
</script>

<style scoped>
.dataRow {
  height: 10vh;
}
</style>
