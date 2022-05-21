// ==UserScript==
// @name         上線紀錄
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  上線紀錄!柏東、浩雲專用
// @author       Dong
// @match        http://*/*
// @match        https://mail.google.com/*
// @icon         https://ssl.gstatic.com/ui/v1/icons/mail/images/favicon_chat_r2.ico
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    if (location.href.split("/")[2]='mail.google.com') {
        console.log(location.href.split("/"));
    }
})();