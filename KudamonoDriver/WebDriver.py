import json
import requests
from KudamonoDriver.serverManipulator import *
from KudamonoRequests.k_requester import *

#from sessionData import sessionData

class WebDriver():
    def __init__(self,browser,port='9000'):
        self.port=port
        self.capabilites={}
        self.browser = browser
        self.url = 'http://127.0.0.1:'+self.port+"/"
        self.session=""
        self.server_manipulator = ServerManipulator()
        self.requester = k_requests()
        

    #BROWSER MANIPULATION

    def start_browser(self, browser = "chrome",capabilities={}):

        self.server_manipulator.open_server(browser,self.port)
        self.session = self.create_session(capabilities)

    def navigate(self,url):
        """
        Navigates to a site
        :param url: The url.
        :return:
        """
        try:
            response = self.requester.post(self.url+"session/"+self.session+"/url",{"url": url})
        except:
            print("Something went wrong on navigation")
            self.end_session(self.session)

    #-----------------BROWSER SIZE---------------------
    def close_browser(self):
        self.requester.delete(self.url+"session/"+self.session+"/window")

    def max_browser(self):
        max_url = self.url+"session/"+self.session+"/window/maximize"
        my_json = {'value':'maximize'}
        self.requester.post(max_url,my_json)
        #response = requests.request("POST",max_url,data=json.dumps(my_json).encode('utf-8'))

    def min_browser(self):
        min_url = self.url + "session/" + self.session + "/window/minimize"
        my_json = {'value': 'minimize'}
        response = requests.request("POST", min_url, data=json.dumps(my_json).encode('utf-8'))

    def full_screen_browser(self):
        fs_url = self.url + "session/" + self.session + "/window/fullscreen"
        my_json = {'value': 'fullscreen'}
        response = requests.request("POST", fs_url, data=json.dumps(my_json).encode('utf-8'))

    def set_browser_size(self,height,width):
        browser_size_url = self.url+"session/"+self.session+"/window/rect"
        my_json = {'width': width,'height': height}
        response = requests.request("POST", browser_size_url, data=json.dumps(my_json).encode('utf-8'))
    #----------------END OF BROWSER SIZES--------------------------------------------------
    def get_status(self):
        status_url = self.url + "status"
        response = requests.get(status_url)
        print("--STATUS---------")
        print(response.text)
        print("-----------------")
        return response.text

    #ELEMENT MANIPULATION

    def locate_element(self,location_type,location_value):
        """
        Locates an element.
        :param location_type: Type of location (id, name, etc)
        :param location_value: the locator itself.
        :return: the element.
        :author: Pablo Soifer
        """
        element_url = self.url + "session/" + self.session + "/element"
        my_json = {'using':location_type,'value':location_value}
        response = requests.request("POST", element_url, data=json.dumps(my_json).encode('utf-8'))
        return json.loads(response.text)['value']['ELEMENT']


    def write(self,element,text):
        """
        Writes something in a web element
        :param element: The element where the text will be writen
        :param text: The text that will go.
        :return:
        """
        write_url = self.url + "session/" + self.session +"/element/"+element+"/value"
        my_json = {'value': [text]}
        response = requests.request("POST", write_url, data=json.dumps(my_json).encode('utf-8'))

    def click(self,element):
        """
        Clicks on an element
        :param element: The element to be clicked
        :return:
        """
        write_url = self.url + "session/" + self.session + "/element/" + element + "/click"
        my_json = {'value': 'click'}
        response = requests.request("POST", write_url, data=json.dumps(my_json).encode('utf-8'))

    def get_element_text(self,element):
        """
        Gets an element text
        :param element: The element to get the text
        :return:
        """
        #text_url = self.url + "session/" + self.session + "/element/"+element+"/text"
        #response = requests.request("GET",text_url)
        #return json.loads(response.text)['value']
        return json.loads(self.requester.get(self.url + "session/" + self.session + "/element/"+element+"/text").text)['value']
    
    
    


    #MAYBE METHODS BELOW SHOULD GO IN A SEPARATE CLASS?

    def create_session(self,capabilities):
        if capabilities == {}:
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
            return json.loads(response.text)['sessionId']
        except:
            self.end_session()


    def end_session(self):
        requests.delete(self.url+"/session"+self.session)

