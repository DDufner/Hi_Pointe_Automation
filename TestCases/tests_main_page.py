from PageObjects.MainPage import MainPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  
import time

class Test_001_Main_Page_General:

    def test_confirm_main_page_url(self, driver_setup):
        driver = driver_setup
        #mainPage = MainPage(driver)
        driver.get(MainPage.main_page_url)
        if driver.current_url == "https://hipointedrivein.com/":
            assert True
        else:
            assert False
        driver.quit()

    def test_confirm_menu_modal_opens(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.driver.get(MainPage.main_page_url)
        MainPage.clickElement(self, MainPage.navigation_menu_icon)
        time.sleep(2)
        MainPage.confirmElementExists(self, MainPage.hi_pointe_icon_modal_link)
        # try:
        #     self.driver.quit()
        #     assert True
        # except:
        #     print("element is not clickable! oh no!") 
        #     self.driver.quit()
        #     assert False
    
    def test_confirm_single_modal_element(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.driver.get(MainPage.main_page_url)
        MainPage.clickElement(self, MainPage.navigation_menu_icon)
        try:
            MainPage.clickElement(self, MainPage.our_story_modal_link)
            assert True
        except:
            print("something went wrong!") 
            assert False

    def test_confirm_list_of_elements(self, driver_setup):
        self.driver = driver_setup
        self.mainPage = MainPage(self.driver)
        self.driver.get(MainPage.main_page_url)
        MainPage.confirmListOfElementsExist(self, MainPage.navigation_modal_links_list)