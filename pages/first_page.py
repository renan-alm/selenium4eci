# pages/first_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FirstPage:
    def __init__(self, driver):
        self.driver = driver

    def input_token(self, token):
        wait = WebDriverWait(self.driver, 10)
        token_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Auth Token"]')))
        self.driver.execute_script("arguments[0].value = arguments[1];", token_input, token)
        token_input.send_keys(Keys.RETURN)
