from tkinter import *
import socket
import datetime
import os

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

window = Tk()
window.geometry("600x400")
window.resizable(width=False, height=False)
window.title("CVF Loop")
lab = Label(window)
lab.pack()


Host_Label = Label(None, text = "Host: " +hostname, width=15, font=('bold, 12'))
Host_Label.place(x=300, y=30)
IP_Label = Label(None, text="IP: " +ip, width=15, font=('bold, 12'))
IP_Label.place(x=180, y=30)

    


def task():
    time = datetime.datetime.now().strftime("Last Update: %I:%M:%S:%p")
    lab.config(text=time)
    window.after(30000, task)
    

def find_driver():
    for file in os.listdir(r'C:\windows\system32\drivers'):
        if file == "bam.sys":
            return file + " found. Nvme driver detected"
       # else:
          #  return "no driver detected, check hardware."

Driver_Label = Label(None, text = find_driver(), width=30, font =('bold, 12'))
Driver_Label.place(x=10, y=60) 

     


           
find_driver()
task()
window.mainloop()
