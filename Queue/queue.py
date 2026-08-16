from queue import Queue


class FileQueue:

    def __init__(self):
        self.queue = Queue()

    def add(self, file):
        self.queue.put(file)
        print(f"Added to queue: {file.name}")

    def get(self):
        return self.queue.get()

    def task_done(self):
        self.queue.task_done()