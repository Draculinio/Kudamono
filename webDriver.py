import requests
import json
import subprocess
from sessionData import sessionData

class webDriver():
    def __init__(self,browser):
        self.browser = browser
        self.url = 'http://127.0.0.1:9000/'
        self.session=""
        self.process = ""

    def start_browser(self):
        self.open_server("chrome")
        self.session = self.create_session()
        
    def navigate(self,url):
        try:
            my_json = {"url": "https://www.google.com"}
            navigation_url = self.url+"session/"+self.session+"/url"
            print("Pointing to: "+navigation_url)
            response = requests.request("POST", navigation_url, data=json.dumps(my_json).encode('utf8'))
            print(response.text)
        except:
            print("Something went wrong on navigation")
            self.end_session(self.session)

    def close_browser(self):
        close_url = self.url+"session/"+self.session+"/window"
        requests.request("DELETE", close_url)

    #MAYBE METHODS BELOW SHOULD GO IN A SEPARATE CLASS?

    def open_server(self,server):
        """Opens the server in a subroprcess. Which server will open depends on the browser you want to use."""
        if str.upper(server) == "CHROME":
            #self.process = subprocess.Popen("chromedriver.exe --verbose --port=9000")
            self.process = subprocess.Popen("chromedriver.exe --port=9000")
            return self.process #TODO: See if this is needed in the future

    def create_session(self):
        capabilities = {
            "desiredCapabilities": {
                "browserName": "chrome",
                "chromeOptions": {
                    "binary": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                },
                "platform": "ANY"
            }
        }
        try:

            session_url = self.url+"session"
            response = requests.request("POST", session_url, data=json.dumps(capabilities).encode('utf8'))
            #print("Response: "+response.text)
            return json.loads(response.text)['sessionId']
        except:
            self.end_session()


    def end_session(self):
        #requests.request("DELETE",self.url+"/session"+self.session)
        requests.delete(self.url+"/session"+self.session)

    def end_driver(self):
        print("Finishing webdriver server...")
        self.process.terminate()