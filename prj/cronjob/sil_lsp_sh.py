########################################################
# Title         :   SIL-LSP  Api batch program
# Database  :   pwaadb.sildata, pwaadb.sildata_history
# Files        :   sil_lsp_sh.py, sil_lsp_sh.log, sil_lsp_cron.sh
########################################################

import sys, hmac, httplib, json, time, hashlib, logging
import pymongo


# logging function
def print_log( log_str ) :
    print log_str
    logging.info( log_str )
    return ""




# loggin config
logging.basicConfig(filename='sil_lsp_sh.log', level=logging.INFO,  format='%(asctime)s \n====> %(message)s')

# now time
now_str = time.strftime('%Y-%m-%d %H:%M:%S') 
week_str = time.strftime('%Y%U') 

#print "====> week_str: ", week_str
#sys.exit()

# log
log_str = "\n\n========= sil_lsp_sh.py  start ========="
print_log( log_str )

# DB connect
mongoCon = pymongo.MongoClient("localhost")

# Api 
key = '7d535d9ec739be2e4b1d643e128d2562'
secret = 'a7f20c469d501f51296b5d997426313c377c83aeb0afb072ffc505cde05f4de69aafa5629d81340c76d51866b1d5b3b596d8679ad9861b5619f683871968e9ce'
curr_time = str(int( time.time() ))
h1 = hmac.new(secret, curr_time+key, hashlib.sha1)
api_sig = h1.hexdigest()
res_str = '/all?api_key=7d535d9ec739be2e4b1d643e128d2562&api_sig=' + api_sig

# http connect
conn = httplib.HTTPSConnection("pcalspdata-qa.api.sil.org")
conn.request("GET",res_str)
res = conn.getresponse()

# log
log_str = "HTTPSConnection: "+ res.reason
print_log( log_str )


# data list 
count = 0
if res.reason == "OK" :
    res_obj = json.loads( res.read() )
    for data in res_obj["items"] :        
        count += 1
        entry = {}
        entry["iso_code"] = data.get("iso_code", "")
        entry["reference_name"] = data.get("reference_name", "")
        entry["existing_scripture"] = data.get("existing_scripture", "")
        entry["existing_scripture_dis"] = data.get("existing_scripture_dis", "")
        entry["update_date_time"] = data.get("update_date_time", "")
        entry["sys_reg_date_time"] = now_str
        entry["sys_year_week"] = week_str        
        # convert
        res_text = json.dumps(entry)
        res_doc = json.loads(res_text)
        # data table
        mongoCon.pwaadb.sildata.update( {"iso_code":res_doc["iso_code"]}, res_doc, upsert=True)
        # history table
        mongoCon.pwaadb.sildata_history.update( {"iso_code":res_doc["iso_code"], "sys_year_week":res_doc["sys_year_week"]}, res_doc, upsert=True)

else:
    # log
    log_str = "HTTPSConnection Error"
    print_log( log_str )


# log
log_str = "Total count: %d" % count
print_log( log_str )

