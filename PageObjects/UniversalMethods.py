from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException

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

    def click_element_and_back(self, element):
        driver.find_element(By.XPATH, value=element).click()
        driver.back()

    def confirm_element_exists(self, target_element):
        try:
            target_element = self.driver.find_element(By.XPATH, value=target_element)
            driver.quit()
            assert True
        except NoSuchElementException:
            print("Element not found.")
            assert False  

    def confirm_correct_URL(self, target_url):
        if self.driver.current_url == target_url:
            print("URL is correct!")
            assert True
        else:
            assert False

    def confirm_list_of_elements_exist(self, target_elements_list):
        for item in target_elements_list:
            try:
                item = self.driver.find_element(By.XPATH, value=item)
            except NoSuchElementException:
                assert False, f"Element not found: {item}"
        assert True
  