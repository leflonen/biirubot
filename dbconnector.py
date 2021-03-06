from pymongo import MongoClient

class DBConnector(object):
    def __init__(self, db_name, collection_name,
                mongo_address='mongo', mongo_port=27017,
                username='root', password='rootbiiru'):
        self._db_name = db_name
        self._collection_name = collection_name
        self._client = MongoClient(mongo_address, mongo_port,
                                   username=username, password=password)

    def get_client(self):
        return self._client

    def get_db(self):
        return self.get_client()[self._db_name]

    def get_collection(self):
        return self.get_db()[self._collection_name]
