from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .filerecord import FileRecord


class SentinelWatcher:

    def __init__(self, inbox_path, output_queue):

        self.inbox_path = inbox_path
        self.output_queue = output_queue

        self.observer = Observer()

        self.handler = SentinelEventHandler(
            self.output_queue
        )

    def start(self):

        self.observer.schedule(
            self.handler,
            path=self.inbox_path,
            recursive=False
        )

        self.observer.start()

    def stop(self):

        self.observer.stop()
        self.observer.join()


class SentinelEventHandler(FileSystemEventHandler):

    def __init__(self, output_queue):

        self.output_queue = output_queue

    def on_created(self, event):

        if event.is_directory:
            return

        file = FileRecord(
            event.src_path,
            "Created"
        )

        self.output_queue.put(file)