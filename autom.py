from webDriver import webDriver

driver = webDriver("Chrome")
driver.start_browser()
driver.navigate("http://www.google.com")
driver.close_browser()
#driver.end_session()
driver.end_driver()