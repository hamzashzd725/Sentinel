from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from threading import Thread
from pathlib import Path 
from datetime import datetime
from .logger import Filelogger #temp
from .readiness import ReadinessChecker


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

        thread = Thread(
            target=self.process_file,
            args=(file,)
        )

        thread.start()

    def process_file(self, file):

        print(f"Started processing: {file.name}")
        checker = ReadinessChecker()

        checker.wait_until_ready(file)

        print(f"Finished waiting: {file.name}")

        logger = Filelogger("sentinel.txt")

        logger.log_file(file)

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

    def display(self):

        print(f"""
            Path: {self.path}
            Filename: {self.name}
            Extension: {self.extension}
            Size: {self.size} bytes
            Timestamp: {self.timestamp.strftime("%d-%m-%Y %H:%M:%S")}
            Event: {self.event}
            """)