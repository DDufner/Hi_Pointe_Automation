from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class UniversalMethods:
    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver = driver

    def click_element(self, element):
        self.driver.find_element(By.XPATH, value=element).click()

    #wait function isn't working yet, needs more tweaking.  
    def wait_for_element(self, element):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(By.XPATH, value = element))
        except:
            print("Element not found within the specified time.")
            driver.quit()
    ###

    def enter_value(self, element, value):
        self.driver.find_element(By.XPATH, value=element).send_keys(value)

    def click_element_and_back(self, element):
        driver.find_element(By.XPATH, value=element).click()
        driver.back()

    def confirm_element_exists(self, target_element):
        try:
            target_element = self.driver.find_element(By.XPATH, value=target_element)
            print("Element found.")
            assert True
        except NoSuchElementException:
            print("Element not found.")
            driver.quit()
            assert False  

    def confirm_correct_URL(self, target_url):
        if self.driver.current_url == target_url:
            print("URL is correct.")
            assert True
        else:
            print("URL does not match.")
            driver.quit()
            assert False

    def confirm_list_of_elements_exist(self, target_elements_list):
        for item in target_elements_list:
            try:
                item = self.driver.find_element(By.XPATH, value=item)
            except NoSuchElementException:
                driver.quit()
                assert False, f"Element not found: {item}"
        assert True

    def collect_data_into_list(self, target_elements):
        data = self.driver.find_element(By.XPATH, target_elements)
        
  