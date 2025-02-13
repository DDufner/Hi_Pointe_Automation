from PageObjects.StartOrder import StartOrder
from PageObjects.GiftCard import GiftCard
from PageObjects.FindLocations import FindLocations
from PageObjects.ContactUs import ContactUs
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
        time.sleep(3)
        self.universalMethods.click_element(StartOrder.start_new_order_button)
        self.universalMethods.confirm_correct_URL(StartOrder.serving_options_url)
        self.driver.quit()

    def test_reorder_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(3)
        self.universalMethods.click_element(StartOrder.reorder_button)
        self.universalMethods.confirm_element_exists(StartOrder.modal_title_reorder_modal)
        self.driver.quit()

    def test_my_rewards_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(3)
        self.universalMethods.click_element(StartOrder.my_rewards_button)
        self.universalMethods.confirm_element_exists(StartOrder.modal_title_my_rewards_modal)
        self.driver.quit()
    
    def test_powered_by_link(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.click_element(StartOrder.powered_by_appfront_link)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.universalMethods.confirm_correct_URL(StartOrder.powered_by_appfront_url)
        self.driver.quit()
    
    def test_terms_of_service_link(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.click_element(StartOrder.terms_of_service_link)
        self.universalMethods.confirm_correct_URL(StartOrder.tos_base_url)
        time.sleep(5)        
        self.driver.quit()

    def test_privacy_policy_link(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(5)
        self.universalMethods.click_element(StartOrder.privacy_policy_link)
        print(StartOrder.privacy_policy_link_url)
        print("CHECK THIS VALUE: " + StartOrder.privacy_policy_link_url_cp)
        self.universalMethods.confirm_correct_URL(StartOrder.privacy_policy_link_url_cp)
        time.sleep(5)
        self.driver.quit()

    def test_login_icon(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.driver.get(StartOrder.start_order_url)
        time.sleep(5)
        self.universalMethods.click_element(StartOrder.profile_login_button)
        self.universalMethods.confirm_element_exists(StartOrder.modal_title_login_modal)
        self.driver.quit()

    def test_contact_us_button(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)  
        self.contactUs = ContactUs(self.driver) 
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.click_element(StartOrder.contact_us_button)
        time.sleep(2)
        self.universalMethods.confirm_correct_URL(ContactUs.contact_us_url)
        self.driver.quit()

    def test_send_a_gift_card(self, driver_setup):
        self.driver = driver_setup
        self.startOrder = StartOrder(self.driver)
        self.universalMethods = UniversalMethods(self.driver)   
        self.giftCard = GiftCard(self.driver)
        self.driver.get(StartOrder.start_order_url)
        time.sleep(2)
        self.universalMethods.click_element(StartOrder.send_a_gift_card_button)
        time.sleep(2)
        self.universalMethods.confirm_correct_URL(GiftCard.gift_card_url)
        self.driver.quit()

    def test_valid_address_returns_delivery_locations(self, driver_setup):
        self.driver = driver_setup
        self.findLocations = FindLocations(self.driver)
        self.universalMethods = UniversalMethods(self.driver)
        self.driver.get(FindLocations.delivery_url)
        time.sleep(3)
        self.universalMethods.enter_value(FindLocations.delivery_address_field, FindLocations.valid_test_address)
        time.sleep(3)
        self.findLocations.print_all_delivery_locations(FindLocations.delivery_location_name_element)
        time.sleep(5)

        #self.universalMethods.confirm_element_exists(FindLocations.generic_location_element)
        location_name = self.driver.find_element(By.XPATH, "//span[contains(text(),'Wash Ave')]")
        print("The name of the first suggested location is "+location_name.text)
        self.driver.quit() 