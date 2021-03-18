from tkinter import *
from tkinter import ttk #ttk is theme of tk
import csv

#### Add to csv file
def WritetoCSV(data):
    with open('data.csv','a',newline='',encoding= 'utf-8') as  file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(data)
    print('Success to save file')
    
# เครื่องหมาย comment

# Main Program
GUI = Tk() #Tk() คือหน้าจอหลักโปรแกรม
GUI.title('Summary to learn')
GUI.geometry('700x700') #500 = กว้าง , 300 = สูง


#### Font
FONT1 = ('Angsana New', 20, 'bold') #'Angsana New'ขนาด 20 เป็นตัวหนา
FONT2 = ('Angsana New', 20) # 'Angsana New' ขนาด 20


#### Title
L1 = ttk.Label(GUI,text='หัวข้อ', font=FONT1, foreground='green') #Font1 ค่าที่เป็นdefault เป็น global variable
L1.pack() #นำ L1 ไปติดกับโปรแกรมหลัก

#### Text box 1
v_title = StringVar() # StringVar() เป็นตัวแปรพิเศษ ไว้เก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI, textvariable=v_title, font = FONT2, width=30) # Entry  ช่องกรอบ
E1.pack()            # textvariable=v_title เอาช่องกรอบไปผูกกับ v_title



#### Detail
L2 = ttk.Label(GUI,text= 'รายละเอียด', font=FONT1, foreground='green') # เพิ่มสี สามรถใส่ background='blue' ได้แต่ไม่สวยจารย์เลยใส่  foreground = 'blue' 
L2.pack()

#### Text box 2
v_detail = StringVar()
E2 = ttk.Entry(GUI, textvariable=v_detail, font=FONT2, width=40)
E2.pack()


#### Button Save                
def SaveButton(event=None): # event=None คือพิมพ์เสร็จแล้วกด enter มันจะส่งevent ไปที่ function เราจะต้องใส่ eventให้มันส่งข้อมูลเข้าไป None ใส่เวลาเรากดปุ่มไม่ใส่เกิด Error ****ถ้าปุ่มธรรมดาก็ไม่ต้องใส่
    title=v_title.get()
    detail = v_detail.get() # .get() ดึงข้อมูลจากตัวแปร v_title  โดย.get() ใช้ได้กับ StringVar() เท่านั้น
    print(title)
    print(detail)
    dt = [title,detail] # dt = data list เพราะจะเอาข้อมูลไปใส่
    WritetoCSV(dt)
    print('กำลังบันทึกข้อมูล... ..')
    #clear ข้อมูล
    v_title.set('') # สั่งเคลียร์ข้อมูลให้ว่าง
    v_detail.set('') # สั่งเคลียร์ข้อมูลให้ว่าง
    E1.focus()   # clear เสร็จให้ cursor มาอยู่ที่ E1ช่องกรอบแรก


E2.bind('<Return>',SaveButton)    #อยากให้ กด save ด้วยการ enter ได้ E2 
# E2.bind() เช็คในช่องกรอกที่ 2 ว่ามีปุ่ม Enter หรือไม่ หากกดให้ทำการเรียกฟังก์ชัน SaveButton
E2.bind('<Control-s>',SaveButton)  #อยากให้ กด save ด้วยการ ctrl+s
B1 = ttk.Button(GUI,text='SAVE',command=SaveButton)  #commandเชื่อมกับFunction SaveButton       
B1.pack(ipadx=20, ipady=20, pady=20)  #ปรับขนาดปุ่ม
# ipadx = ระยะห่างภายในปุ่มแนวแกน x
# ipady = ระยะห่างด้านนอกปุ่ม ทั้งบนและล่างแนวแกน y


# table
header = ['Title','Detail'] # เป็นexel เปล่าๆ ชื่อหัวข้อ
table = ttk.Treeview(GUI,height=10,column=header, show='headings') #table ตารางหลักที่แสดงข้อมูล
table.place(x=20,y=300) #.pack()เอาปุ่มไปใส่ในGUIหลัก 


table.heading('Title',text='หัวข้อ') #show คำว่าหัวข้อที่column Title
table.column('Title',width=200)     #ปรับความกว้าง
table.heading('Detail',text='รายละเอียด') #show คำว่ารายละเอียดที่ column Detail
table.column('Detail',width=460)

# ทดลอง insert ข้อมูลลงไป
row = ['GUI คืออะไร?','GUI : Graphical User Interface'] # Arow1 | B1 ลักษณะการใส่ๆเป็นชุดๆไป
table.insert('','end',value=row) # การสร้างcolumnปกติจะใส่เป็น number ไป / endเป็นการบอกว่าให้ใส่เข้าไปท้ายสุด


row = ['.insert()','คือการใส่ข้อมูลเข้าไป'] # Arow1 | B1 ลักษณะการใส่ๆเป็นชุดๆไป
table.insert('',1,value=row)







GUI.mainloop()
#GUI.mainloop() จากGUIจะทำให้โปรแกรมันตลอด
