import cPickle
import os
import shutil
from functions import *

class LanderDB:
    def __init__(self, dbname, autosave=True):
        self.autosave = autosave
        if not dbname.endswith(".db"):
            dbname = dbname + ".db"
        if os.path.exists(dbname + ".lock"):
            raise Exception("The DB is locked. Please remove the {}.lock file".format(dbname))
        self.dbname = dbname
        if os.path.exists(dbname):
            try:
                self.databaseData = cPickle.load(open(dbname))
            except Exception as e:
                raise Exception("Could not connect to database {}. DB file might be corrupted. {}".format(dbname, e))
        else:
            self.databaseData = {
                "collections":{},
                "index":{}
            }
            self.save()

    def save(self):
        while os.path.exists(self.dbname + ".lock"):
            pass
        open(self.dbname + ".lock", 'w')
        if not os.path.exists(self.dbname):
            open(self.dbname, 'w').write("{}")
        try:
            cPickle.dump(self.databaseData, open(self.dbname, 'w'), protocol=cPickle.HIGHEST_PROTOCOL)
        except Exception as e:
            os.remove(self.dbname + ".lock")
            raise Exception("There was an error writing data to the database: {}".format(e))
        os.remove(self.dbname + ".lock")

    def find(self, collection, data):
        return find.find(self.databaseData, collection, data)

    def insert(self, collection, data):
        insert.insert(self.databaseData, collection, data)
        if self.autosave:
            self.save()

    def delete(self, collection, data):
        found = self.find(collection, data)
        if found:
            delete.delete(self.databaseData, collection, found)
        if self.autosave:
            self.save()

