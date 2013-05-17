import json
import os

class Connect:

    def __init__(self, db_file):
        self.db = db_file
        if not os.path.exists(self.db):
            with open(self.db, 'wb') as file:
                file.write(json.dumps({}))

    def insert(self, collection, data):
        with open(self.db, 'rb') as file:
            json_data = json.loads(file.read())
            if collection not in json_data:
                json_data[collection] = []
            json_data[collection].append(data)
            with open(self.db, 'wb') as file:
                file.write(json.dumps(json_data))
    
    def find(self, collection, data):
        with open(self.db, 'rb') as file:
            json_data = json.loads(file.read())
            if collection not in json_data:
                return False
            output = []
            for x in json_data[collection]:
                if data != "all":
                    for y in data:
                        if data[y] == x[y]:
                            output.append(x)
                else:
                    output.append(x)
            return output
    
    def remove(self, collection, data):
        with open(self.db, 'rb') as file:
            json_data = json.loads(file.read())
            if collection not in json_data:
                return False
            json_data[collection].remove(data) #Will only delete one entry
            with open(self.db, 'wb') as file:
                file.write(json.dumps(json_data))

