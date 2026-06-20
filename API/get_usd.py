import requests

response = requests.get("http://api.navasan.tech/latest/?api_key=freeTEG7VANz89P2pOlyd6aiieBYtXxc")

def get_usd_price() -> int :
   if response.status_code == 200:
    data = response.json()
    if data['usd_usdt']!=None and data['usd_usdt']['value']!=None:
      return int(data['usd_usdt']['value'])
    else :
        return -1

   else:
       return -1

