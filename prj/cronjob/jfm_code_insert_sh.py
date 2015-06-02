########################################################
# Title         :   jfm countrie code insert program
# Database  :   pwaadb.jfm_countries
# Files        :   jfm_code_insert_sh.py
########################################################

import sys, hmac, httplib, json, time, hashlib, logging
import pymongo


# logging function
def print_log( log_str ) :
    print log_str
    #logging.info( log_str )
    return ""




# loggin config
#logging.basicConfig(filename='jfm_sh.log', level=logging.INFO,  format='%(asctime)s \n====> %(message)s')

# now time
now_str = time.strftime('%Y-%m-%d %H:%M:%S') 

# log
log_str = "\n\n========= jfm_code_insert_sh.py  start ========="
print_log( log_str )

# DB connect
mongoCon = pymongo.MongoClient("localhost")

# Api 
res_str = "/v2/media-countries/PG?apiKey=55088da22fc360.94752181&expand=mediaLanguages&metadataLanguageTags=en"
# http connect
conn = httplib.HTTPSConnection("admin.arclight.org")
conn.request("GET", res_str)
res = conn.getresponse()

# log
log_str = "HTTPSConnection: "+ res.reason
print_log( log_str )


#print "====> res.read() : ", res.read()
#sys.exit()

# data list 
count = 0
if res.reason == "OK" :
    res_obj = json.loads( res.read() )
    for data in res_obj["_embedded"]["mediaLanguages"] :        
        count += 1
        entry = {}
        entry["languageId"] = data.get("languageId", "")
        entry["name"] = data.get("name", "")
        entry["iso3"] = data.get("iso3", "")
        entry["sys_reg_date_time"] = now_str
 
        # convert
        res_text = json.dumps(entry)
        res_doc = json.loads(res_text)
        # data table
        mongoCon.pwaadb.jfm_countries.update( {"iso3":res_doc["iso3"]}, res_doc, upsert=True)

else:
    # log
    log_str = "HTTPSConnection Error"
    print_log( log_str )


# log
log_str = "Total count: %d" % count
print_log( log_str )

