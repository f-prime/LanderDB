import json
import os
import bson

class Connect:

    def __init__(self, db_file):
        self.db = db_file
        self.b = bson.BSON()
        if not os.path.exists(self.db):
            with open(self.db, 'wb') as file:
                file.write(self.b.encode({'':''}))

    def insert(self, collection, data):
        with open(self.db, 'rb') as file:
            json_data = bson.decode_all(file.read())[0]
            if collection not in json_data:
                json_data[collection] = []
            json_data[collection].append(data)
            with open(self.db, 'wb') as file:
                file.write(self.b.encode(json_data))
    
    def find(self, collection, data):
        with open(self.db, 'rb') as file:
            json_data = bson.decode_all(file.read())[0]
            if collection not in json_data:
                return False
            output = []
            for x in json_data[collection]:
                for y in data:
                    if data[y] == x[y]:
                        output.append(x)
            return output
    
    def remove(self, collection, data):
        with open(self.db, 'rb') as file:
            json_data = bson.decode_all(file.read())[0]
            if collection not in json_data:
                return False
            json_data[collection].remove(data) #Will only delete one entry
            with open(self.db, 'wb') as file:
                file.write(self.b.encode(json_data))
