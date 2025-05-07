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
options.add_argument("-profile")
options.add_argument("/app/za73pwwo.default")
driver = webdriver.Firefox(service=webdriver.firefox.service.Service("/usr/local/bin/geckodriver"), options=options)
driver.get("https://www.youtube.com")
time.sleep(20)
os.system("/app/fuck")
driver.save_screenshot("/app/fuck/a.png")
time.sleep(5)
e1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"))
e1.click()
time.sleep(5)
driver.save_screenshot("/app/fuck/b.png")
e2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, "ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)"))
e2.click()
time.sleep(5)
driver.save_screenshot("/app/fuck/c.png")
driver.quit()
