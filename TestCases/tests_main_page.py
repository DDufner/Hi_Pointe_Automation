from PageObjects.MainPage import MainPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
from selenium import webdriver
import time

class Test_001_Main_Page_General:

    def test_confirm_main_page_url(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.driver.get(MainPage.main_page_url)
        if self.driver.current_url == "https://hipointedrivein.com/":
            print("URL is correct!")
            assert True
        else:
            assert False
        self.driver.quit()

    def test_confirm_menu_modal_opens(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.driver.get(MainPage.main_page_url)
        MainPage.clickElement(self, MainPage.navigation_menu_icon)
        time.sleep(2)
        try: 
            MainPage.confirmElementExists(self, MainPage.hi_pointe_icon_modal_link)
            assert True
            print("Modal opened successfully!")
        except: 
            print("Hi Pointe icon not found, modal not opened") 
            assert False
        self.driver.quit()

    def test_confirm_single_modal_element(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.driver.get(MainPage.main_page_url)
        self.mainPage.clickElement(MainPage.navigation_menu_icon)
        try:
            self.mainPage.clickElement(MainPage.our_story_modal_link)
            assert True
            print("Successful navigation to Our Story page from navigation modal.")
        except:
            print("something went wrong!") 
            assert False

       
        #MainPage.confirmElementExists(self, MainPage.hi_pointe_icon_modal_link)
        # try:
        #     self.driver.quit()
        #     assert True
        # except:
        #     print("element is not clickable! oh no!") 
        #     self.driver.quit()
        #     assert False

    # def test_confirm_list_of_elements(self, driver_setup):
    #     self.driver = driver_setup
    #     self.mainPage = MainPage(self.driver)
    #     self.driver.get(MainPage.main_page_url)
    #     MainPage.confirmListOfElementsExist(self, MainPage.navigation_modal_links_list)