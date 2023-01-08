from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import datapersonal
import pytest
import time

class Test_Employee_Personal_Details:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
        
    def test_personal_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datapersonal.Selenium_Selectors.username_input).send_keys(datapersonal.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=datapersonal.Selenium_Selectors.password_input).send_keys(datapersonal.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datapersonal.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datapersonal.Selenium_Selectors.firstname_input).send_keys(datapersonal.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=datapersonal.Selenium_Selectors.lastname_input).send_keys(datapersonal.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.id_xpath).send_keys(datapersonal.Sathesh_Data.id_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.save_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datapersonal.Selenium_Selectors.personal_input).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.nickname_xpath).send_keys(datapersonal.Sathesh_Data.nickname_data)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.otherID_xpath).send_keys(datapersonal.Sathesh_Data.otherID_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.license_xpath).send_keys(datapersonal.Sathesh_Data.license_data)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.license_date_xpath).send_keys(datapersonal.Sathesh_Data.license_date_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.SSN_xpath).send_keys(datapersonal.Sathesh_Data.SSN_data)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.SIN_xpath).send_keys(datapersonal.Sathesh_Data.SIN_data)
        time.sleep(3)
        nationality_box = self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.national_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        marital_box = self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.marital_xpath)
        marital_box.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 200)")
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.male_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.date_xpath).send_keys(datapersonal.Sathesh_Data.birth_data)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.click_xpath)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datapersonal.Selenium_Selectors.save_xpath_1).click()
        time.sleep(7)
        print("Successfully all details filled in personal detail page #")
        
        
        
        
    
        