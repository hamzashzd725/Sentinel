import time
from watcher import SentinelWatcher

watcher = SentinelWatcher("inbox")

watcher.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watcher.stop()
