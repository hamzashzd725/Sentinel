from pathlib import Path
from datetime import datetime



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