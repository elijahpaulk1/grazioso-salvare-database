from pymongo import MongoClient

class MongoCRUD(object):
    """ CRUD operations for MongoDB """

    def __init__(self, user, password, host, port, db_name, collection_name):
        """ Initialize MongoDB connection """
        self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/{db_name}')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        """ Insert a document into the specified collection """
        try:
            if data:
                self.collection.insert_one(data)
                return True
            else:
                raise ValueError("No data provided to insert")
        except Exception as e:
            print(f"Error during insertion: {e}")
            return False

    def read(self, query):
        """ Query documents from the specified collection """
        try:
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print(f"Error during query: {e}")
            return []

    def update(self, query, update_data):
        """ Update documents in the specified collection """
        try:
            if query and update_data:
                self.collection.update_many(query, {"$set": update_data})
                return True
            else:
                raise ValueError("No query or update data provided")
        except Exception as e:
            print(f"Error during update: {e}")
            return False

    def delete(self, query):
        """ Delete documents from the specified collection """
        try:
            if query:
                self.collection.delete_many(query)
                return True
            else:
                raise ValueError("No query provided")
        except Exception as e:
            print(f"Error during deletion: {e}")
            return False