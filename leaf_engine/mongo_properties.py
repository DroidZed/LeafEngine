from attrs import define


@define
class MongoProperties:
    uri: str
    db_name: str


# TODO: add more when needed
