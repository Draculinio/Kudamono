#Ejecutar el chromedriver
import os
import json
import requests

os.system("chromedriver.exe --port=9000")

#session creation
my_json =  {
   "desiredCapabilities": {
      "browserName": "chrome",
      "chromeOptions": {
         "binary": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
      },
      "platform": "ANY"
   }
}

url = "http://127.0.0.1:9000/session"

response = requests.request("POST",url,data=json.dumps(my_json).encode('utf8'))

print(response.text)
print(response.headers) 
session = json.loads(response.text)['sessionId']
#Session destruction
response = requests.request("DELETE",url+"/"+session)
print(response.text)
