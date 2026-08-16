import time
from pathlib import Path
from threading import Thread
from queue import Queue


class ReadinessChecker:

    def __init__(self, stability_time=2.0, check_interval=0.5):
        self.stability_time = stability_time
        self.check_interval = check_interval

    def wait_until_ready(self, file):
        previous_size = -1
        stable_for = 0.0

        while stable_for < self.stability_time:

            current_size = Path(file.path).stat().st_size

            if current_size == previous_size:
                stable_for += self.check_interval
            else:
                stable_for = 0.0

            previous_size = current_size

            time.sleep(self.check_interval)

        return True
    
    


class ReadinessWorker:

    def __init__(self, file_queue):
        self.file_queue = file_queue
        self.waiting_files = Queue()

        self.worker = Thread(
            target=self.process,
            daemon=True
        )

    def start(self):
        self.worker.start()

    def add(self, file):
        self.waiting_files.put(file)

    def process(self):

        while True:

            file = self.waiting_files.get()

            try:
                checker = ReadinessChecker()

                checker.wait_until_ready(file)

                print(f"Ready: {file.name}")

                self.file_queue.add(file)

            finally:
                self.waiting_files.task_done()