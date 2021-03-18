from tkinter import *
from tkinter import ttk
import csv

def WritetoCSV(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw =csv.writer(file)
		fw.writerow(data)
	print('Success to save file')


GUI = Tk()
GUI.title('Program a note')
GUI.geometry('500x500')

FONT1 = ('Ansana New', 20, 'bold')
FONT2 = ('Ansana New', 20)

L1 = ttk.Label(GUI,text='Title', font=FONT1, foreground='Green')
L1.pack()

v_title = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_title, font=FONT2, width=30)
E1.pack()

L2 = ttk.Label(GUI,text='Detail',font=FONT1,foreground='blue')
L2.pack()

v_detail = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_detail,font=FONT2, width=40)
E2.pack()

def SaveButton(event=None):
	title=v_title.get()
	detail =v_detail.get()
	print(title)
	print(detail)
	dt = [title,detail]
	WritetoCSV(dt)
	print('Wait a minute........')
	v_title.set('')
	v_detail.set('')
	E1.focus()

E2.bind('<Return>',SaveButton)
E2.bind('<Control-s>',SaveButton)
B1 = ttk.Button(GUI,text='SAVE',command=SaveButton)
B1.pack(ipadx=20, ipady=20, pady=20)

GUI.mainloop()
