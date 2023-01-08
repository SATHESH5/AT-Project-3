from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import dataemergency
import pytest
import time

class Test_Emergency_Contact_Details:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
        
    def test_emergency_contact_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataemergency.Selenium_Selectors.username_input).send_keys(dataemergency.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=dataemergency.Selenium_Selectors.password_input).send_keys(dataemergency.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataemergency.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataemergency.Selenium_Selectors.firstname_input).send_keys(dataemergency.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=dataemergency.Selenium_Selectors.lastname_input).send_keys(dataemergency.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.id_xpath).send_keys(dataemergency.Sathesh_Data.id_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.save_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataemergency.Selenium_Selectors.emergency_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.add_1_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.name_xpath).send_keys(dataemergency.Sathesh_Data.name_data)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.relationship_xpath).send_keys(dataemergency.Sathesh_Data.relationship_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.home_no_xpath).send_keys(dataemergency.Sathesh_Data.home_no_data)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.mobile_no_xpath).send_keys(dataemergency.Sathesh_Data.mobile_no_data)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.work_no_xpath).send_keys(dataemergency.Sathesh_Data.work_no_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemergency.Selenium_Selectors.save_1_xpath).click()
        time.sleep(8)
        print("Successfully all details filled in Emergency contact details")
        
        