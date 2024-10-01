#this is my first python code. EOF
#this is a second line i added to find out how git works

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_drive():

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_drive()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")

    return element

print(main())