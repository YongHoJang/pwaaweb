import hmac, httplib, json
from hashlib import sha1
from time import time

def getRequest():
    key = '7d535d9ec739be2e4b1d643e128d2562'

    secret = 'a7f20c469d501f51296b5d997426313c377c83aeb0afb072ffc505cde05f4de69aafa5629d81340c76d51866b1d5b3b596d8679ad9861b5619f683871968e9ce'

    curr_time = str(int(time()))

    h1 = hmac.new(secret, curr_time+key, sha1)

    api_sig = h1.hexdigest()
    #print api_sig

    res_str = '/all?api_key=7d535d9ec739be2e4b1d643e128d2562&api_sig=' + api_sig
    #print res_str

    conn = httplib.HTTPSConnection("pcalspdata-qa.api.sil.org")
    conn.request("GET",res_str)
    res = conn.getresponse()
    print res.status, res.reason
    #print res.read()
    return json.loads(res.read())

