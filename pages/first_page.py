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
        
        # Use JavaScript to set the value and trigger the input event
        self.driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));", token_input, token)
        
        # Verify the value of the input field
        value = self.driver.execute_script("return arguments[0].value;", token_input)
        print(f"Token input value: {value}")
        
        token_input.send_keys(Keys.RETURN)
