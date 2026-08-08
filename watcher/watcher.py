from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
import time
class SentinelEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        print (f"New File: {event.src_path}")

observer = Observer()

handler = SentinelEventHandler()

observer.schedule(
    handler, 
    path = "inbox",
    recursive = False
)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

        

