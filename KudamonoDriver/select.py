from KudamonoDriver.key import Keys


class Select:
    def __init__(self,element,driver):
        self.element = element
        self.driver = driver
    #SELECTS... this is gonna be hard... 
    # 07/23/2017 Well, it wasn't.
    def select_by_text(self,text):
        """
        Selects item by text
        """
        
        all_text = self.driver.get_element_text(self.element).splitlines()
        all_text = [item.strip() for item in all_text] #Strip whitespaces
        number = all_text.index(text)
        self.select_by_index(number)

    def select_by_index(self,index):
        """
        Selects item by index
        """
        my_key = Keys()
        self.driver.click(self.element)
        self.driver.write(self.element,my_key.get_key('HOME'))
        for i in range(0,index):
            self.driver.write(self.element,my_key.get_key('KEYDOWN'))
        self.driver.write(self.element,my_key.get_key('RETURN'))

    

    #TODO: Select By value

    