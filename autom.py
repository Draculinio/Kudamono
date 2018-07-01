      #####################SANDBOX########################
import os
import json
import requests
import subprocess

import threading

#os.system("chromedriver.exe --port=9000")
def server():
    process = subprocess.Popen("chromedriver.exe --verbose --port=9000")
    return process

def flow():
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
    #Navigation
    my_json = {"url": "https://github.com/Draculinio/Kudamono"}
    response = requests.request("POST",url+"/"+session+"/url",data=json.dumps(my_json).encode('utf8'))
    print(response.text)
    #Close browser
    response = requests.request("DELETE", url + "/" + session+"/window")
    #Session destruction
    response = requests.request("DELETE",url+"/"+session)
    print(response.text)


process = server()
flow()
process.terminate()