# 引用必要套件

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('C:/Users/DongD/Desktop/lkge-web-firebase-adminsdk-2t4fb-fc56b022ca.json')
# C:/Users/DongD/Desktop/lkge-web-firebase-adminsdk-2t4fb-a02dfe2631.json
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

# 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用



path = "Dong Chen"
collection_ref = db.collection(path)

資料 = {'班幣': {'班幣': 45000},
        '第1周第1堂': {'教師簽章': 'xxx', '內容': '1.完成期告\n', '作業': [True, True, True], '準時': [True], '班規': [True, True, True], '名稱': '1/12 獨研'}, 
        '第1周第2堂': {'準時': [True], '名稱': '1/13 電影', '班規': [True, True, True], '教師簽章': '孫浩雲', '內容': '1.寫自評單\n2.完成劇本\n', '作業': [True, True, True]},
        '第1周第3堂': {'內容': '1.寫自評單\n\n', '教師簽章': '陳柏東', '準時': [True], '名稱': '1/12 情意', '作業': [True, True, True], '班規': [True, True, True]}, 
        '第1周第4堂': {'教師簽章': '123', '內容': '', '作業': [True, True, True], '準時': [True], '班規': [True, True, True], '名稱': ''}, 
        '第1周第5堂': {'準時': [True], '名稱': '', '班規': [True, True, True], '教師簽章': '789', '內容': '', '作業': [True, True, True]}, 
        '第1周筆記1': {'內容': '145646', '提交': False, '名稱': '課堂筆記', '標籤': '自拍電影'}, 
        '第1周筆記2': {'標籤': 'Minecraft', '提交': False, '內容': '2號筆記', '名稱': '課堂筆記'}, 
        '第1周筆記3': {'標籤':'網頁設計','名稱': '課堂筆記','提交': False,'內容':'3號筆記'},
      }

docs = collection_ref.get()
for doc in docs:
    資料[doc.id] = doc.to_dict()

print(資料)




# #語法
# #doc_ref = db.collection("集合名稱").document("文件id")
# for i in range(1,4,1):
#   doc = {
#     '內容':str(i)+'號筆記',
#     '名稱':'課堂筆記',
#     '提交':False,
#     '標籤':l[i]
#   }
#   doc_ref = db.collection("Dong Chen").document('第1周筆記'+str(i))
#   # doc_ref提供一個set的方法，input必須是dictionary
#   doc_ref.set(doc)