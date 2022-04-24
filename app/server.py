from flask import Flask, request
import ujson

from logger import log_config

broker = Flask(__name__)
logger = log_config()

@broker.route("/pop/<queue_name>", methods=["GET"])
def pop_queue(queue_name: str):
    logger.info(f"Pop fila: {queue_name}")
    return ujson.dumps("queue")

@broker.route("/add/<queue_name>", methods=["POST"])
def add_queue(queue_name: str):
    data = request.get_json()
    logger.info(f"Recebido fila: {queue_name} - {data}")
    return ujson.dumps("queue")


if __name__ == "__main__":
    broker.run('127.0.0.1', 5000, debug=True)