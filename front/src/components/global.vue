<script>
let baseUrl;
if (process.env.VUE_APP_ENVIRONMENT === "productionEnv") {
  // 生产包环境
  baseUrl = "https://10.239.183.54:8082/api";
} else if (process.env.VUE_APP_ENVIRONMENT === "testEnv") {
  // 测试包环境
  baseUrl = "https://10.239.183.54:8082/api";
} else if (process.env.VUE_APP_ENVIRONMENT === "developmentEnv") {
  // 开发包环境
  baseUrl = "https://10.239.183.54:8082/api";
}
export default {
  url: baseUrl,
};
</script>

