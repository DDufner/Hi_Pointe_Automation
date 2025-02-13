from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class GiftCard: 
    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver = driver
        
    gift_card_url = "https://hipointedrivein.appfront.app/gift-card/"
    