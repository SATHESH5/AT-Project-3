from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Test_Data import dataPIM
import pytest
import time

class Test_PIM:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_orangeHRM_Admin(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=dataPIM.Selenium_Selectors.username_input).send_keys(dataPIM.Sathesh_Data.username)
        self.driver.find_element(by=By.NAME, value=dataPIM.Selenium_Selectors.password_input).send_keys(dataPIM.Sathesh_Data.password)
        self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Admin').perform()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.admin_xpath).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('PIM').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Leave').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.leave_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Time').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.time_text).click()
        time.sleep(3)
        
                
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Recruitment').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.recruitment_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('My Info').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.myinfo_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Performance').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.performance_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Dashboard').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.dashboard_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Directory').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.directory_text).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Maintenance').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.maintenance_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.cancel_button).click()
        time.sleep(3)
        
        search_box = self.driver.find_element(by=By.XPATH, value=dataPIM.Selenium_Selectors.search_xpath)
        action = ActionChains(self.driver)
        action.click(on_element=search_box).send_keys('Buzz').perform()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=dataPIM.Selenium_Selectors.buzz_text).click()
        time.sleep(6)
        print("Successfully all under the text name to be captured in search text box #")
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
        
        
        
        
        
        
        
           