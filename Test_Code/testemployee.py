from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import dataemployee
import pytest
import time

class Test_Add_Employee:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_Add_Employee(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataemployee.Selenium_Selectors.username_input).send_keys(dataemployee.Sathesh_Data.username)
        self.driver.find_element(by=By.NAME, value=dataemployee.Selenium_Selectors.password_input).send_keys(dataemployee.Sathesh_Data.password)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataemployee.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataemployee.Selenium_Selectors.first_name).send_keys(dataemployee.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=dataemployee.Selenium_Selectors.middle_name).send_keys(dataemployee.Sathesh_Data.middlename_data)
        self.driver.find_element(by=By.NAME, value=dataemployee.Selenium_Selectors.last_name).send_keys(dataemployee.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.id_xpath).send_keys(dataemployee.Sathesh_Data.id_data)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.create_button_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.username_xpath).send_keys(dataemployee.Sathesh_Data.username_data)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.password_xpath).send_keys(dataemployee.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.conform_password_xpath).send_keys(dataemployee.Sathesh_Data.conform_Password_data) 
        time.sleep(3)  
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.enabled_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataemployee.Selenium_Selectors.save_xpath).click()
        time.sleep(8)
        print("Successfully add Employee details to the Employee List")
        
        
        
        
        
        
        