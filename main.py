import threading
from sync_server import start_server
from sync_monitor import start_monitor
from config import LOCAL_MAC, PORT

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server, args=(LOCAL_MAC, PORT))
    server_thread.daemon = True
    server_thread.start()

    start_monitor()
