<h1>This is the setting page for webserver for BKC</h1><br>
##Leo 06/24/2024<br>
机器：cyp10<br>
ip:10.239.183.54<br>

webserver包括三部分<br>
1.**Vue(前端）**<br>
2.**Nginx(中间件）**<br>
3.**Django(后端）**<br>


# 1. Vue前端介绍 <br>
## 1.1文件夹介绍 <br>
### 1.1.1 dist 
dist代表的是打包之后的文件夹，表明是使用npm run build 打包前端一直运行

### 1.1.2 node_modules
是采用npm install 安装必备的前端包，用处不大

### 1.1.3 public
存放共用标识符，可以忽略

### 1.1.4 src
| src | 前端代码存储 |
| --- | --- |
| 1 assest | 存放前端图片文件 |
| 2 components<br>(important) | 存放的是前端页面代码，是最主要的界面 <br> Execution里面存放的是执行的三个界面 <br> 分别是test_case_overview / environment_configuration(Env_Config.vue) / automation_configuration(Aotu_Config.vue) <br> History里面存放的是历史记录页面（只完成了demo，其他的还待完善) <br> Container.vue是界面总体布局的文件 <br>Header.vue是页面抬头的页面文件 <br>Loading.vue是页面加载的文件 <br>Login.vue是登陆界面 <br>global.vue是全局文件 |
| 3 plugins | element.js是js文件，用于页面布局 | 
| 4 router | 页面路由配置文件，也就是页面link绑定到前端的那个文件 url和前端文件匹配的文件 |
| 5 store | 前端页面缓存文件，类似于cookie，将数据缓存在前端，让页面跳转的时候数据仍然保存，<br> 页面refresh之后数据就会丢失 |
|6 App.vue | 页面全局布置文件 |
| 7 main.ts | 页面全局属性文件 |
| 8 shims-vue.d.ts | 不用管，默认配置文件 |

### 1.1.5 .env.*
这个表示在不同的运行状态下，前端的api将传递到后端哪一个接口，不需要动

### 1.1.6 vue.config.js
代表动态资源和静态资源将如何搜索路径，配置好的不需要动

## 1.2 运行路径介绍
举例，从test_case_overview.vue开始，axios.get('/SearchTestCase', { params })（Line.394）<br>
-->main.ts:axios.defaults.baseURL = "http://10.239.183.54:8082" 打入到nginx 8082接口<br>
-->传入到后端,进行api接口，然后将数据从nginx返回到前端，完成前端数据传输 

# 2. Nginx介绍
https://wiki.ith.intel.com/display/NPX/Webserver+Setting

# 3. Django后端介绍
https://wiki.ith.intel.com/display/NPX/Webserver+Setting






