const cors_proxy = require('cors-anywhere');
const express = require('express');
const app = express();

const host = '0.0.0.0';
const port = process.env.PORT || 8080;

// 🛡️ অ্যাডভান্সড আইপিটিভি হেডার ট্রান্সকোডার ইঞ্জিন
cors_proxy.createServer({
    originWhitelist: [], // যেকোনো ডোমেইন (আপনার গিটহাব) থেকে রিকোয়েস্ট এলাও করবে
    requireHeader: [],   // ব্রাউজারের কোনো কাস্টম হেডার রিকোয়ারমেন্ট থাকবে না
    removeHeaders: [
        'cookie', 
        'cookie2', 
        'x-request-url', 
        'x-requested-with',
        'user-agent',
        'referer'
    ],
    setHeaders: {
        'accept': '*/*',
        'access-control-allow-origin': '*',
        'access-control-allow-methods': 'GET, OPTIONS',
        'access-control-allow-headers': '*',
        'connection': 'keep-alive'
    },
    // ভিডিও ফাইলের বাফারিং ড্রপ বা ক্র্যাশ হ্যান্ডলার
    handleInitialRequest: function (req, res, location) {
        return false; 
    }
}).listen(port, host, () => {
    console.log('Zion IPTV Premium Proxy Engine Active on ' + host + ':' + port);
});
