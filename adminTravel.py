from tkinter import *
from tkinter import messagebox
import socket
from functools import partial


app = Tk()
server_ip = socket.gethostbyname(socket.gethostname())
port = 5000

f1 = Frame(app)
f1.grid(row=0, column=0)
f2 = Frame(app)
f2.grid(row=1, column=0)


def settingApp():
    app.title('Admin')

def admin():
    button = Button(f1,text='admin', bg = 'cyan', height = 8,state=DISABLED, borderwidth = 0,width = 45).pack()

def seat():
    seat_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    for i, c in enumerate(seat_list):
        Button(f2, text = c, height = 5, width = 6, bg = 'lightblue', command = partial(seat_queue, c)).grid(row = i//5, column = i%5, padx = 5, pady = 5)

def seat_queue(c):
    import admin
    data = str(admin.name_admin.get())+ ',' +str(c)
    
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.connect((server_ip, port))

        server.send(data.encode('utf-8'))

        data_server = server.recv(1024).decode('utf-8')

        data_server = str(data_server)

        if len(data_server) > 0:
            messagebox_notify(data_server)
            break

        server.close()
        
def messagebox_notify(data_server):
    if data_server == 'success':
        messagebox.showinfo(f'{data_server}',f'{data_server}ful')
    else:
        messagebox.showinfo(f'ที่นั่งไม่ว่าง',f'มีคนจองแล้ว')
    
def ending():
    app.mainloop()

settingApp()
admin()
seat()
ending()
