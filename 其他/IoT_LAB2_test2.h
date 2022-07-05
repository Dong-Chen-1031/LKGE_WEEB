//----------------------這裡是主頁面--------------------
static const char mainPage[] PROGMEM = u8R"(
  <!DOCTYPE html>
  <html>
  <head>
      <title>遙控車</title>
      <meta name='viewport' content='width=device-width, initial-scale=1.0'>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  </head>
  <body>
    <a href='call?buzzer=w'>前進</a> 
    <br><br>
    <a href='call?buzzer=s'>後退</a> 
    <br><br>
    <a href='call?buzzer=a'>左轉</a> 
    <br><br>
    <a href='call?buzzer=d'>右轉</a> 
  </body>
  </html>
)";

//----------------------這裡是錯誤路徑頁面--------------------
static const char errorPage[] PROGMEM= u8R"(

)";
  
static const char settingPage[] PROGMEM= u8R"(

)";

//---------勿刪 (讓網頁資料儲存在程式區以節省記憶體)------------
#define WEBPAGE_IN_PROGMEM

