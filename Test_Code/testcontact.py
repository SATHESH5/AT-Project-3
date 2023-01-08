from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Test_Data import datacontact
import pytest
import time

class Test_Employee_Contact_Details:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
        
    def test_contact_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datacontact.Selenium_Selectors.username_input).send_keys(datacontact.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=datacontact.Selenium_Selectors.password_input).send_keys(datacontact.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datacontact.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datacontact.Selenium_Selectors.firstname_input).send_keys(datacontact.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=datacontact.Selenium_Selectors.lastname_input).send_keys(datacontact.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.id_xpath).send_keys(datacontact.Sathesh_Data.id_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.save_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datacontact.Selenium_Selectors.contact_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.street_xpath).send_keys(datacontact.Sathesh_Data.street_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.street_1_xpath).send_keys(datacontact.Sathesh_Data.street_1_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.city_xpath).send_keys(datacontact.Sathesh_Data.city_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.state_xpath).send_keys(datacontact.Sathesh_Data.state_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.postal_code_xpath).send_keys(datacontact.Sathesh_Data.postal_code_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.country_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.home_no_xpath).send_keys(datacontact.Sathesh_Data.home_no_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.mobile_no_xpath).send_keys(datacontact.Sathesh_Data.mobile_no_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.work_no_xpath).send_keys(datacontact.Sathesh_Data.work_no_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.email_xpath).send_keys(datacontact.Sathesh_Data.email_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.email_1_xpath).send_keys(datacontact.Sathesh_Data.email_1_data)
        self.driver.find_element(by=By.XPATH, value=datacontact.Selenium_Selectors.save_1_xpath).click()
        time.sleep(7)
        print("Successfully all details filled in contact details page")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        