import requests
import json
from datetime import datetime
import hashlib
import hmac

ipaymuVa  = "1179005695516187" #your iPaymu VA
ipaymuKey = "3B00D100-64C8-41AE-BB8D-E21AA0E51F14" #your iPaymu API Key

body =  {}

data_body    = json.dumps(body)
data_body    = json.dumps(body, separators=(',', ':'))
encrypt_body = hashlib.sha256(data_body.encode()).hexdigest()
stringtosign = "{}:{}:{}:{}".format("POST", ipaymuVa, encrypt_body, ipaymuKey)
signature    = hmac.new(ipaymuKey.encode(), stringtosign.encode(), hashlib.sha256).hexdigest().lower()

timestamp    = datetime.today().strftime('%Y%m%d%H%M%S')

url = "https://my.ipaymu.com/api/v2/payment-method-list"

payload={}
files={}
headers = {
  'Content-Type': 'application/json',
  'signature': signature,
  'va': ipaymuVa,
  'timestamp': timestamp
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
