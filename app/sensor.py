import random
import time

import Pyro4

from app.logger import log_config
from config import PYRO_URL


class Sensor:
    broker = None
    logger = None

    name = None
    topic_name = None
    value = None

    """
    TODO:
    deve monitorar (temperatura, umidade ou velocidade)
    deve modificar valor atual da leitura
    deve ser possivel minimo e máximo qlqr hora
    ao atingir valor deve se enviar
    """

    def __init__(self, name=None, topic_name=None):
        if name is None:
            name = f"Sensor:{random.randint(0,9999)}"

        if topic_name is None:
            topic_name = "default"

        self.name = name
        self.value = random.randint(0, 400)
        self.topic_name = topic_name
        self.broker = Pyro4.core.Proxy(PYRO_URL)
        self.logger = log_config()

    def start(self):
        self.logger.info("Iniciando sensor")
        self.create_gui()

        while True:
            time.sleep(1)
            self.value = random.randint(0, 400)
            message = (
                f"Producer: {self.name}, Topic: {self.topic_name}, Value: {self.value}"
            )
            self.broker.publish(self.topic_name, message)
            print(f"Enviado: {message}")

    def create_gui(self):
        self.logger.info("Iniciando interface")
