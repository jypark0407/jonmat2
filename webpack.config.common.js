var path = require('path');
var webpack = require('webpack');


module.exports = {
    context: path.join(__dirname, 'front'),
    entry: {
        'commons': ['commons.jsx'],
        'index': ['index.jsx'],
        'restaurant': ['restaurant.jsx'],
        'restaurantList': ['restaurantList.jsx'],
        'congressMember': ['congressMember.jsx'],
        'congressMemberList': ['congressMemberList.jsx']
    },
    resolve: {
        extensions: ['', 'styl', '.jsx', '.js'],
        modulesDirectories: ['node_modules', 'front']
    },
    module: {
        loaders: [{
            test: /\.jsx?$/,
            loader: 'babel',
            query: {
                presets: ['es2015', 'react', 'react-hmre']
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
