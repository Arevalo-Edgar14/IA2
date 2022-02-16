module.exports = {
  devServer: {
    watchOptions: {
      ignored: /node_modules/,
      aggregateTimeout: 300,
      poll: 500
    },
    // compress: true,
    // host: 'projectname.local'
    // public: 'ia2_devcontainer-app-1:8080',
    // public: '127.0.0.11:8080',
    public: '0.0.0.0:8080',
    disableHostCheck: true,
    port: 4000
  }
}
