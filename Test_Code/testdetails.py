from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import datadetails
import pytest
import time

class Test_Employee_Details:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_Employee_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datadetails.Selenium_Selectors.username_input).send_keys(datadetails.Sathesh_Data.username)
        self.driver.find_element(by=By.NAME, value=datadetails.Selenium_Selectors.password_input).send_keys(datadetails.Sathesh_Data.password)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datadetails.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datadetails.Selenium_Selectors.first_name).send_keys(datadetails.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=datadetails.Selenium_Selectors.middle_name).send_keys(datadetails.Sathesh_Data.middlename_data)
        self.driver.find_element(by=By.NAME, value=datadetails.Selenium_Selectors.last_name).send_keys(datadetails.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.id_xpath).send_keys(datadetails.Sathesh_Data.id_data)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.create_button_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.username_xpath).send_keys(datadetails.Sathesh_Data.username_data)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.password_xpath).send_keys(datadetails.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.conform_password_xpath).send_keys(datadetails.Sathesh_Data.conform_Password_data) 
        time.sleep(3)  
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.enabled_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.save_xpath).click()
        time.sleep(8)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.personal_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.contact_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.emergency_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.dependent_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.immegration_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.job_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.salary_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.tax_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.report_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.qualification_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,50)")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datadetails.Selenium_Selectors.membership_xpath).click()
        time.sleep(8)
        print("Successfully captured all taps present in employee details page")
        
        
        
        
        
        
        
        
        