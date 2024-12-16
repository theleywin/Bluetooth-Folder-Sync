import socket
import os
from config import SYNC_FOLDER, PEER_MAC, PORT
from watchdog.events import FileSystemEventHandler
from sync_client import send_file, send_delete_notification

is_syncing = False
is_receiving = False 


def start_server(local_mac, port):
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    sock.bind((local_mac, port))
    sock.listen(1)

    print("Todo en talla")

    while True:
        client_sock, address = sock.accept()
        print(f"Conexión aceptada de {address[0]}")

        metadata = client_sock.recv(1024).decode()
        operation, filename, filesize = metadata.split("::")
        filesize = int(filesize)

        if operation == "DELETE":
            filepath = os.path.join(SYNC_FOLDER, filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"Archivo eliminado: {filename}")
        else:
            global is_receiving
            is_receiving = True
            print(f"Recibiendo archivo: {filename} ({filesize} bytes)")
            with open(os.path.join(SYNC_FOLDER, filename), "wb") as f:
                received = 0
                while received < filesize:
                    data = client_sock.recv(1024)
                    f.write(data)
                    received += len(data)
            print(f"Archivo recibido correctamente: {filename}")
            is_receiving = False

        client_sock.close()


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        global is_syncing, is_receiving
        if not event.is_directory and not is_syncing and not is_receiving:
            is_syncing = True
            send_file(event.src_path, PEER_MAC, PORT)
            is_syncing = False

    def on_deleted(self, event):
        global is_syncing, is_receiving
        if not event.is_directory and not is_syncing and not is_receiving:
            is_syncing = True
            send_delete_notification(os.path.basename(event.src_path), PEER_MAC, PORT)
            is_syncing = False

    def on_modified(self, event):
        global is_syncing, is_receiving
        if not event.is_directory and not is_syncing and not is_receiving:
            is_syncing = True
            send_file(event.src_path, PEER_MAC, PORT)
            is_syncing = False