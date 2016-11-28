
def delete(dbdata, collection, found):
    for f in found:
        index = dbdata['index'][collection][f['id']]
        dbdata['collections'][collection].pop(index)
        del dbdata['index'][collection][f['id']]
