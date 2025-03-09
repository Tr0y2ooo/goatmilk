# goatmilk
## 前言
這是一個公開版本的專案內容，這是一個小型簡單的ERP系統，礙於一些內容以及品牌名稱無法出現，所以有些部分可能會呈現的不完整，作者只有我一個人全手刻出來的QQ，原本聽老闆的需求以為是簡單幾個網頁，沒想到老闆需求越開越大慢慢地從幾個功能變成幾個平台幾十個功能，最後老闆甚至還有想加入AI的衝動，我在向他說明維護成本後，老闆比較收斂了XDD。  

## 專案簡介
如前言所說，這是一個小型的ERP系統，主要處理羊奶的訂購、叫貨、點貨、收款等等雜七雜八的功能，使用到兩種平台，APP以及網頁版，APP主要是給配送羊奶的員工使用的，語言是flutter，網頁有兩個，內部員工管理後台和客戶訂購的電商網站，管理後台是純html+js+css沒套模板，後端資料庫是用google的firebase；電商網站是wordpress套版加上一些客製化的修改，目前整個系統還在持續更新中，因為老闆需求也一直在增加...。

## 主要功能
### APP
- 帳號綁定Google登入
  - 使用firebase的Authorization做登入驗證的部分，透過Google帳號統一管理。
  - ![image](https://github.com/user-attachments/assets/788bfd0e-6693-4a76-8ad8-b152aea971f9)
  - ![image](https://github.com/user-attachments/assets/57338a2f-fc16-4830-9e0a-7089ece91702)

- 讀取excel轉換成導航頁面(統計該日羊奶總數及口味)
  - ![image](https://github.com/user-attachments/assets/4a9246db-db71-42b6-afa2-f1e31a2b0b7f)
  - ![image](https://github.com/user-attachments/assets/83660e7f-8832-4e76-a6aa-c6ecaaccfe68)
  - ![image](https://github.com/user-attachments/assets/65d9d370-099b-4383-b17c-b1683a28a160)
 
- 配送範圍
  - ![image](https://github.com/user-attachments/assets/0ec3f1af-e08f-42ac-b34c-6ff693576558)

- 及時回報聊天室(可以傳圖片文字座標)
  - ![image](https://github.com/user-attachments/assets/536750e0-43c4-46b6-842e-14c046da05f4)

- 簽署入職合約(簽署完會自動產出一分簽好的合約存在個人的google空間)
  - ![image](https://github.com/user-attachments/assets/293b04f5-bf40-4295-9163-867afbafd644)

### 電商網站
- 產品展示(有購物車功能)
  - ![image](https://github.com/user-attachments/assets/ddf215a7-c438-4c2b-b81b-da3ba694458c)
- Google評論網友評價
  - 
- 公司簡介
  - ![image](https://github.com/user-attachments/assets/bf0f15af-8da6-4f5e-848e-925dfd0b4cd0)

- 新聞報導文章
- 聯絡資訊
### 後台網站
- 個人資料
- 新增訂單
- 查詢&修改訂單
- 查詢客戶資料
- 羊奶總數點貨
- 配送員總數
- 配送員回報
- 客戶帳單查詢
- 所有客戶帳單一覽
- 對帳
- 幼稚園(團戶)訂購及收費
