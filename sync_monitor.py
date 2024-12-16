import time
from watchdog.observers import Observer
from sync_server import Handler
from config import SYNC_FOLDER


def start_monitor():
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, SYNC_FOLDER, recursive=True)
    observer.start()
    print(f"Nuestra Carpeta: {SYNC_FOLDER}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
