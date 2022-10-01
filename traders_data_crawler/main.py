from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from fake_headers import Headers
import mysql.connector
import subprocess
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

def en_side(s):
    if(s=='做多'): return str('long')
    if(s=='做空'): return str('short')

def check_ch(s):
    for _char in s:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

input_path = '../webclimber/hot_traders.txt'
f = open(input_path,'r')
output_path = './traders_data.txt'
out = open(output_path,'w')

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
url_list=f.readlines()

for trader_url in url_list:
    chrome.get(trader_url)
    time.sleep(0.5)
    #determine if bingx or binance
    try:
        type=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[2]')
        if(type.text[3]=='g'): error_maker=chrome.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[1]/div[2]/div[10]')
        continue
        #binance無開倉時間，放生
        #history = WebDriverWait(chrome,5).until(
        #    EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[4]/div[1]/div[3]'))
        #)
    except:
        history = WebDriverWait(chrome,5).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]'))
        )

    actions = ActionChains(chrome)
    actions.click(history) #press history button
    actions.perform()
    actions.reset_actions()#show history first then load more data

    #load full data
    seemore = WebDriverWait(chrome,5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[3]/div'))
    )
    while(seemore.text=="View More"):
        seemore = WebDriverWait(chrome,5).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[3]/div'))
        )
        actions.click(seemore)
        actions.perform()
        actions.reset_actions()

    data= chrome.find_elements(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[2]/div/div')
    trader_id=GetId(chrome.current_url)
    out.write(trader_id+"\n")
    print(trader_id)
    for order in data[1:-1]:
        detail=order.text.split("\n")
        if(not check_ch(detail[0]) and detail[0]!=''):
            tmp = detail[0]+" "+detail[1]+" "+detail[2]+" "+detail[4]+" "+detail[3]+" "+detail[5]+" "+detail[-4]
            out.write(tmp + "\n")
            print(tmp)
f.close()
out.close()
chrome.close()
