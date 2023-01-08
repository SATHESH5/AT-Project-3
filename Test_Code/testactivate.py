from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import dataactivate
import pytest
import time

class Test_Employment_Termination_And_Activation:
    
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
        
    def test_termination_activation(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataactivate.Selenium_Selectors.username_input).send_keys(dataactivate.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=dataactivate.Selenium_Selectors.password_input).send_keys(dataactivate.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataactivate.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataactivate.Selenium_Selectors.firstname_input).send_keys(dataactivate.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=dataactivate.Selenium_Selectors.lastname_input).send_keys(dataactivate.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.id_xpath).send_keys(dataactivate.Sathesh_Data.id_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.save_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.job_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.joined_data_xpath).send_keys(dataactivate.Sathesh_Data.joined_date_data)
        job_title = self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.job_1_xpath)
        job_title.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(5)
        job_catagery = self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.catagery_xpath)
        job_catagery.send_keys(Keys.DOWN)
        job_catagery.click()
        time.sleep(2)
        sub_unit = self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.sub_unit_xpath)
        sub_unit.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        location = self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.location_xpath)
        location.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        employment_status = self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.status_xpath)
        employment_status.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.save_1_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.terminate_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.terminate_1_xpath).send_keys(dataactivate.Sathesh_Data.terminiate_date_data)
        time.sleep(2)
        terminate_role = self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.terminate_2_xpath)
        terminate_role.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.note_xpath).send_keys(dataactivate.Sathesh_Data.note_text)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.save_2_xpath).click()
        time.sleep(7)
        self.driver.find_element(by=By.XPATH, value=dataactivate.Selenium_Selectors.activate_xpath).click()
        time.sleep(7)
        print("Employment termination and activation successfully")
        
        
        
        
        
        
        
        
        