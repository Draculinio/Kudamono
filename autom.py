from webDriver import webDriver

driver = webDriver("Chrome")
driver.start_browser()
driver.navigate("http://www.google.com")
driver.max_browser()
driver.min_browser()
driver.full_screen_browser()
driver.locate_element("xpath","//*[@id='lst-ib']")
driver.get_status()
driver.close_browser()

driver.end_driver()