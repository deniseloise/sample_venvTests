#! python3
# sample python script for testing venv

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")
driver.maximize_window()

driver.implicitly_wait(10)  # seconds

#Timestamp - Start
print('The script run at ' + str(datetime.datetime.now()))