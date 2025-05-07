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
driver.save_screenshot("/app/yt_screenshot/a.png")
time.sleep(5)
e1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"buttons\"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")))
e1.click()
time.sleep(5)
driver.save_screenshot("/app/yt_screenshot/b.png")
e2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-compact-link-renderer:nth-of-type(1) div:nth-of-type(2) > yt-formatted-string:nth-of-type(1)")))
e2.click()
time.sleep(5)
driver.save_screenshot("/app/yt_screenshot/c.png")
e3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"content\"]/input")))
e3.send_keys("C:\\Users\\Administrator\\qq\\d45.mp4")
time.sleep(20)
driver.save_screenshot("/app/yt_screenshot/d.png")
e4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.title ytcp-social-suggestion-input > div")))
e4.clear()
e4.send_keys("""tag your theduviya 😂😂 .  .  .  bgmi core 🤡 .  .  . #bgmi #bgmitamil #fyp #funny""")
time.sleep(5)
e5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.description ytcp-social-suggestion-input > div")))
e5.clear()
e5.send_keys("""#bgmilovers❤️ #bgmitamillive #bgmitamilreels #bgmitamil #bgmimemes #bgmitamilgameplay #bgmi #bgmiholidaygiveaway #bgmi #bgmiholidaygiveaway #bgmitamilstatus #bgmitamilmemes #bgmitamilan #bgmiclips #bgmicore #bgmiindia🇮🇳 #bgmi❤️ #bgmifunny #pubgmoments #pubgtamils #pubgtamilmemes #pubgtamizhan #pubgtamil #pubgmeme #pubgmeme  #pubgvibes #pubg #pubgindia #fy #fypシ❤️💞❤️ #fypシ #fyp #fyp
""")
time.sleep(5)
driver.save_screenshot("/app/yt_screenshot/e.png")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytkc-made-for-kids-select tp-yt-paper-radio-button:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1)"))).click()
time.sleep(8)
driver.save_screenshot("/app/yt_screenshot/f.png")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='next-button']/ytcp-button-shape"))).click()
time.sleep(8)
driver.save_screenshot("/app/yt_screenshot/g.png")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='next-button']/ytcp-button-shape"))).click()
time.sleep(8)
driver.save_screenshot("/app/yt_screenshot/h.png")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='next-button']/ytcp-button-shape"))).click()
time.sleep(8)
driver.save_screenshot("/app/yt_screenshot/i.png")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tp-yt-paper-radio-button:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(1)"))).click()
time.sleep(8)
driver.save_screenshot("/app/yt_screenshot/j.png")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ytcp-button[@id='done-button']/ytcp-button-shape"))).click()
time.sleep(8)
driver.save_screenshot("/app/yt_screenshot/k.png")
driver.quit()
