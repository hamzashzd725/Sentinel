from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
import os


class SentinelEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        print (f"New File: {event.src_path}")
        
        
        previous_size = -1

        while True:
            try:
                current_size = os.path.getsize(event.src_path)

                if current_size == previous_size:
                    break

                previous_size = current_size
                time.sleep(1)

            except FileNotFoundError:
                time.sleep(1)

        print("File transfer finished!")
        
    
    

class SentinelWatcher:

    def __init__(self, inbox_path):
        self.inbox_path = inbox_path
        self.observer = Observer()
        self.handler = SentinelEventHandler()

    def start(self):
        self.observer.schedule(
            self.handler,
            path = self.inbox_path,
            recursive= False
        )

        self.observer.start()
    
    def stop(self):
        self.observer.stop()
        self.observer.join()



# GETTING THE INBOX DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent
current_directory = BASE_DIR / "Inbox"


# STARTING WATCHER

watcher = SentinelWatcher(current_directory)
watcher.start()
print(f"Watching: {current_directory}")


try:
    watcher.observer.join()

except KeyboardInterrupt:
    watcher.stop()