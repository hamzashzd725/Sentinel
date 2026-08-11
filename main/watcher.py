from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from pathlib import Path 
from datetime import datetime
from logger import Filelogger #temp
import time
import os




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



class SentinelEventHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        file = FileRecord(
            event.src_path,
            "Created"
        )

        file.wait_until_finished()
        
        
        logger = Filelogger("sentinel.txt") #temp
        logger.log_file(file) #temp

        file.display()

#creates the filerecord which will be further used
class FileRecord:

    def __init__(self, file_path, event_type):
        self.path = Path(file_path)
        self.event = event_type

        self.name = self.path.name
        self.extension = self.path.suffix.lstrip(".").upper()
        self.timestamp = datetime.now()

        self.size = self.path.stat().st_size

    def wait_until_finished(self):

        previous_size = -1
        stable_checks = 0

        while stable_checks < 3:

            current_size = self.path.stat().st_size

            if current_size == previous_size:
                stable_checks += 1
            else:
                stable_checks = 0

            previous_size = current_size

            time.sleep(1)

        self.size = self.path.stat().st_size

    def display(self):

        print(f"""
            Path: {self.path}
            Filename: {self.name}
            Extension: {self.extension}
            Size: {self.size} bytes
            Timestamp: {self.timestamp.strftime("%d-%m-%Y %H:%M:%S")}
            Event: {self.event}
            """)