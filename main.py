import requests

url = "https://secure.smslink.ro/sms/gateway/communicate/index.php"

#
#  Get your SMSLink / SMS Gateway Connection ID and Password from 
#  https://www.smslink.ro/get-api-key/
#

querystring = {
  "connection_id":"... My SMS Gateway Connection ID ...",
  "password":"... My SMS Gateway Connection Password ...",
  "to":"07xyzzzzzz",
  "message":"My Test Message"
}

headers = {}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)