from motor.motor_asyncio import AsyncIOMotorClient


class Skeleton:
    def __init__(self, db_url: str, db_name: str):
        self.__db_instance = AsyncIOMotorClient(db_url)[db_name]
