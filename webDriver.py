import requests
import json
import subprocess

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
            my_json = {"url": url}
            requests.request("POST", self.url + self.session + "/url", data=json.dumps(my_json).encode('utf8'))
        except:
            print("Something went wrong on navigation")
            self.end_session(self.sessio)

    def close_browser(self):
        requests.request("DELETE", self.url + self.session + "/window")

    #MAYBE METHODS BELOW SHOULD GO IN A SEPARATE CLASS?

    def open_server(self,server):
        """Opens the server in a subroprcess. Which server will open depends on the browser you want to use."""
        if str.upper(server) == "CHROME":
            self.process = subprocess.Popen("chromedriver.exe --verbose --port=9000")
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
            print("URL TO POINT: "+self.url)
            #response = requests.request("POST", self.url+"/session", data=json.dumps(capabilities).encode('utf8'))
            response = requests.post(self.url+"//session",json=[capabilities])
            print("Response: "+response.text)
            return response
        except:
            self.end_session()


    def end_session(self):
        #requests.request("DELETE",self.url+"/session"+self.session)
        requests.delete(self.url+"/session"+self.session)

    def end_driver(self):
        self.process.terminate()