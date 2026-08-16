import time
from pathlib import Path


class ReadinessChecker:

    def __init__(
        self,
        stability_time=2.0,
        check_interval=0.5
    ):

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