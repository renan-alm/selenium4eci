# tests/test_example.py
import unittest
import time
from utils.driver import get_driver
from utils.token_reader import read_token
from pages.first_page import FirstPage

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.first_page = FirstPage(self.driver)

    def test_input_token(self):
        self.driver.get("https://eci.github.com/")
        token = read_token()
        self.first_page.input_token(token)
        input("Press Enter to continue...")  # Pause execution until Enter is pressed
        # Add assertions as needed to verify the next page or successful login

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
