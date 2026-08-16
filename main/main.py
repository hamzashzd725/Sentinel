import time
from pathlib import Path

from Watcher.watcher import SentinelWatcher
from Queue.queue import FileQueue
from Queue.readiness_worker import ReadinessWorker
from dispatcher.dispatcher import Dispatcher


BASE_DIR = Path(__file__).resolve().parent.parent
current_directory = BASE_DIR / "Inbox"


detection_queue = FileQueue()

ready_queue = FileQueue()


readiness_worker = ReadinessWorker(
    detection_queue,
    ready_queue
)


watcher = SentinelWatcher(
    current_directory,
    detection_queue
)

dispatcher = Dispatcher(
    ready_queue
)


readiness_worker.start()

watcher.start()
dispatcher.start()


try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    watcher.stop()