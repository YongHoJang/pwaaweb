import datetime
from flask import url_for 
from prj import db 


class TestObj(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True) 
