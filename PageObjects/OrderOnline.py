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
    
    #get started modal elements
    #get_started_modal = "//*[@id='app']/div[2]/div/div/div/div/div" #auto suggest from copilot
    get_started_modal_close_button = "//button[@id='close-btn']"
    login_button_get_started_modal = "//a[contains(text(),'Login')]"
    full_name_field_get_started_modal = "//input[@name='fullname']"
    phone_number_field_get_started_modal = "//input[@name='phone']"
    email_address_field_get_started_modal = "//input[@name='email']"
    #having difficulty with getting month/day/year drop down elements to work
    month_dropdown_get_started_modal = "//div[@id='select-jh0buhah6']" 
    day_dropdown_get_started_modal = "//div[@id='select-jh0buhah7']"
    signup_button_get_started_modal = "//a[@class='index-module--Button--6cadf noselect index-module--Centered--18426']"
    #...
    signup_button_get_started_modal = "//a[@class='index-module--Button--6cadf noselect index-module--Centered--18426']"
    terms_of_service_link_get_started_modal = "//a[contains(text(),'Terms of Service')]"
    privacy_policy_link_get_started_modal = "//a[contains(text(),'Privacy Policy')]"
    skip_button_get_started_modal = "//small[contains(text(),'Skip')]"