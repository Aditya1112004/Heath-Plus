import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner

class HealthPlusWebsiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    # ---------- HOME PAGE TEST CASES ----------

    def test_home_page_title(self):
        """Test Case 1: Verify Home Page Title"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        self.assertIn("Health Plus", self.driver.title)

    def test_service_link_navigation(self):
        """Test Case 2: Verify Clicking 'Services' Link Navigates to Services Page"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        service_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Services"))
        )
        service_link.click()
        time.sleep(2)
        self.assertIn("Services", self.driver.page_source)

    def test_review_link_navigation(self):
        """Test Case 3: Verify Clicking 'Reviews' Link Navigates to Reviews Page"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        review_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Reviews"))
        )
        review_link.click()
        time.sleep(2)
        self.assertIn("Reviews", self.driver.page_source)

    def test_about_link_navigation(self):
        """Test Case 4: Verify Clicking 'About' Link Navigates to About Section"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        about_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "About"))
        )
        about_link.click()
        time.sleep(2)
        self.assertIn("About", self.driver.page_source)

    def test_doctors_link_navigation(self):
        """Test Case 5: Verify Clicking 'Doctors' Link Navigates to Doctors Page"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        doctors_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Doctors"))
        )
        doctors_link.click()
        time.sleep(2)
        self.assertIn("Doctors", self.driver.page_source)

    

    def test_subscribe_button(self):
        """Test Case 6: Verify Subscription Button Presence"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        subscribe_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Subscribe']"))
        )
        self.assertTrue(subscribe_button.is_displayed(), "'Subscribe' button is not displayed!")

   
    def test_footer_subscription_section(self):
        """Test Case 7: Verify Footer Subscription Section Exists"""
        self.driver.get("https://alkaison.github.io/Health-Plus/")
        footer = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//footer"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not displayed!")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    # Run the tests and generate an HTML report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
