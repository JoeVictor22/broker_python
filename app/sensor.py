import random
import time

import Pyro4

from config import PYRO_URL


class Sensor:
    broker = None
    logger = None

    name = None
    topic_name = None
    value = None

    monitor = None
    min_target = None
    max_target = None

    calls = 0
    random = None
    timer = None
    active = None
    monitor_types = ["temperature", "humidity", "speed"]
    buffer = None

    """
    TODO:
    deve monitorar (temperatura, umidade ou velocidade) # select
    deve modificar valor atual da leitura # input
    deve ser possivel minimo e máximo qlqr hora # input
    ao atingir valor deve se enviar # mostrar valor atual
    """

    def __init__(self, name=None, topic_name=None, monitor=None):
        if name is None:
            name = f"Sensor:{random.randint(0,9999)}"

        if topic_name is None:
            topic_name = "default"

        if monitor is None or monitor not in self.monitor_types:
            monitor = random.choice(self.monitor_types)

        self.min_target = 0
        self.max_target = 10
        self.monitor = monitor
        self.name = name
        self.value = 0
        self.topic_name = topic_name
        self.broker = Pyro4.core.Proxy(PYRO_URL)
        self.random = False
        self.timer = 1
        self.calls = 0
        self.active = False
        self.buffer = list()

    def set_min(self, val):
        if val <= self.max_target:
            self.min_target = val

    def set_max(self, val):
        if val >= self.min_target:
            self.max_target = val

    def update(self):
        time.sleep(0.16)
        if self.active:
            if self.random:
                self.value = random.randint(
                    self.min_target - (self.min_target * 2),
                    self.max_target + self.max_target,
                )

            message = (
                f"Producer: {self.name}, Topic: {self.topic_name}, Value: {self.value}"
            )

            if self.value >= self.max_target or self.value <= self.min_target:
                self.calls += 1
                self.broker.publish(self.topic_name, message)
                self.insert_message(message)


    def insert_message(self, message):
        message = self.format_message(str(message))
        self.buffer.append(message)

    @staticmethod
    def format_message(message):
        from datetime import datetime

        time = datetime.now().strftime("%H:%M:%S")
        return f"[{time}] - {message}"
