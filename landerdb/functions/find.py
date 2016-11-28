"""
{
    collections: {
        users:[
            {
                _id:5,
                firstname:"Frankie",
                username:"Omg"
            }
        ]
    }

    index: {
        users:{
            "asdkk12k123sad":0
        }
    }
}
"""


def find(dbdata, collection, data):
    if collection not in dbdata['collections']:
        return []
    if "id" in data:
        if collection in dbdata['index']:
            index = dbdata['index'][collection].get(data['id'])
            if index:
                return [dbdata['collections'][collection][index]]
        return []
    output = []
    for on in dbdata['collections'][collection]:
        for key in data:
            if key in data and key in on:
                if data[key] != on[key]:
                    break
            else:
                break
        else:
            output.append(on)
    return output

