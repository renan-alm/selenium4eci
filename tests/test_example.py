# tests/test_example.py
import unittest
from utils.driver import get_driver
from pages.base_page import BasePage

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.base_page = BasePage(self.driver)

    def test_open_google(self):
        self.base_page.open_url("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
