module.exports = {
   
    
    publicPath: process.env.NODE_ENV === 'production' ? '/api' : '/',
    lintOnSave: false,  // 关闭eslint校验
    publicPath: '/',   // 静态资源路径改为相对路径，否则静态资源路径会报错
    outputDir: process.env.outputDir    // 打包生成目录
}

