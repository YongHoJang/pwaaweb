#from obserber import model
from sil import request
from models import Record

def run_weekly():
    record = Record(module_name="SIL")
    record.data = request.getRequest()
    
    record.save()