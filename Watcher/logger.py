from pathlib import Path


class Filelogger:

    def __init__(self, log_path):
        self.log_path = Path(log_path)

    def log_file(self, file):

        with open(self.log_path, "a") as log:

            log.write(f"""
Path: {file.path}
Filename: {file.name}
Extension: {file.extension}
Size: {file.size} bytes
Timestamp: {file.timestamp.strftime("%d-%m-%Y %H:%M:%S")}
Event: {file.event}
------------------------------
""")