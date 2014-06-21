import json
import os

__version__ = "1.3.0"

class Connect:

    def __init__(self, db_file, autosave = False):
        self.db = db_file
        self.json_data = {}
        # allows find to be called multiple times, without 
        # re-reading from disk unless a change has occured
        self.stale = True
        self.autosave = autosave
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
    
    def insert(self, collection, *data):
        self._load()
        if collection not in self.json_data:
            self.json_data[collection] = []
        for new in data:
            self.json_data[collection].append(new)
        if self.autosave:
            self.save()
    def update(self, collection, check, new):
        self._load()
        if collection not in self.json_data:
            return False
        for x in self.json_data[collection]:
            yes = True
            for y in check:
                if y in x and check[y] == x[y]:
                    continue
                else:
                    yes = False
                    break
            if yes:
                edited = x
                for z in new:
                    edited[z] = new[z]
                self.json_data[collection].remove(x)
                self.json_data[collection].append(edited)
            
            if self.autosave:
                self.save()
    def remove(self, collection, data):
        self._load()
        if collection not in self.json_data:
            return False
        self.json_data[collection].remove(data) #Will only delete one entry
        if self.autosave:
            self.save()

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

    def get(self, collection, key, all_=False):
        self._load()
        if collection not in self.json_data:
            return False
        out = []
        if not all_:
            for x in self.json_data[collection]:
                if key in x:
                    out.append(x[key])
        else:
            out = self.json_data[collection] 
        return out if out else False
        
    def contains(self, collection, key):
        self._load()
        if collection not in self.json_data:
            return False
        for x in self.json_data[collection]:
            if key in x:
                return True
        return False
