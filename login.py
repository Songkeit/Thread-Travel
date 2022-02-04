import tkinter as tk
from PIL import Image,ImageTk
import socket
from tkinter import messagebox

root = tk.Tk()
server_ip = socket.gethostbyname(socket.gethostname())
port = 5000
name = tk.StringVar()
#Head
root.geometry("400x400")

#image
root.option_add("*Front","consolas 20")
img = Image.open("boat.jpg")
img = img.resize((int(img.width*.1),int(img.height*.07)))
photo = ImageTk.PhotoImage(img)
lbl = tk.Label(image=photo)
lbl.pack()

def check_name():
    if len(str(name.get())) < 3 or str(name.get()) == 'admin':
        messagebox.showinfo("ชื่อไม่ถูกต้อง", "โปรดใส่ชื่อมากกว่า 2 ตัวอักษร")
    else:
        next_page()

labelNum1 = tk.Label(root, text="Enter your name").pack()
entryNum1 = tk.Entry(root, textvariable=name).pack()
btn = tk.Button(root,text="-->",height = 2,width = 7,command=check_name).pack(pady=20)

 

def next_page():
    root.destroy()
    import ThreadTravel



root.mainloop()
    


