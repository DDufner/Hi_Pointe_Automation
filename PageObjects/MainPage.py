from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action=ActionChains(driver)

class MainPage:
    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver = driver

    main_page_url = "https://hipointedrivein.com/"
    submit_application_banner_close_button = "//a[@class='close']"
    navigation_menu_icon = "//a[@id='nav-trigger']" 
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
    twitter_modal_icon_modal_link = "//div[@class='main-nav-right main-nav-panel']//ul[@class='social-nav']//li[@class='social-nav-twitter']"

    #List for testing of all navigation modal links
    navigation_modal_links_list = [our_story_modal_link, food_and_drink_modal_link, locations_modal_link, catering_modal_link, 
                             order_online_modal_link, in_the_press_modal_link, job_openings_modal_link, buy_gift_cards_modal_link, 
                             instagram_modal_icon_modal_link, facebook_modal_icon_modal_link, twitter_modal_icon_modal_link, 
                             hi_pointe_icon_modal_link]