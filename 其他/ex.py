from openpyxl import workbook,load_workbook

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('D:/啟用工具/lkge-web-firebase-adminsdk-2t4fb-3d6bd5431a.json')
# C:/Users/DongD/Desktop/lkge-web-firebase-adminsdk-2t4fb-a02dfe2631.json
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

wb = load_workbook("C:/Users/User/Downloads/LKGE_WEEB/其他/林小資優通 (回覆).xlsx")

ws = wb.active



for i in range(2,4,1):
    print(str(i)+'：'+ws['B'+str(i)].value+' - '+ws['c'+str(i)].value+' - '+ws['D'+str(i)].value)
    path = "目錄/學生"
    doc_ref = db.document(path)
    doc = {ws['D'+str(i)].value:ws['C'+str(i)].value}
    doc_ref.update(doc)