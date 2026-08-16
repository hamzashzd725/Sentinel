from threading import Thread


class Dispatcher:

    def __init__(self, input_queue):

        self.input_queue = input_queue

        self.worker = Thread(
            target=self.process,
            daemon=True
        )
        
        # Routes here will be added for different file types.

        self.route = {
            # "PDF": document_extractor
        }

    def start(self):

        self.worker.start()

    def process(self):

        while True:

            file = self.input_queue.get()

            try:

                handler = self.route.get(file.extension)

                if handler is not None:
                    handler.process(file)

                else:
                    print(f"No handler for: {file.name}")

            finally:

                self.input_queue.task_done()