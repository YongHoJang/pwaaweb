

class SILData:
    '''
    SILData class holds values for the corresponding mongodb collection.
    '''
    
    def __init__(self, iso_code, reference_name, existing_scripture, 
        existing_scripture_dis, update_date_time):
        self.iso_code = iso_code
        self.reference_name = reference_name
        self.existing_scripture = existing_scripture
        self.existing_scripture_dis = existing_scripture_dis
        self.update_date_time = update_date_time
    
    
    @staticmethod
    def create_from_bson(bson):
        sildata = SILData(bson['iso_code'], bson['reference_name'], 
            bson['existing_scripture'], bson['existing_scripture_dis'],
            bson['update_date_time'])
        return sildata
