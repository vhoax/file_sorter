from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json



class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder_to_track):
            src = folder_to_track + "/" + file
            destination = folder_destination + "/" + file
            os.rename(src, folder_destination)


folder_to_track = "C:/Users/hx/Desktop/input"
folder_destination = "C:/Users/hx/Desktop/output"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()


