import uuid
import pprint

def insert(dbdata, collection, data):
    _id = uuid.uuid4().hex
    data["id"] = _id
    if collection not in dbdata['collections']:
        dbdata['collections'][collection] = [data]
    else:
        dbdata['collections'][collection].append(data)

    if collection not in dbdata['index']:
        dbdata['index'][collection] = {
            _id: len(dbdata['collections'][collection]) - 1
        }
    else:
        dbdata['index'][collection][_id] = len(dbdata['collections'][collection]) - 1 
    return _id
