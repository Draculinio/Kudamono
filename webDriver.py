import requests
import json
import os
class webDriver():
    def __init__(self,browser):
        self.browser = browser
        self.url = 'http://127.0.0.1:9000/'

    def start_browser(self):
        self.open_server("chrome")
        self.create_session()
        

    def end_browser(self,session_id):
        response = requests.request("DELETE",self.url+"/session"+session_id)

    #MAYBE METHODS BELOW SHOULD GO IN A SEPARATE CLASS?

    def open_server(self,server):
        if str.upper(server) == "CHROME":
            os.system("chromedriver.exe --port=9000")

    def create_session(self):
        browser_configuration = {  # TODO: Start working in a json parser
            "desiredCapabilities": {
                "browserName": "chrome",
                "chromeOptions": {
                    "binary": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                },
                "platform": "ANY"
            }
        }
        response = requests.request("POST", self.url, data=json.dumps(browser_configuration).encode('utf8'))