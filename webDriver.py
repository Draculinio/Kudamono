import requests
import json
import os
class webDriver():
    def __init__(self,browser):
        self.browser = browser
        self.url = 'http://127.0.0.1:9000/'
    def start_browser(self):
        #Open server
        os.system("chromedriver.exe --port=9000")
        browser_configuration =  { #TODO: Start working in a json parser
           "desiredCapabilities": {
              "browserName": "chrome",
              "chromeOptions": {
                 "binary": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
              },
              "platform": "ANY"
           }
        }
        response = requests.request("POST",self.url,data=json.dumps(my_json).encode('utf8'))
        

    def end_browser(self,session_id):
        response = requests.request("DELETE",self.url+"/session"+session_id)
