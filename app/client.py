import random

import Pyro4

from config import PYRO_URL


class Client:
    broker = None

    name = None
    topics = None
    broker_topics = None
    buffer = None

    def __init__(self, name=None):
        if name is None:
            name = f"Cliente:{random.randint(0,9999)}"

        self.buffer = list()
        self.insert_message("Iniciando cliente")
        self.topics = list()
        self.name = name
        self.value = random.randint(0, 400)
        self.broker = Pyro4.core.Proxy(PYRO_URL)
        self.broker_topics = list()

    def set_topics(self, new_topics):
        self.topics = new_topics

    def update(self):
        self.broker_topics = self.broker.get_topics()
        for topic in self.topics:
            message = self.broker.subscribe(topic)
            if message and message != "":
                message = f"{topic} - {message}"
                self.insert_message(message)

    def insert_message(self, message):
        message = self.format_message(str(message))
        self.buffer.append(message)

    @staticmethod
    def format_message(message):
        from datetime import datetime

        time = datetime.now().strftime("%H:%M:%S")
        return f"[{time}] - {message}"
