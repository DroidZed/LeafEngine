from typing import Any
from motor.motor_asyncio import AsyncIOMotorCollection


class CrudClient[DBC]:
    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection = collection

    async def query_collection(self, payload: dict) -> list[dict] | None:
        """
        A CRUD method used to query a specific collection using the payload given in arguments.
        Args:
            payload: dict

        Returns:
                A list of documents fetched from the database. None if nothing is present.
        """

        return [c async for c in self._collection.find(payload, {"_id": 0, "__v": 0})]

    async def get_one(self, payload: dict) -> Any:
        return await self._collection.find_one(payload)

    async def insert_into_collection(self, payload: list[dict[str, Any]]) -> None:
        await self._collection.insert_many(payload)

    async def delete_from_collection(self, payload: dict) -> None:
        await self._collection.delete_many(payload)

    async def update_document(
        self,
        criteria: dict,
        payload: dict,
        upsert: bool = True,
    ) -> None:
        await self._collection.update_one(criteria, payload, upsert=upsert)
