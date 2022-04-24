from typing import Iterator

from tinydb import TinyDB, Query

db = TinyDB("db.json")

"""
# db document structure
{
    "name": "SomethingSomething",
    "data": 
        {
            "0": dict(),
            "1": dict()
        }
}

"""


def get_all():
    return db.all()


def get_declared_queues() -> Iterator:
    for item in get_all():
        yield item["name"]


def get_queue_stats(queue_name: str):
    for item in get_all():
        yield {"name": item["name"], "count": len(item["data"])}


def get_queue(queue_name: str):
    return db.search(Query().name == queue_name)


def pop_from_queue(queue_name: str):
    return db.search(Query().name == queue_name)


def add_to_queue(queue_name: str, data: dict):
    return db.search(Query().name == queue_name)


def remove_from_queue(queue_name: str):
    return db.search(Query().name == queue_name)
