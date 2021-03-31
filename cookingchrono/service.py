from os import environ
from time import sleep

from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer
from plyer import notification


class CountDownTime:
    def __init__(self, duration):
        self.duration = duration
        self.running = True
        self.client = OSCClient(b"localhost", 3002)
        self.server = OSCThreadServer()
        self.server.listen(address=b"localhost", port=3000, default=True)
        self.server.bind(b"/pause", self.pause)

    def count_down(self):
        while self.running:
            sleep(1)
            self.duration -= 1
            self.client.send_message(
                b"/count_down",
                [str(self.duration).encode("utf8")],
            )

    def pause(self):
        self.running = not self.running
        self.count_down()


if __name__ == "__main__":
    try:
        cdt = CountDownTime(int(environ.get("PYTHON_SERVICE_ARGUMENT", "")))
        cdt.count_down()
    except Exception as e:
        notification.notify(title="error", message=e)
