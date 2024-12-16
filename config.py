import os

# Configuración Bluetooth
LOCAL_MAC = " "
PEER_MAC = " "
PORT = 30

# Carpeta de sincronización
SYNC_FOLDER = "comunismo"

# Creación de carpeta de sincronización si no existe
if not os.path.exists(SYNC_FOLDER):
    os.makedirs(SYNC_FOLDER)
