"""
c_db_handler for handling MongoDB databases
"""

from pymongo import MongoClient

class c_db_handler:
    """
    Class for reading and writing to MongoDB database
    """

    def __init__(self):
        self._mongo_host = "localhost"
        self._mongo_port = 27017
        self._mongo_username = "root"
        self._mongo_password = "pswrd"

        self._client = None

    def __del__(self):
        self._client.close()

    @property
    def client(self)->MongoClient:
        return self._client

    @client.setter
    def client(self, value:MongoClient):
        self._client = value

    @property
    def mongo_host(self)->str:
        return self._mongo_host
    
    @property
    def mongo_port(self)->str:
        return self._mongo_port

    @property
    def mongo_username(self)->str:
        return self._mongo_username
    
    @property
    def mongo_password(self)->str:
        return self._mongo_password

    def connect(self)->bool:
        """
        Connect to MongoDB database and initialize MongoClient. Return True on succes, False otherwise.
        """

        # Connection URL
        #connection_url = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/{database_name}"
        connection_url = f"mongodb://{self.mongo_username}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}"

        # Connect to MongoDB
        self.client = MongoClient(connection_url, connect=True)

        # Test connection
        try:
            self.client.server_info()
            print(f"Connection to database succeeded: {self.mongo_host}:{self.mongo_port}")
        except Exception as e:
            print(f"Connection to database failed: {self.mongo_host}:{self.mongo_port}")
            print(e)
            return False
        
        return True

    def write_to_collection(self, database_name: str, collection_name: str, document: dict)->bool:
        """
        Write a document to a collection in the database.
        """
        try:
            # Access the specified collection and insert the document
            db = self.client[database_name]
            collection = db[collection_name]
            result = collection.insert_one(document)
            print(f"Document inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Failed to write document to collection. Error: {e}")
            return False
        
        return True

    def get_collection(self, database_name: str, collection_name: str)->dict:
        """
        Read and return the entire collection as a nested dictionary. Return None on failure.
        """
        try:
            collection = self.client[database_name][collection_name]
            cursor = collection.find()
            return list(cursor)  # Convert cursor to a list of dictionaries
        except Exception as e:
            print(f"Failed to read collection. Error: {e}")
            return None

    def find_document_by_key_value(self, database_name: str, collection_name: str, key: str, value: str)->dict:
        """
        Find a document in the collection by a specific key and value.
        Returns the document if found, otherwise returns None.
        """
        try:
            collection = self.client[database_name][collection_name]
            query = {key: value}
            document = collection.find_one(query)
            return document
        except Exception as e:
            print(f"Failed to find document. Error: {e}")
            return None

    def remove_document_by_key_value(self, database_name: str, collection_name: str, key: str, value: str)->bool:
        """
        Remove a document from the collection based on a specific key and value.
        Returns True on succes, otherwise False.
        """
        try:
            collection = self.client[database_name][collection_name]
            query = {key: value}
            result = collection.delete_one(query)
            
            if result.deleted_count > 0:
                print(f"Document with {key}={value} removed successfully.")
                return True
            else:
                print(f"No document found with {key}={value}. Nothing removed.")
                return False
        except Exception as e:
            print(f"Failed to remove document. Error: {e}")
            return False
        
    def remove_collection(self, database_name: str, collection_name: str)->bool:
        """
        Delete a collection from the database.
        Returns True if the collection is deleted, otherwise returns False.
        """
        try:
            self.client[database_name][collection_name].drop()
            print(f"Collection {collection_name} deleted successfully.")
            return True
        except Exception as e:
            print(f"Failed to delete collection. Error: {e}")
            return False

    def remove_database(self, database_name: str)->bool:
        """
        Delete the entire database.
        Returns True if the database is deleted, otherwise returns False.
        """
        try:
            self.client.drop_database(database_name)
            print(f"Database {database_name} deleted successfully.")
            return True
        except Exception as e:
            print(f"Failed to delete database. Error: {e}")
            return False

if __name__ == "__main__":
    
    db = c_db_handler()
    db.connect()