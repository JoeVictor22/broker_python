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
    broker_topics = None
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
        self.broker_topics = list()
        self.logger = log_config()

    def set_topics(self, new_topics):
        self.topics = new_topics

    def update(self):
        self.broker_topics = self.broker.get_topics()
        print(f"a {self.broker_topics}")
        for topic in self.topics:
            message = self.broker.subscribe(topic)
            print(f"Recebido - Topico: {topic}, Message: {message}")
