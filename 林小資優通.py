# 引用必要套件
import socket
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('dong-virus-firebase-adminsdk-iislp-cb5ebea9d3.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

doc = {
  '名稱':'',
  '內容': '',
  '準時':[False],
  '班規':[False,False,False],
  '作業': [False,False,False],
  '教師簽章':None
}

# 建立文件 必須給定 集合名稱 文件id
# 即使 集合一開始不存在 都可以直接使用

# 語法
# doc_ref = db.collection("集合名稱").document("文件id")

doc_ref = db.collection("回報資料").document(socket.gethostname())

# doc_ref提供一個set的方法，input必須是dictionary
doc_ref.set(doc)