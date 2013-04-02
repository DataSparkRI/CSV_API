from pymongo import MongoClient
from csv import DictReader
from datetime import datetime

class Doink:
    def __init__(self, database, collection):
        self.database = database
        connection = MongoClient()
        self.collection = connection[database][collection]
        self.metadata = self.collection.find_one({'metadata': True})

class Doinker:
    def __init__(self, csv_path, database):
        self.csv_path = csv_path
        self.database = database
        self.connection = MongoClient()
        self.metadata = self.create_metadata()

    def set_collection(self, collection):
        self.metadata['collection'] = collection

    def set_description(self, description):
        self.metadata['collection'] = description

    def generate_rows(self):
        csv_file = open(self.csv_path, 'r')
        dict_reader = DictReader(csv_file)
        for row_dict in dict_reader:
            yield row_dict
        csv_file.close()

    def get_schema(self):
        for row in self.generate_rows():
            return row.keys()

    def create_metadata(self):
        row = {
            'metadata': True,
            'schema': {},
            'description': '',
            'last_modified': None
        }
        metadata = {
            'row': row,
            'row_id': None,
            'collection': ''
        }
        for field in self.get_schema():
            metadata['row']['schema'][field] = ''
        return metadata

    def insert_data(self):
        collection = self.connection[self.database][self.metadata['collection']]
        self.metadata['row_id'] = collection.insert(self.metadata['row'])
        for row in self.generate_rows():
            collection.insert(row)
        collection.update({'_id': self.metadata['row_id']}, {'$set': {'last_modified': datetime.utcnow()}})

    def __del__(self):
        self.connection.disconnect()
