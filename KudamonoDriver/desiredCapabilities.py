class DesiredCapabilities:
    def __init__(self):
        self.desiredCapabilities = {'desiredCapabilities':{}}
    def add_capability(self,key,value):
        self.desiredCapabilities['desiredCapabilities'][key]=value
        print(self.desiredCapabilities)
