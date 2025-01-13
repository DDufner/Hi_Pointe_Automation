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
action=ActionChains(driver)

class MainPage:
    main_page_url = "https://hipointedrivein.com/"

    #main view, links below still need to be tested and confirmed
    navigation_menu_icon = "//strong[contains(text(),'Nav')]"
    order_online_link = "//a[@id='order-online-trigger']"
    food_and_drink_image = "//a[@id='home-grid-block-1']" 
    our_story_image = "//a[@id='home-grid-block-2']"
    catering_image = "//a[@id='home-grid-block-4']"
    delivery_image = "//a[@id='home-grid-block-3']"
    locations_and_contact_image = "//a[@id='home-grid-block-5']"
    
    #navigation menu modal elements.  NOTE: all will be 'visible' by xpath but not clickable unless user opens menu modal.
    our_story_modal_link = "//a[contains(text(),'Our Story')]"
    food_and_drink_modal_link = "//a[contains(text(),'Food & Drink')]"
    locations_modal_link = "//a[contains(text(),'Locations')]"
    catering_modal_link = "//a[contains(text(),'Catering')]"
    order_online_modal_link = "//li[@class='main-nav-item']//a[contains(text(),'Order Online')]"
    in_the_press_modal_link = "//a[contains(text(),'In The Press')]"
    job_openings_modal_link = "//a[contains(text(),'Job Openings')]"
    buy_gift_cards_modal_link = "//a[contains(text(),'Buy Gift Cards')]"
    hi_pointe_icon_modal_link = "//*[@id='logo-nav']"

    instagram_modal_icon_modal_link = "//div[@id='home-grid-social']//span[@class='fa fa-instagram']"
    facebook_modal_icon_modal_link = "//div[@id='home-grid-social']//span[@class='fa fa-facebook']"
    twitter_modal_icon_modal_link = "//div[@id='home-grid-social']//span[@class='fa fa-twitter']']"

    #List for testing of all navigation modal links
    navigation_modal_links_list = [our_story_modal_link, food_and_drink_modal_link, locations_modal_link, catering_modal_link, 
                             order_online_modal_link, in_the_press_modal_link, job_openings_modal_link, buy_gift_cards_modal_link, 
                             instagram_modal_icon_modal_link, facebook_modal_icon_modal_link, twitter_modal_icon_modal_link, 
                             hi_pointe_icon_modal_link]

    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver = driver

    # nav modal links
    def clickElement(self, element):
        driver.find_element(By.XPATH, value=element).click()

    def clickElementAndBack(self, element):
        driver.find_element(By.XPATH, value=element).click()
        driver.back()

    def confirmElementExists(self, target_element):
        try:
            target_element = self.driver.find_element(By.XPATH, value=target_element)
            driver.quit()
            assert True
        except NoSuchElementException:
            print("Element not found.")
            assert False  

    def confirmListOfElementsExist(self, target_elements_list):
        for item in target_elements_list:
            try:
                item = self.driver.find_element(By.XPATH, value=item)
            except NoSuchElementException:
                assert False, f"Element not found: {item}"
        assert True

    #NOTE: below methods are most likely not needed and replaced by 'clickecElement' method above.
    # def clickNavigation(self):
    #     self.driver.find_element(By.XPATH, value=self.navigation_menu_icon).click()

    # def clickOurStoryNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.our_story_modal_link).click()

    # def clickFoodAndDrinkNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.food_and_drink_modal_link).click()

    # def clickLocationsNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.locations_modal_link).click() 
    
    # def clickCateringNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.catering_modal_link).click()

    # def clickOrderOnlineNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.order_online_modal_link).click()

    # def clickInThePressNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.in_the_press_modal_link).click()

    # def clickJobOpeningsNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.job_openings_modal_link).click()
    
    # def clickBuyGiftCardsNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.buy_gift_cards_modal_link).click()
    # #social media icons in nav modal
    # def clickInstagramNavModal(self):   
    #     self.driver.find_element(By.XPATH, value=self.instagram_modal_icon_modal_link).click()
    
    # def clickFacebookNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.facebook_modal_icon_modal_link).click()

    # def clickTwitterNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.twitter_modal_icon_modal_link).click()

    # def clickHiPointeNavModal(self):
    #     self.driver.find_element(By.XPATH, value=self.hi_pointe_icon_modal_link).click()
