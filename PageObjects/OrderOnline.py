from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class OrderOnline: 
    order_online_url = "https://hipointedrivein.appfront.app/?openSignup=true"
    
    #get_started_modal = "//*[@id='app']/div[2]/div/div/div/div/div" #auto suggest from copilot
    login_button_get_started_modal = "//a[@class='index-module--Button--6cadf noselect index-module--Centered--18426 index-module--Slim--707a7']"
    full_name_field_get_started_modal = "//input[@name='fullname']"
    phone_number_field_get_started_modal = "//input[@name='phone']"
    email_address_field_get_started_modal = "//input[@name='email']"
    month_dropdown_get_started_modal = "//div[@id='select-jh0buhah6']" 
    day_dropdown_get_started_modal = "//div[@id='select-jh0buhah7']"
    signup_button_get_started_modal = "//a[@class='index-module--Button--6cadf noselect index-module--Centered--18426']"