import os
print(os.listdir())  # เป็นการเช็คสว่ามี ไฟล์อะไรบ้างใน floder นี้

import csv

def ReadCSV():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr=csv.reader(file)
        data = list(fr)
    #print(data)
    return data # คือการส่งข้อมูลไปใช้งานต่อ

ReadCSV()

alldata = ReadCSV()
print(alldata)

for dt in alldata:
    print(dt[1])
