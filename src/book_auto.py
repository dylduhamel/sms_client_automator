import xlrd
import os
from twilio.rest import Client
from client import clientInfo

loc = "/Users/dylanduhamel/CODE/VSCodeProjects/Python/Book_Automator/src/3.xls"
clientList = []

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for i in range(2, sheet.nrows -4, 2):
     name = sheet.cell_value(i, 0).lower()
     bookID = sheet.cell_value(i + 1, 0).lower()
     balance = int(sheet.cell_value(i, 12))
     clientList.append(clientInfo(bookID, name, balance))

for obj in clientList:
     print(obj.messageFormat())

# client = Client("AC2a01d84e68aa71949fc83eccd0aaa546", "953fd2f2c3004dff70f128fc5ebab45f")

# message = client.messages \
#                 .create(
#                      body=clientList[13].messageFormat(),
#                      from_='+12546153182',
#                      to='+15719699225'
#                  )