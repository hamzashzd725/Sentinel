from queue import Queue
from threading import Thread


class FileQueue:

    def __init__(self):
        self.queue = Queue()
        self.worker = Thread(
            target=self.process_queue,
            daemon=True
        )

    def add(self, file):
        self.queue.put(file)
        print(f"Added to queue: {file.name}")

    def start(self):
        self.worker.start()

    def process_queue(self):

        while True:

            file = self.queue.get()

            try:
                print(f"Processing: {file.name}")

            finally:
                self.queue.task_done()