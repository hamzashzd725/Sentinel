from threading import Thread
from .readiness import ReadinessChecker


class ReadinessWorker:

    def __init__(self, input_queue, output_queue):

        self.input_queue = input_queue
        self.output_queue = output_queue

        self.checker = ReadinessChecker()

        self.worker = Thread(
            target=self.process,
            daemon=True
        )

    def start(self):

        self.worker.start()

    def process(self):

        while True:

            file = self.input_queue.get()

            try:

                self.checker.wait_until_ready(file)

                print(f"Ready: {file.name}")

                self.output_queue.put(file)
                

            finally:

                self.input_queue.task_done()