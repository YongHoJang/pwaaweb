from models import *

# get latest SIL Dataset from collection 'record'
def retrive():
    c = Record._get_collection().aggregate([
            {'$sort':
                {'created_at':-1}
            },
            {'$limit': 1},
            {'$unwind':'$data.items'},
            {'$project': 
                {'item':'$data.items', '_id':0}
            }
        ])
    
    return c;


# test code and example for handling SIL Dataset
def print_code():
    cursor = retrive()
    for c in cursor['result']:
        print c['item']['iso_code']
        
def list_size():
    cursor = retrive()
    print len(cursor['result'])