from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import datatax
import pytest
import time

class Test_Employee_Tax_Exemptions:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_tax_exemptions(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datatax.Selenium_Selectors.username_input).send_keys(datatax.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=datatax.Selenium_Selectors.password_input).send_keys(datatax.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datatax.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datatax.Selenium_Selectors.firstname_input).send_keys(datatax.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=datatax.Selenium_Selectors.lastname_input).send_keys(datatax.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.id_xpath).send_keys(datatax.Sathesh_Data.id_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.save_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.tax_xpath).click()
        time.sleep(5)
        status_role = self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.status_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.exemptions_xpath).send_keys(datatax.Sathesh_Data.exemptions_data)
        time.sleep(2)
        state_role = self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.state_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        status_1_role = self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.status_1_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.exemptions_1_xpath).send_keys(datatax.Sathesh_Data.exemptions_1_data)
        time.sleep(3)
        unemployment_state = self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.unemployment_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        work_state = self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.work_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datatax.Selenium_Selectors.save_1_xpath).click()
        time.sleep(5)
        print("Successfully salary details filled in Tax exemptions details page")
        
        
        
        
        
        
        
        
        