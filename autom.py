from webDriver import webDriver
import time
import os

driver = webDriver("Chrome",'8500')
driver.start_browser()
driver.navigate(os.getcwd()+"/Test_site/index.html")
driver.max_browser()
driver.min_browser()
driver.full_screen_browser()
search_bar = driver.locate_element("xpath","//*[@id='my_search']")
driver.write(search_bar,"Hola Mundo")

submit_button = driver.locate_element("xpath","//*[@id='submit_search']")
driver.click(submit_button)
gotosite_link = driver.locate_element("xpath","//*[@id='goto_first_page']")
driver.click(gotosite_link)
time.sleep(2)
driver.get_status()
driver.close_browser()

driver.end_driver()