from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from fake_headers import Headers
import mysql.connector
import subprocess
import time

def getID(urlStr):
    for i in range(len(urlStr) - 1):
        if (urlStr[i] == "/" and urlStr[i + 1] >= "0" and urlStr[i + 1] <= "9"):
            return urlStr[i + 1:len(urlStr) - 1]
    return ""

path = 'hot_traders_new.txt'
f = open(path,'w')

header = Headers(
    browser = "chrome",  # Generate only Chrome UA
    os = "win",  # Generate only Windows platform
    headers = False # generate misc headers
)
customUserAgent = header.generate()['User-Agent']

service = Service("/usr/bin/chromedriver")
options = Options()

options.add_argument("--disable-notifications")
options.add_argument("--headless")
options.add_argument(f"--user-agent={customUserAgent}")
options.add_argument("--window-size=1280x720")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

chrome = webdriver.Chrome(service=service, options=options)
chrome.get("https://bingx.com/zh-hk/traders")
time.sleep(2)
menu = chrome.window_handles[0]

sqldb = mysql.connector.connect(
    host = "localhost",
    user = "tradersuser",
    password = "TRADERSuser",
    database = "tradersdb",
)
cursor = sqldb.cursor()
cursor.execute("DELETE FROM `top`;")

for i in range(1,13):
    chrome.find_element(By.XPATH,f'//*[@id="__layout"]/div/div[1]/div/div[2]/div/div[4]/div/div[{i}]/div[1]').click()
    trader_page = chrome.window_handles[1]
    chrome.switch_to.window(trader_page)
    tmp = chrome.current_url[0:chrome.current_url.find('?')]
    print(tmp)
    f.write(tmp+"\n")
    cursor.execute("INSERT IGNORE INTO `info` VALUES(" + getID(tmp) +", NULL, NULL, NULL);")
    cursor.execute("REPLACE INTO `top` VALUES(" + getID(tmp) +");")
    chrome.close()
    chrome.switch_to.window(menu)

sqldb.commit()
chrome.quit()
f.close()
