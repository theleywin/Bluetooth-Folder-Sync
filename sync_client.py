import os
import socket


def send_file(filepath, peer_mac, port):
    if not os.path.exists(filepath):
        print("El archivo especificado no existe.")
        return

    filesize = os.path.getsize(filepath)
    filename = os.path.basename(filepath)
    metadata = f"CREATE::{filename}::{filesize}"

    with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as sock:
        sock.connect((peer_mac, port))
        sock.send(metadata.encode())

        with open(filepath, "rb") as f:
            while chunk := f.read(1024):
                sock.send(chunk)

    print(f"Se envió: {filename}")


def send_delete_notification(filename, peer_mac, port):
    metadata = f"DELETE::{filename}::0"

    with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as sock:
        sock.connect((peer_mac, port))
        sock.send(metadata.encode())

    print(f"Se eliminó: {filename}")
