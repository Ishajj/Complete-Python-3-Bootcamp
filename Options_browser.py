from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#A headless browser is just a regular web browser, except that it contains no visible UI element.
# Just like you’d expect, it can do more than make requests: it can also render HTML (though you cannot see it),
# keep session information, and even perform asynchronous network communications by running JavaScript code.
options = webdriver.ChromeOptions()
options.set_headless()
# options.add_argument('-headless')
options.add_argument('-start-maximized')
options.add_argument('-disable-notifications')
options.add_argument('-incognito')

driver=webdriver.Chrome(executable_path="C:/Users/I823285/PycharmProjects/SeleniumTest/Browsers/chromedriver.exe",chrome_options=options)
