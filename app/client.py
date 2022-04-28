import random
import time

import Pyro4

from app.logger import log_config
from config import PYRO_URL


class Client:
    broker = None
    logger = None

    name = None
    topics = None

    """
    TODO:
    trabalhar com lista de topicos ao inves de topico fixo
    listar topicos
    assinar mais de um topico
    mostrar quais  mensagens chegaram
    """

    def __init__(self, name=None):
        if name is None:
            name = f"Cliente:{random.randint(0,9999)}"

        self.topics = list()
        self.name = name
        self.value = random.randint(0, 400)
        self.broker = Pyro4.core.Proxy(PYRO_URL)
        self.logger = log_config()

    def start(self):
        self.logger.info("Iniciando cliente")
        self.create_gui()

        while True:
            time.sleep(1)

            for topic in self.topics:
                message = self.broker.subscribe(topic)
                print(f"Recebido - Topico: {topic}, Message: {message}")

    def create_gui(self):
        self.logger.info("Iniciando interface")
