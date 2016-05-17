var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.config.common');


module.exports = {
    context: config.context,
    entry: config.entry,
    output: {
        path: path.join(__dirname, 'static/build/'),
        filename: '[name].js',
        publicPath: '/static/build/'
    },
    plugins: [
        new BundleTracker()
    ],
    resolve: config.resolve,
    module: config.module
};
