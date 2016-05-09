var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var port = 8008;


module.exports = {
    port: port,
    devtool: 'source-map',
    context: path.join(__dirname, 'front'),
    entry: {
        'commons': [
            'commons.js'
        ],
        'restaurant': [
            'restaurant.js'
        ],
        'congress-member': [
            'congress-member.js'
        ]
    },
    output: {
        path: path.join(__dirname, 'static/build/'),
        filename: '[name].js',
        // publicPath: 'http://localhost:' + port + '/static/'
        publicPath: '/static/build/'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(),
        new BundleTracker()
        // new webpack.DefinePlugin({
        // 	__CONFIG__: JSON.stringify('debug')
        // })
    ],
    resolve: {
        extensions: ['', 'styl', '.jsx', '.js'],
        modulesDirectories: ['node_modules', 'front']
    },
    module: {
        loaders: [{
            test: /\.jsx?$/,
            loaders: ['react-hot', 'babel?presets[]=es2015&presets[]=react'],
            exclude: 'node_modules'
        }, {
            test: /\.json$/,
            loaders: ['json']
        }, {
            test: /\.styl$/,
            loaders: ['style', 'css', 'stylus']
        }, {
            test: /\.(png|jpg|svg)$/,
            loaders: ['file']
        }]
    }
};
