import threading

def admin_interface():
    import admin

def host():
    import server
    server.server()

def start_server():
    server = threading.Thread(target=host)
    server.start()

def start_admin():
    admin = threading.Thread(target=admin_interface)
    admin.start()
    
start_admin()
start_server()
