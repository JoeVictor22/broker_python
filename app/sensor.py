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
    monitor_types = ["temperature", "humidity", "speed"]

    """
    TODO:
    deve monitorar (temperatura, umidade ou velocidade) # select
    deve modificar valor atual da leitura # input
    deve ser possivel minimo e máximo qlqr hora # input
    ao atingir valor deve se enviar # mostrar valor atual
    """

    def __init__(
        self, name=None, topic_name=None, monitor=None, min_target=None, max_target=None
    ):
        if name is None:
            name = f"Sensor:{random.randint(0,9999)}"

        if topic_name is None:
            topic_name = "default"

        if monitor is None or monitor not in self.monitor_types:
            monitor = random.choice(self.monitor_types)

        if min_target is None:
            min_target = random.randint(0, 9999)

        if max_target is None or max_target < min_target:
            max_target = random.randint(min_target, min_target + 9999)

        self.min_target = min_target
        self.max_target = max_target
        self.monitor = monitor
        self.name = name
        self.value = 0
        self.topic_name = topic_name
        self.broker = Pyro4.core.Proxy(PYRO_URL)
        self.random = False
        self.timer = 1
        self.calls = 0

    def update(self):
        time.sleep(self.timer)
        if self.random:
            self.value = random.randint(0, 9999)

        message = (
            f"Producer: {self.name}, Topic: {self.topic_name}, Value: {self.value}"
        )

        if self.random >= self.max_target or self.random <= self.min_target:
            self.calls += 1
            self.broker.publish(self.topic_name, message)
            print(f"Enviado: {message}")

