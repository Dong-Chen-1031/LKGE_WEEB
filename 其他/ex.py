from openpyxl import workbook,load_workbook

wb = load_workbook("C:/Users/User/Downloads/LKGE_WEEB/其他/林小資優通 (回覆).xlsx")

ws = wb.active



for i in range(2,4,1):
    print(str(i)+'：'+ws['B'+str(i)].value+' - '+ws['c'+str(i)].value)