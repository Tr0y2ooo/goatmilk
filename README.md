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
  - ![image](https://github.com/user-attachments/assets/1bf972af-39c8-4298-baf9-66aa70e47267)
- 公司簡介
  - ![image](https://github.com/user-attachments/assets/bf0f15af-8da6-4f5e-848e-925dfd0b4cd0)
- 新聞報導文章
  - ![image](https://github.com/user-attachments/assets/3eb96dbf-1d7d-4c16-8a33-6db17b18289c)
- 聯絡資訊
  - ![image](https://github.com/user-attachments/assets/0ac10403-dc7c-4afb-8569-8a1e366fd73a)
### 後台網站
- 登入介面
  - 可以用Google登入或是電話號碼(限定台灣門號)
  - ![image](https://github.com/user-attachments/assets/e27c6ece-4ae5-43c1-9c40-672798ee7375)
  - ![image](https://github.com/user-attachments/assets/96297784-8159-4c62-ba12-c79e66dc8c8f)


- 個人資料
  - 這邊有設計4個等級的身分(最高管理員(老闆)->管理員(助理)->配送員->客戶)
  - 最高管理員有所有的功能，還能管理其他帳號的身分，查看入帳的修改紀錄
  - 管理員除了上述兩個功能，以下都是管理員有權限可以使用的
  - 配送員只有新增訂單跟查看每日任務可以用
  - 客戶功能有查看自己的餘額、自己這個月的訂單，可以自己修改，最晚可以在前一天晚上6點前修改、自己的帳單可以列印出來繳
  - ![image](https://github.com/user-attachments/assets/98437666-ae71-4c6b-8526-f5f25eefb229)

- 新增訂單
  - ![image](https://github.com/user-attachments/assets/7a0deefa-e7da-4c98-a4d4-7df7a7e48e26)

- 查詢&修改訂單
  - ![image](https://github.com/user-attachments/assets/8ef92c94-ee56-41f3-9a57-f36130a0187e)
  - ![image](https://github.com/user-attachments/assets/4361f3dd-04bb-4997-ab52-0223c6cad7e3)

- 查詢客戶資料
  - 可以輸入客戶姓名或是地址或是電話對後端資料庫做查詢
  - ![image](https://github.com/user-attachments/assets/e1056960-ebaf-4e67-8e45-ff8d2e309347)
  - 有word predict的功能
  - ![image](https://github.com/user-attachments/assets/47dd4060-e8e3-48e4-b2f7-e908117be47f)


- 羊奶總數點貨
  - ![image](https://github.com/user-attachments/assets/38108cd7-57e2-4682-9405-26a8ee04eeb3)
  - ![image](https://github.com/user-attachments/assets/e746fe99-2d40-498f-bcf3-1784fc1ee025)
  - ![image](https://github.com/user-attachments/assets/2cb00cc0-e5b4-48ca-bc67-f4257c744270)

- 配送員總數
  - 盤點配送員該路線今日總瓶數以及路線，產出CSV搭配手機APP做導航
  - ![image](https://github.com/user-attachments/assets/ec198e13-d159-42ef-a43d-098e1202768f)
  - 可以下載成CSV
  - ![image](https://github.com/user-attachments/assets/4f39b661-3c8e-4b32-90cf-eb0425aa0a79)


- 配送員回報
  - 選好日期後會顯示出有回報的配送員
  - ![image](https://github.com/user-attachments/assets/e83506a4-37a0-4a8f-a9a4-d72e28125577)
  - 選好後會出現他回報的內容，也就是手機APP聊天室那邊的訊息
  - ![image](https://github.com/user-attachments/assets/b2c140ee-7aa3-4f69-9186-438e9f34786a)

- 客戶帳單查詢
  - ![image](https://github.com/user-attachments/assets/a07a219c-3051-4a82-9ad7-719c16e86c5e)

- 所有客戶帳單一覽
  - 可以顯示該路線所有人的餘額(負的表示有帳單未繳)
  - ![image](https://github.com/user-attachments/assets/de0a0243-bcc6-471a-a41d-45b394a36be0)
  - 切換成只有負的客戶，方便客服人員通知客戶
  - ![image](https://github.com/user-attachments/assets/13282e87-743a-4993-bec1-eb36ef464145)


- 對帳
  - ![image](https://github.com/user-attachments/assets/9c28eb00-8546-4859-8d59-895f92881be3)
  - 入帳
  - ![image](https://github.com/user-attachments/assets/6fdbb473-5112-4a5a-a2dc-ee23fb62701b)
  - 餘額及時更新
  - ![image](https://github.com/user-attachments/assets/525793fc-ff12-493c-873c-12972cc6b3ef)
  - 後端有更改紀錄，這邊之後會做一個前端給老闆管理
  - ![image](https://github.com/user-attachments/assets/9d375b12-ad56-44cd-99af-559f914d65db)


- 幼稚園(團戶)訂購及收費
