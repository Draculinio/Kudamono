class DesiredCapabilities:
    def __init__(self):
        self.desiredCapabilities = {'desiredCapabilities':{}}
    def add_capability(self,key,value):
        self.desiredCapabilities['desiredCapabilities'][key]=value
        
    def add_chrome_options(self,key,value):
        if not 'chromeOptions' in self.desiredCapabilities:
            self.desiredCapabilities['desiredCapabilities']['chromeOptions']={}
        self.desiredCapabilities['desiredCapabilities']['chromeOptions'][key]=value
            