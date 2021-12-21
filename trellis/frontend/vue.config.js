module.exports = {
  // configureWebpack: {
  //   resolve: {
  //     alias: {
  //       "@": require("path").resolve(__dirname, "src")
  //     }
  //   }
  // },
   devServer: {
     proxy: {
        "/api/*": {
          target: "http://localhost:8000/",
          pathRewrite: {
                  '^/api': ''
          },
          secure: false
        }
     }
  },
};