from WebDriver import WebDriver
import time
import os
from key import *
from select import *

key = Keys()
driver = WebDriver("Chrome", '8500')
driver.start_browser()
driver.navigate(os.getcwd()+"/Test_site/index.html")
driver.max_browser()
driver.min_browser()
driver.full_screen_browser()
search_bar = driver.locate_element("xpath","//*[@id='my_search']")
driver.write(search_bar,"Hola Mundo"+key.get_key('SEMICOLON'))
time.sleep(2)
submit_button = driver.locate_element("xpath","//*[@id='submit_search']")
driver.click(submit_button)
gotosite_link = driver.locate_element("xpath","//*[@id='goto_first_page']")
print(driver.get_element_text(gotosite_link))
driver.click(gotosite_link)
combo = driver.locate_element("xpath","//*[@id='testSelect']")
comboSelector = Select(combo,driver)
comboSelector.select_by_text("Second Option")
time.sleep(2)
comboSelector.select_by_index(2)
time.sleep(2)
driver.get_status()
driver.close_browser()
