#!/usr/bin/env python3
from tkinter import *
import socket
import datetime 


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


window = Tk()
window.geometry("600x400")
window.resizable(width=False, height=False)
window.title("CVF_Loop")
lab = Label(window)
lab.pack()

def task():

	time = datetime.datetime.now().strftime("Last Refresh: %H:%M:%S")
	lab.config(text=time)
	window.after(30000, task)
		
	label_1 = Label(None, text=ip, width=20,font=('bold, 20'))
	label_1.place(x=-50, y=20)


	with open('file.txt', 'r') as searchfile:
		for line in searchfile:
			if 'Firmware:' in line:


					label_2 = Label(None, text=line, width=25,font=('bold, 20'))
					label_2.place(x=-50, y=60)

task()
window.mainloop()