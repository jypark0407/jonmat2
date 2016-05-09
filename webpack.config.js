var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var port = 8008;


module.exports = {
    port: port,
    // devtool: 'source-map',
    devtool: 'eval',
    context: path.join(__dirname, 'front'),
    entry: {
        'commons': [
            'webpack-dev-server/client?http://0.0.0.0:' + port,
            'webpack/hot/only-dev-server',
            'commons.jsx'
        ],
        'index': [
            'webpack-dev-server/client?http://0.0.0.0:' + port,
            'webpack/hot/only-dev-server',
            'index.jsx'
        ],
        'restaurant': [
            'webpack-dev-server/client?http://0.0.0.0:' + port,
            'webpack/hot/only-dev-server',
            'restaurant.jsx'
        ],
        'congress-member': [
            'webpack-dev-server/client?http://0.0.0.0:' + port,
            'webpack/hot/only-dev-server',
            'congress-member.jsx'
        ]
    },
    output: {
        path: path.join(__dirname, 'static/build/'),
        filename: '[name].js',
        publicPath: 'http://localhost:' + port + '/static/'
        // publicPath: '/static/build/'
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
            loader: 'babel',
            query: {
                presets: [ 'es2015', 'react', 'react-hmre' ]
            },
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
