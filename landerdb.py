import json
import os

__version__ = "1.0.0"

class Connect:

    def __init__(self, db_file):
        self.db = db_file
        self.json_data = {}
        # allows find to be called multiple times, without 
        # re-reading from disk unless a change has occured
        self.stale = True
        if not os.path.exists(self.db):
           self.save()
        
    def _load(self):
        if self.stale:
            with open(self.db, 'rb') as fp:
                try:
                    self.json_data = json.load(fp)
                except:
                    with open(self.db, 'wb') as file:
                        file.write(json.dumps(self.json_data))
                    self._load()
    def save(self):
        with open(self.db, 'wb') as fp:
            json.dump(self.json_data, fp)
            self.stale = True
    
    def insert(self, collection, data):
        self._load()
        if collection not in self.json_data:
            self.json_data[collection] = []
        self.json_data[collection].append(data)

    def remove(self, collection, data):
        self._load()
        if collection not in self.json_data:
            return False
        self.json_data[collection].remove(data) #Will only delete one entry
            
    def find(self, collection, data):
        self._load()
        if collection not in self.json_data:
            return False
        output = []
        for x in self.json_data[collection]:
            if data != "all":
                yes = True
                for y in data:
                    if y not in x:
                        yes = False 
                        break
                    else:
                        if data[y] != x[y]:
                            yes = False
                            break
                if yes and x not in output:
                    output.append(x)
                    
            else:
                output.append(x)
        return output
    


