from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = "C:/Users/Szalai Dániel/Documents/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, 'cookie')
store_elements = driver.find_element(By.ID, 'store').find_elements(By.TAG_NAME,
                                                                   'div')
store_elements_dict = {}

for element in store_elements:
    if element.get_attribute("id") == "buyElder Pledge":
        pass
    else:
        price = int(element.text.split("-")[1].split("\n")[0].replace(",", ""))
        id = (element.get_attribute("id"))
        store_elements_dict[price] = id

now = time.time()
start = now

while True:
    cookie.click()

    if time.time() > now + 1:
        cookie_number = int(driver.find_element(By.ID, 'money').text.replace(
            ",", ""))
        affordable = []
        for key in store_elements_dict:
            if key <= cookie_number:
                affordable.append(key)
        max_affordable = max(affordable)
        driver.find_element(By.ID, store_elements_dict[max_affordable]).click()

        now = time.time()
    if now >= start+300:
        print(driver.find_element(By.ID, 'cps').text)
        break

driver.quit()

