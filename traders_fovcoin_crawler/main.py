from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from fake_headers import Headers
import time

def GetId(s):
    id=""
    flag=False
    for i in s[::-1]:
        if(i=="/" and flag): break
        if(i=="/"):
            flag=True
            continue
        if(flag):
            id+=i
    return id[::-1]

input_path = '../traders_link_crawler/hot_traders.txt'
f = open(input_path,'r')
output_path = './traders_fovcoin.txt'
out = open(output_path,'w')

header = Headers(
    browser = "chrome",
    os = "wim",
    headers = False
)
customUserAgent = header.generate()['User-Agent']

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--headless")
options.add_argument(f"--user-agent={customUserAgent}")
options.add_argument("--window-size=1280x720")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

chrome = webdriver.Chrome('./chromedriver.exe', options=options)
url_list=f.readlines()

for trader_url in url_list:
    chrome.get(trader_url)
    out.write(GetId(chrome.current_url)+'\n')
    time.sleep(1)
    try:
        for i in range(2,6):
            coin = chrome.find_element(By.XPATH,f'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[{i}]/span[1]')
            print(coin.text)
            if coin.text!='LUNA-OLD':
                out.write(coin.text+" ")
        out.write("\n")
    except:
        out.write("\n")
f.close()
out.close()
chrome.close()
