from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class ContactUs: 
    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver = driver
        
    contact_us_url = "https://hipointedrivein.appfront.app/contact-us/"
    contact_us_header = "//span[contains(text(),'Contact Us')]"
    order_experience_radio = "//span[contains(text(),'Order Experience')]"
    food_quality_radio = "//span[contains(text(),'Food Quality')]"
    app_or_web_radio = "//span[contains(text(),'App or Web')]"
    on_your_mind_other_radio = "//div[@class='index-module--CardContent--b60d5']//span[contains(text(),'Other')]" 