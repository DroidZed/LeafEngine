from leaf_engine.utils._singleton import SingletonClass
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBConnection(metaclass=SingletonClass):
    def __init__(self, uri: str, db_name: str) -> None:
        self.__db_connection = AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000)[
            db_name
        ]

    @property
    def connection(self):
        return self.__db_connection
