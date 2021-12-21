module.exports = {
  configureWebpack: {
    resolve: {
      alias: {
        "@": require("path").resolve(__dirname, "src")
      }
    }
  },
   devServer: {
    proxy: {
      "api/": {
        target: "http://localhost:8000/",
        changeOrigin: true,
        headers: {
          "X-Forwarded-For": "http://localhost:8000/",
        },
        onProxyRes(proxyRes) {
          proxyRes.headers["Access-Control-Allow-Origin"] = "*";
          proxyRes.headers["Access-Control-Allow-Methods"] = "*";
          proxyRes.headers["Access-Control-Allow-Headers"] = "*";
        },
      },
    },
  },
};