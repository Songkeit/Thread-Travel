import tkinter as tk
from PIL import Image,ImageTk
import socket
from tkinter import messagebox

root = tk.Tk()
server_ip = socket.gethostbyname(socket.gethostname())
port = 5000
name_admin = tk.StringVar()
#Head
root.geometry("400x400")

#image
root.option_add("*Front","consolas 20")
img = Image.open("boat.jpg")
img = img.resize((int(img.width*.1),int(img.height*.07)))
photo = ImageTk.PhotoImage(img)
lbl = tk.Label(image=photo)
lbl.pack()

#inputData
def inputData():
    labelNum1 = tk.Label(root, text="Enter your name").pack()
    entryNum1 = tk.Entry(root, textvariable=name_admin).pack()
    btn = tk.Button(root,text="-->",height = 2,width = 7,command=check_name).pack(pady=20)

def check_name():
    if len(str(name_admin.get())) < 3:
        messagebox.showinfo("ชื่อไม่ถูกต้อง", "โปรดใส่ชื่อมากกว่า 2 ตัวอักษร")
    else:
        next_page()   

def next_page():
    root.destroy()
    import adminTravel

#ending
def ending():
    root.mainloop()
    
inputData()
ending()
