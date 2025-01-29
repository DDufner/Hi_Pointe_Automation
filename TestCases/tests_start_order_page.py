from PageObjects.StartOrder import StartOrder
from PageObjects.UniversalMethods import UniversalMethods
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
from selenium import webdriver
import time

class Test_002_Start_Order_General_Tests:

    def test_start_new_order_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.clickElement(StartOrder.start_new_order_button)
        self.universalMethods.confirmCorrectURL(StartOrder.serving_options_url)
        self.driver.quit()

    def test_reorder_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.clickElement(StartOrder.reorder_button)
        self.universalMethods.confirmElementExists(StartOrder.modal_title_reorder_modal)
        self.driver.quit()

    def test_my_rewards_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.clickElement(StartOrder.my_rewards_button)
        self.universalMethods.confirmElementExists(StartOrder.modal_title_my_rewards_modal)
        self.driver.quit()
    
    def test_powered_by_link(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.clickElement(StartOrder.powered_by_appfront_link)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.universalMethods.confirmCorrectURL(StartOrder.powered_by_appfront_url)
        self.driver.quit()
    
    def test_terms_of_service_link(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.clickElement(StartOrder.terms_of_service_link)
        self.universalMethods.confirmCorrectURL(StartOrder.tos_base_url)
        time.sleep(5)        
        self.driver.quit()

    def test_privacy_policy_link(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(5)
        self.universalMethods.clickElement(StartOrder.privacy_policy_link)
        print(StartOrder.privacy_policy_link_url)
        self.universalMethods.confirmCorrectURL(StartOrder.privacy_policy_link_url)
        time.sleep(5)
        self.driver.quit()

    def test_login_icon(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(5)
        self.universalMethods.clickElement(StartOrder.profile_login_button)
        self.universalMethods.confirmElementExists(StartOrder.modal_title_login_modal)
        self.driver.quit()

    def test_contact_us_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.clickElement(StartOrder.contact_us_button)
        time.sleep(2)
        self.universalMethods.confirmCorrectURL(StartOrder.contact_us_url)
        self.driver.quit()