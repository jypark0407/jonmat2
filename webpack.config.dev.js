var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.config.common');
var port = 8008;


Object.keys(config.entry).forEach(function(key) {
    config.entry[key].unshift('webpack/hot/only-dev-server');
    config.entry[key].unshift('webpack-dev-server/client?http://0.0.0.0:' + port);
});

module.exports = {
    port: port,
    devtool: 'eval',
    context: config.context,
    entry: config.entry,
    output: {
        path: path.join(__dirname, 'static/build/'),
        filename: '[name].js',
        publicPath: 'http://localhost:' + port + '/static/'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(),
        new BundleTracker()
    ],
    resolve: config.resolve,
    module: config.module
};
