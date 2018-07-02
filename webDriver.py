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
            my_json = {"url": url}
            navigation_url = self.url+"session/"+self.session+"/url"
            response = requests.request("POST", navigation_url, data=json.dumps(my_json).encode('utf8'))
        except:
            print("Something went wrong on navigation")
            self.end_session(self.session)

    def close_browser(self):
        close_url = self.url+"session/"+self.session+"/window"
        requests.request("DELETE", close_url)

    def max_browser(self):
        max_url = self.url+"session/"+self.session+"/window/maximize"
        my_json = {'value':'maximize'}
        response = requests.request("POST",max_url,data=json.dumps(my_json).encode('utf-8'))

    def min_browser(self):
        min_url = self.url + "session/" + self.session + "/window/minimize"
        my_json = {'value': 'minimize'}
        response = requests.request("POST", min_url, data=json.dumps(my_json).encode('utf-8'))

    def full_screen_browser(self):
        fs_url = self.url + "session/" + self.session + "/window/fullscreen"
        my_json = {'value': 'fullscreen'}
        response = requests.request("POST", fs_url, data=json.dumps(my_json).encode('utf-8'))

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