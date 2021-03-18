#writecsv.py

import csv

def WritetoCSV(data):
    with open('test.csv','a',newline='',encoding= 'utf-8') as  file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(data)
    print('Success to save file')

data = ['print() คืออะไร?' , 'คำสั่งในการแสดงผลข้อความ']
WritetoCSV(data)
