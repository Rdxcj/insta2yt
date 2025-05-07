import json
import os
import subprocess
import time
import sys
import os
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--headless")
driver = webdriver.Firefox(service=webdriver.firefox.service.Service("/usr/local/bin/geckodriver"), options=options)
driver.get("https://www.youtube.com")
time.sleep(10)
driver.save_screenshot("/usr/local/bin/k.png")
time.sleep(5)
driver.quit()
