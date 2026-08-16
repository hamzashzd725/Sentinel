from queue import Queue


class FileQueue:

    def __init__(self):
        self.queue = Queue()

    def put(self, file):
        self.queue.put(file)

    def get(self):
        return self.queue.get()

    def task_done(self):
        self.queue.task_done()