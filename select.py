from key import Keys
from webDriver import *

class Select:
    def __init__(self,element,driver):
        self.element = element
        self.driver = driver
    #SELECTS... this is gonna be hard...
    def select_by_text(self,text):
        """
        Selects item by text
        """
        my_key = Keys()
        all_text = self.driver.get_element_text(self.element).splitlines()
        all_text = [item.strip() for item in all_text] #Strip whitespaces
        print(all_text)
        print(all_text[0])
        number = all_text.index(text)
        self.driver.click(self.element)
        self.driver.write(self.element,my_key.get_key('HOME'))
        for i in range(0,number):
            self.driver.write(self.element,my_key.get_key('KEYDOWN'))
        self.driver.write(self.element,my_key.get_key('RETURN'))