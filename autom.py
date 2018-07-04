from webDriver import webDriver
import time

driver = webDriver("Chrome")
driver.start_browser()
driver.navigate("http://www.google.com")
driver.max_browser()
driver.min_browser()
driver.full_screen_browser()
search_bar = driver.locate_element("xpath","//*[@id='lst-ib']")
driver.write(search_bar,"Hola Mundo")
time.sleep(5)
driver.get_status()
driver.close_browser()

driver.end_driver()