from tkinter import *

 
root = Tk()
root.option_add("*Font", "consolas 20")
f1 = Frame(root, bg="green")
f1.grid(row=0, column=0)
f2 = Frame(root, bg="red")
f2.grid(row=1, column=0)
 
Label(f1, text="Thank you", width=20).pack(padx=10, pady=10)
Label(f2, text="คุณได้ทำการจองเรียบร้อยแล้ว", width=20).pack(padx=10, pady=10)

root.mainloop()
