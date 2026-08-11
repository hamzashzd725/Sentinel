import time
from watcher import SentinelWatcher
from pathlib import Path
from watcher import FileRecord



# GETTING THE INBOX DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent
current_directory = BASE_DIR / "Inbox"


watcher = SentinelWatcher(current_directory)

watcher.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watcher.stop()




