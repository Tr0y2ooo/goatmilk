# goatmilk
## 前言
這是一個公開版本的專案內容，這是一個小型簡單的ERP系統，礙於一些內容以及品牌名稱無法出現，所以有些部分可能會呈現的不完整，作者只有我一個人全手刻出來的QQ，原本聽老闆的需求以為是簡單幾個網頁，沒想到老闆需求越開越大慢慢地從幾個功能變成幾個平台幾十個功能，最後老闆甚至還有想加入AI的衝動，我在向他說明維護成本後，老闆比較收斂了XDD。  

## 專案簡介
如前言所說，這是一個小型的ERP系統，主要處理羊奶的訂購、叫貨、點貨、收款等等雜七雜八的功能，使用到兩種平台，APP以及網頁版，APP主要是給配送羊奶的員工使用的，語言是flutter，網頁有兩個，內部員工管理後台和客戶訂購的電商網站，管理後台是純html+js+css沒套模板，後端資料庫是用google的firebase；電商網站是wordpress套版加上一些客製化的修改，目前整個系統還在持續更新中，因為老闆需求也一直在增加...。

## 主要功能
### APP
- 帳號綁定Google登入
  - 使用firebase的Authorization做登入驗證的部分，透過Google帳號統一管理。
  - ![image](https://github.com/user-attachments/assets/813a1e23-324a-4797-bc5e-ceaabbcb575a)

  - ![image](https://github.com/user-attachments/assets/5ef7d725-0ccf-487a-86e0-1bf0c4e35f3a)


- 讀取excel轉換成導航頁面(統計該日羊奶總數及口味)
  - ![image](https://github.com/user-attachments/assets/b62e2b0c-c74b-4da6-8ac3-786992cef9bb)

  - ![image](https://github.com/user-attachments/assets/baf0e213-71d5-48d3-9f1e-873cb7675431)

  - ![image](https://github.com/user-attachments/assets/33837ad9-1230-446a-a653-fada95d4b891)
  - ![image](https://github.com/user-attachments/assets/8ba8e317-4f89-4fbf-a6f1-9f6cb143a2c1)


 
- 配送範圍
  - ![image](https://github.com/user-attachments/assets/2b56aac0-1394-467d-b412-0a564c54e270)


- 及時回報聊天室(可以傳圖片文字座標)
  - ![image](https://github.com/user-attachments/assets/ac46f791-d7e3-41f3-8ae6-0cb3ca0f4842)


- 簽署入職合約(簽署完會自動產出一分簽好的合約存在個人的google空間)
  - ![image](https://github.com/user-attachments/assets/b99a706e-8467-4c45-b0c5-fcba990fb0b3)


### 電商網站
- 產品展示(有購物車功能)
  - ![image](https://github.com/user-attachments/assets/f0974ffe-ec15-4d88-bc02-4c8fffa617bf)
  - ![image](https://github.com/user-attachments/assets/087e234e-4caf-4d79-9072-a400017ba058)


- Google評論網友評價
  - ![image](https://github.com/user-attachments/assets/b44638d4-b059-41d8-bce9-7b387362e3a7)

- 公司簡介
  - ![image](https://github.com/user-attachments/assets/5fd03717-b911-4df3-8330-af9066878dbb)

- 新聞報導文章
  - ![image](https://github.com/user-attachments/assets/87bf1b75-55a4-490f-b6eb-cfb3b0801526)

- 聯絡資訊
  - ![Uploading image.png…]()

### 後台網站
- 登入介面
  - 可以用Google登入或是電話號碼(限定台灣門號)
  - ![image](https://github.com/user-attachments/assets/9d7817e6-f00c-40d4-82c5-b9b8667a8cd5)

  - ![image](https://github.com/user-attachments/assets/0146c5ef-6c0a-4961-9f8e-d256e91cc441)



- 個人資料
  - 這邊有設計4個等級的身分(最高管理員(老闆)->管理員(助理)->配送員->客戶)
  - 最高管理員有所有的功能，還能管理其他帳號的身分，查看入帳的修改紀錄
  - 管理員除了上述兩個功能，以下都是管理員有權限可以使用的
  - 配送員只有新增訂單跟查看每日任務可以用
  - 客戶功能有查看自己的餘額、自己這個月的訂單，可以自己修改，最晚可以在前一天晚上6點前修改、自己的帳單可以列印出來繳
  - ![image](https://github.com/user-attachments/assets/341703e1-85ec-42cf-bca5-9c1eb4104c7c)


- 新增訂單
  - ![image](https://github.com/user-attachments/assets/3b569d0b-ac74-4cb9-bfb5-b71af3f72045)


- 查詢&修改訂單
  - ![image](https://github.com/user-attachments/assets/8ba6515e-5909-49a8-bbec-0a3f3690de19)

  - ![image](https://github.com/user-attachments/assets/70b534e9-af8e-4e30-ac4a-eb1a10f51eab)


- 查詢客戶資料
  - 可以輸入客戶姓名或是地址或是電話對後端資料庫做查詢
  - ![image](https://github.com/user-attachments/assets/642412bb-29e7-4bbc-907e-67189cead02f)

  - 有word predict的功能
  - ![image](https://github.com/user-attachments/assets/92b04477-72e5-4c76-8dd0-c1f52b435e3f)



- 羊奶總數點貨
  - ![image](https://github.com/user-attachments/assets/d8f0f3b3-f4a7-4f96-80ee-a8114a18f8cb)

  - ![image](https://github.com/user-attachments/assets/2e238b7e-7931-42ca-ba35-a85c266a92a3)

  - ![image](https://github.com/user-attachments/assets/a511b6b7-33d2-4fe6-aca4-956ec5d49445)


- 配送員總數
  - 盤點配送員該路線今日總瓶數以及路線，產出CSV搭配手機APP做導航
  - ![image](https://github.com/user-attachments/assets/c3228a32-76f4-436c-bd8b-1610d5a8f3b2)

  - 可以下載成CSV
  - ![image](https://github.com/user-attachments/assets/2b3edbc3-b055-449e-9784-bdbaf9ab7c1a)



- 配送員回報
  - 選好日期後會顯示出有回報的配送員
  - ![image](https://github.com/user-attachments/assets/ff25db7d-e611-49d0-ab27-8da26cf9d341)

  - 選好後會出現他回報的內容，也就是手機APP聊天室那邊的訊息
  - ![image](https://github.com/user-attachments/assets/80b3fcbd-8dc2-4baf-a36f-af2b146f2814)

- 客戶帳單查詢
  - ![image](https://github.com/user-attachments/assets/cc8b28d3-ec65-4bac-897f-a0173e7a76e9)


- 所有客戶帳單一覽
  - 可以顯示該路線所有人的餘額(負的表示有帳單未繳)
  - ![image](https://github.com/user-attachments/assets/904a6397-7646-4277-8177-c512dd34c6fa)

  - 切換成只有負的客戶，方便客服人員通知客戶
  - ![image](https://github.com/user-attachments/assets/4c27fb15-2bf0-44f6-8f81-5c36ac490ea6)



- 對帳
  - ![image](https://github.com/user-attachments/assets/a35c9bf5-831b-426d-a95d-6d6f9d7b78d9)

  - 入帳
  - ![image](https://github.com/user-attachments/assets/8cfec960-87fa-4b4f-ace0-088c045498d2)

  - 餘額及時更新
  - ![image](https://github.com/user-attachments/assets/3f0b5e1b-7b53-4706-94bb-ef28a4bc7aa7)

  - 後端有更改紀錄，這邊之後會做一個前端給老闆管理
  - ![image](https://github.com/user-attachments/assets/f7499b21-17c8-43bf-ba6d-9ee88aa6653e)

