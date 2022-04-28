from queue import Queue

import Pyro4

from app.logger import log_config

logger = log_config()


@Pyro4.expose
class Servidor(object):
    '''

    topics structure:
    {
        "key": list()
    }
    '''
    topics = {}

    def _get_topic(self, topic_name) -> Queue:
        return self.topics.get(topic_name, None)

    def create_topic(self, topic_name) -> bool:
        if topic_name in self.topics:
            # already exists
            return False

        self.topics[topic_name] = Queue()
        print(f"criou {topic_name}")
        return True

    def publish(self, topic_name, message) -> bool:
        queue = self._get_topic(topic_name)

        if not queue:
            self.create_topic(topic_name)

        queue = self._get_topic(topic_name)
        queue.put(message)
        print(f"message {message}")

        return True

    def subscribe(self, topic_name) -> str:
        queue = self._get_topic(topic_name)

        if not queue:
            self.create_topic(topic_name)
            print(f"create subs")
            return ""

        if queue.empty():
            print(f"empty")
            return ""

        message = queue.get()
        print(f"get {message}")

        return message

def start_server():
    Pyro4.Daemon.serveSimple(
        {
            Servidor: "Broker",
        },
        host="0.0.0.0",
        port=9090,
        ns=False,
        verbose=True,
    )
    print(f"Ready to listen")
