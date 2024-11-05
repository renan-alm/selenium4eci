# utils/driver.py
from selenium import webdriver

def get_driver():
    driver = webdriver.Chrome()  # You can change this to any other browser
    driver.maximize_window()
    return driver

