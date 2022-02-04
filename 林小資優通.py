# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('C:/Users/DongD/Desktop/lkge-web-firebase-adminsdk-2t4fb-a02dfe2631.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

# 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用

l = ['','Minecraft','自拍電影','網頁設計','詩婷老師']

# 語法
# doc_ref = db.collection("集合名稱").document("文件id")
for i in range(1,4,1):
  doc = {
    '內容':str(i)+'號筆記',
    '標題':'課堂筆記',
    '提交':False,
    '標籤':l[i]
  }
  doc_ref = db.collection("Dong Chen").document('第1周筆記'+str(i))
  # doc_ref提供一個set的方法，input必須是dictionary
  doc_ref.set(doc)