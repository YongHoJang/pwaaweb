import datetime
from mongoengine import *

connect('pwaa', host='mongodb://localhost/pwaa', port=27017)

class Record(DynamicDocument):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    module_name = StringField(max_length=255, required=True) 
