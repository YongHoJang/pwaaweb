########################################################
# Title         :   jfm countrie code insert program
# Database  :   pwaadb.jfm_countries
# Files        :   jfm_code_insert_sh.py
########################################################

import sys, hmac, httplib, json, time, hashlib, logging
import pymongo


# now time
now_str = time.strftime('%Y-%m-%d %H:%M:%S') 

# log
log_str = "\n\n========= jfm_code_insert_sh.py  start ========="
print log_str


# DB connect
mongoCon = pymongo.MongoClient("localhost")

# Api 
res_str = "/v2/media-languages?page=1&limit=1297&apiKey=55088da22fc360.94752181"
# http connect
conn = httplib.HTTPSConnection("admin.arclight.org")
conn.request("GET", res_str)
res = conn.getresponse()

# log
log_str = "HTTPSConnection: "+ res.reason
print log_str


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
        entry["iso_code"] = data.get("iso3", "")
        entry["sys_reg_date_time"] = now_str
 
        # convert
        res_text = json.dumps(entry)
        res_doc = json.loads(res_text)

        print "\n===> [%d] : %s" % (count, res_doc)
        # data table, 1214 inserted
        mongoCon.pwaadb.jfm_countries.update( {"iso_code":res_doc["iso_code"]}, res_doc, upsert=True)

else:
    # log
    log_str = "HTTPSConnection Error"
    print log_str


# log
log_str = "Total count: %d" % count
print log_str

