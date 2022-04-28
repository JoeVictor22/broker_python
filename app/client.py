import random
import time

import Pyro4

from app.logger import log_config
from config import PYRO_URL


class Client:
    broker = None
    logger = None

    name = None
    topic_name = None


    '''
    TODO:
    listar topicos
    assinar mais de um topico
    mostrar quais  mensagens chegaram
    '''

    def __init__(self, name=None, topic_name=None):
        if name is None:
            name = f"Cliente:{random.randint(0,9999)}"

        if topic_name is None:
            topic_name = "default"

        self.name = name
        self.value = random.randint(0, 400)
        self.topic_name = topic_name
        self.broker = Pyro4.core.Proxy(PYRO_URL)
        self.logger = log_config()

    def start(self):
        self.logger.info("Iniciando cliente")
        self.create_gui()

        while True:
            time.sleep(1)

            message = self.broker.subscribe(self.topic_name)
            print(f"Recebido - Topico: {self.topic_name}, Message: {message}")

    def create_gui(self):
        self.logger.info("Iniciando interface")
