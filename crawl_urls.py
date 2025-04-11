from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

webdriver_path = "chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
url = "https://www.worldometers.info/coronavirus/"

driver.get(url)
time.sleep(15)

elements = driver.find_elements(By.XPATH, '//*[@id="main_table_countries_today"]/tbody[1]/tr/td[2]/a')
url_sp = []

for element in elements:
    href_value = element.get_attribute("href")
    url_sp.append(href_value)
print("Số lượng URL tìm thấy:", len(url_sp))

driver.quit()

df = pd.DataFrame(url_sp, columns=["URL"])
df.to_csv("urls.csv", index=False)