from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import datadependent
import pytest
import time

class Test_Employee_Dependents_Contact_Details:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
        
    def test_dependents_contact_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datadependent.Selenium_Selectors.username_input).send_keys(datadependent.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=datadependent.Selenium_Selectors.password_input).send_keys(datadependent.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datadependent.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datadependent.Selenium_Selectors.firstname_input).send_keys(datadependent.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=datadependent.Selenium_Selectors.lastname_input).send_keys(datadependent.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.id_xpath).send_keys(datadependent.Sathesh_Data.id_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.save_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datadependent.Selenium_Selectors.dependent_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.add_1_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.name_xpath).send_keys(datadependent.Sathesh_Data.name_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.date_xpath).send_keys(datadependent.Sathesh_Data.date_data)
        time.sleep(3)
        a_relationship = self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.relationship_xpath)
        a_relationship.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.specify_xpath).send_keys(datadependent.Sathesh_Data.specify_data)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datadependent.Selenium_Selectors.save_1_xpath).click()
        time.sleep(7)
        print("Successfully all details filled in dependent contact details")
        
        
        