const cors_proxy = require('cors-anywhere');
const express = require('express');
const app = express();

const host = '0.0.0.0';
const port = process.env.PORT || 8080;

// প্রক্সি সার্ভার ইঞ্জিন সেটআপ
cors_proxy.createServer({
    originWhitelist: [], // খালি রাখার মানে যেকোনো সাইট (আপনার গিটহাব) থেকে এটি অ্যাক্সেস করা যাবে
    requireHeader: [],
    removeHeaders: ['cookie', 'cookie2']
}).listen(port, host, () => {
    console.log('Zion Proxy Running on ' + host + ':' + port);
});
