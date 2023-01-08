from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Test_Data import datauser
import pytest
import time

class Test_User_Admin:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_user_management(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datauser.Selenium_Selectors.username_input).send_keys(datauser.Sathesh_Data.username)
        self.driver.find_element(by=By.NAME, value=datauser.Selenium_Selectors.password_input).send_keys(datauser.Sathesh_Data.password)
        self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.admin_text).click()
        time.sleep(4)
        user_management = self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.user_management_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=user_management).perform()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.users_xpath).click()
        time.sleep(3)
        a_user_role = self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.user_role_xpath)
        a_user_role.send_keys(Keys.DOWN)
        a_user_role.click()
        time.sleep(2)
        a_status_role = self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.status_xpath)
        a_status_role.send_keys(Keys.DOWN)
        a_status_role.click()
        time.sleep(3)
        user_role = self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.user_role_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        status_role = self.driver.find_element(by=By.XPATH, value=datauser.Selenium_Selectors.status_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(5)
        print("Successfully captured user_role and status_role dropdown")
        
        
        
        
        
   
        

        
        