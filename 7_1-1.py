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
        self.driver.get("http://localhost:3000/Health-Plus")
        self.assertIn("Health Plus", self.driver.title)

    def test_service_link_navigation(self):
        """Test Case 2: Verify Clicking 'Services' Link Navigates to Services Page"""
        self.driver.get("http://localhost:3000/Health-Plus")
        service_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Services"))
        )
        service_link.click()
        time.sleep(2)
        self.assertIn("Services", self.driver.page_source)

    def test_Book_Appointment(self):
        """Test Case 3: Verify Clicking 'Reviews' Link Navigates to Reviews Page"""
        self.driver.get("http://localhost:3000/Health-Plus")
        review_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Reviews"))
        )
        review_link.click()
        time.sleep(2)
        self.assertIn("Reviews", self.driver.page_source)

    def test_contributors_link_navigation(self):
        """Test Case 4: Verify Clicking 'Contributors' Link Navigates to About Section"""
        self.driver.get("http://localhost:3000/Health-Plus")
        about_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Contributors"))
        )
        about_link.click()
        time.sleep(2)
        self.assertIn("Contributors", self.driver.page_source)
        
        

    def test_doctors_link_navigation(self):
        """Test Case 5: Verify Clicking 'Doctors' Link Navigates to Doctors Page"""
        self.driver.get("http://localhost:3000/Health-Plus")
        doctors_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Doctors"))
        )
        doctors_link.click()
        time.sleep(2)
        self.assertIn("Doctors", self.driver.page_source)
    
    def test_review_link_navigation(self):
        """Test Case 3: Verify Clicking 'Reviews' Link Navigates to Appointment Page"""
        self.driver.get("http://localhost:3000/Health-Plus")
        review_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Appointment"))
        )
        review_link.click()
        time.sleep(2)
        self.assertIn("Appointment", self.driver.page_source)    

    

    def test_subscribe_button(self):
        """Test Case 6: Verify Subscription Button Presence"""
        self.driver.get("http://localhost:3000/Health-Plus")
        subscribe_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Subscribe']"))
        )
        self.assertTrue(subscribe_button.is_displayed(), "'Subscribe' button is not displayed!")

   
    def test_Slider_button(self):
        
        self.driver.get("http://localhost:3000/Health-Plus")
        subscribe_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Subscribe']"))
        )
        self.assertTrue(subscribe_button.is_displayed(), "'Subscribe' button is not displayed!")
        # Click and verify any relevant changes if applicable
        
    # def test_social_media_links(self):
    #     """Test Case 8: Verify Social Media Links Redirect to Correct Pages"""
    #     self.driver.get("https://alkaison.github.io/Health-Plus/")
        
    #     try:
    #         # Locate and click the Facebook icon
    #         facebook_icon = WebDriverWait(self.driver, 60).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-facebook"))
    #         )
    #         facebook_icon.click()
    #         time.sleep(3)  # Wait for the page to load
    #         self.assertIn("facebook.com", self.driver.current_url, "Facebook link did not redirect correctly!")
    #         self.driver.back()  # Go back to Health Plus page

    #         # Locate and click the LinkedIn icon
    #         linkedin_icon = WebDriverWait(self.driver, 60).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-linkedin"))
    #         )
    #         linkedin_icon.click()
    #         time.sleep(3)  # Wait for the page to load
    #         self.assertIn("linkedin.com", self.driver.current_url, "LinkedIn link did not redirect correctly!")
    #         self.driver.back()  # Go back to Health Plus page

    #         # Locate and click the Twitter icon
    #         twitter_icon = WebDriverWait(self.driver, 60).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-twitter"))
    #         )
    #         twitter_icon.click()
    #         time.sleep(3)  # Wait for the page to load
    #         self.assertIn("twitter.com", self.driver.current_url, "Twitter link did not redirect correctly!")

    #     except Exception as e:
    #         print("An error occurred while testing social media links:", str(e))
    #         self.fail("Test failed due to an unexpected error.")
        

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    # Run the tests and generate an HTML report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
