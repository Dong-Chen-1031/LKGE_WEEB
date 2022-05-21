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

        document.write('<script src="https://www.gstatic.com/firebasejs/4.12.1/firebase.js"></script>');
        document.write('<script src="https://www.gstatic.com/firebasejs/4.12.1/firebase-firestore.js"></script>');

        setTimeout(() => {
             // 連線firebase
            var firebaseConfig = {
                apiKey: "AIzaSyCi0oeTkEvfSuXpvHNiiyLNWvcFfiynIKE",
                authDomain: "dong-max.firebaseapp.com",
                projectId: "dong-max",
                storageBucket: "dong-max.appspot.com",
                messagingSenderId: "266795821751",
                appId: "1:266795821751:web:a9a4a407623bed2c903b32"
            };
            firebase.initializeApp(firebaseConfig);
            var db = firebase.firestore();

                
            //功能
            function setdb(t輸入資料,coll,doc){ //寫入資料
                let db路徑 = db.collection(coll).doc(doc);
                db路徑.set(t輸入資料,{merge:true}).then(() => {
                    console.log('set data successful');
                });
            }

            timemane=String(Date.now())

            //起始
            let t輸出資料 = {
                起始時間:new Date()
            }
            setdb(t輸出資料,'max-紀錄',timemane)   


            setInterval(() => {
                let t輸出資料 = {
                    結束時間:new Date()
                }
                setdb(t輸出資料,'max-紀錄',timemane)
            }, 10000);
            console.log(location.href.split("/"));
        }, 10000);

       
    };
})();