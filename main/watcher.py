from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time


class SentinelEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        print (f"New File: {event.src_path}")
    

class SentinelWatcher:

    def __init__(self, inbox_path):
        self.inbox_path = inbox_path
        self.observer = Observer()
        self.handler = SentinelEventHandler()

    def start(self):
        self.observer.schedule(
            self.handler,
            path = self.inbox_path,
            recursive= True #changed this to make it so it checks all folders
        )

        self.observer.start()
    
    def stop(self):
        self.observer.stop()
        self.observer.join()



# GETTING THE CURRENT DIRECTORY

current_directory = Path.cwd()


# STARTING WATCHER

watcher = SentinelWatcher(current_directory)
watcher.start()
print(f"Watching: {current_directory}")


try:
    watcher.observer.join()

except KeyboardInterrupt:
    watcher.stop()