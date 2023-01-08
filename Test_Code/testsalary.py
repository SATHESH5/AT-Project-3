from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import datasalary
import pytest
import time

class Test_Empolyee_Salary_Details:
    
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield 
        self.driver.close()
        
        
    def test_salary_details(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datasalary.Selenium_Selectors.username_input).send_keys(datasalary.Sathesh_Data.username_data)
        self.driver.find_element(by=By.NAME, value=datasalary.Selenium_Selectors.password_input).send_keys(datasalary.Sathesh_Data.password_data)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.login_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.LINK_TEXT, value=datasalary.Selenium_Selectors.PIM_text).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.add_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=datasalary.Selenium_Selectors.firstname_input).send_keys(datasalary.Sathesh_Data.firstname_data)
        self.driver.find_element(by=By.NAME, value=datasalary.Selenium_Selectors.lastname_input).send_keys(datasalary.Sathesh_Data.lastname_data)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.id_xpath).send_keys('0')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.save_xpath).click()
        time.sleep(6)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.salary_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.add_1_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.component_xpath).send_keys(datasalary.Sathesh_Data.salary_data)
        pay_grade = self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.grade_xpath)
        pay_grade.send_keys(Keys.DOWN)
        pay_grade.click()
        time.sleep(2)
        pay_frequency = self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.frequency_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        currency_amount = self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.currency_xpath)
        currency_amount.send_keys('Ecuador Sucre')
        currency_amount.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.amount_xpath).send_keys(datasalary.Sathesh_Data.amount_data)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.comment_xpath).send_keys(datasalary.Sathesh_Data.comment_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.click_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.account_no_xpath).send_keys(datasalary.Sathesh_Data.Account_No_data)
        time.sleep(2)
        account_type = self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.account_xpath)
        time.sleep(2)
        account_type.send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.specify_xpath).send_keys(datasalary.Sathesh_Data.specify_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.routing_xpath).send_keys(datasalary.Sathesh_Data.routing_data)
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.amount_1_xpath).send_keys(datasalary.Sathesh_Data.amount_1_data)
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0,100)")
        self.driver.find_element(by=By.XPATH, value=datasalary.Selenium_Selectors.save_1_xpath).click()
        time.sleep(10)
        print("Successfully salary details filled in salary details page")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        