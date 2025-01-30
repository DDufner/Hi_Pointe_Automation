from PageObjects.MainPage import MainPage
from PageObjects.UniversalMethods import UniversalMethods
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
from selenium import webdriver
import time

class Test_001_Main_Page_General:

    def test_confirm_main_page_url(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.universalMethods = UniversalMethods(self.driver)  
        self.driver.get(MainPage.main_page_url)
        self.universalMethods.confirm_correct_URL(MainPage.main_page_url)
        self.driver.quit()

    def test_confirm_menu_modal_opens(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.universalMethods = UniversalMethods(self.driver)  
        self.driver.get(MainPage.main_page_url)
        self.universalMethods.click_element(MainPage.navigation_menu_icon)
        time.sleep(2)
        self.universalMethods.confirm_element_exists(MainPage.hi_pointe_icon_modal_link)
        self.driver.quit()

    def test_confirm_single_modal_element(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.universalMethods = UniversalMethods(self.driver)  
        self.driver.get(MainPage.main_page_url)
        self.universalMethods.click_element(MainPage.navigation_menu_icon)
        self.universalMethods.confirm_element_exists(MainPage.our_story_modal_link)
        self.driver.quit()  

    def test_confirm_list_of_elements(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.universalMethods = UniversalMethods(self.driver) 
        self.driver.get(MainPage.main_page_url)
        self.universalMethods.confirm_list_of_elements_exist(MainPage.navigation_modal_links_list)
        self.driver.quit() 