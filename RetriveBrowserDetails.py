from selenium import webdriver

driver=webdriver.Firefox()

driver.get("https://www.google.com")
print(driver.title)
print(driver.page_source)
print(driver.get_cookies())
driver.minimize_window()