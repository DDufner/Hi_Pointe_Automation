from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)



class StartOrder: 
    start_order_url = "https://hipointedrivein.appfront.app/"
    start_order_url_with_get_started_modal = "https://hipointedrivein.appfront.app/?openSignup=true"
    
    #sign up modal elements
    signup_modal = "//div[@class='slick-slide slick-active slick-current']//div//div[@tabindex='-1']"
    close_button_signup_modal = "//button[@id='close-btn']"
    login_button_signup_modal = "//a[contains(text(),'Login')]"
    full_name_field_signup_modal = "//input[@name='fullname']"
    phone_number_field_signup_modal = "//input[@name='phone']"
    email_address_field_signup_modal = "//input[@name='email']"
    month_dropdown_signup_modal = "//div[contains(text(),'Month')]" 
    day_dropdown_signup_modal = "//div[contains(text(),'Day')]"
    year_dropdown_signup_modal = "//div[contains(text(),'Year')]"
    signup_button_signup_modal = "//a[@class='index-module--Button--6cadf noselect index-module--Centered--18426']"
    terms_of_service_link_signup_modal = "//a[contains(text(),'Terms of Service')]"
    privacy_policy_link_signup_modal = "//a[contains(text(),'Privacy Policy')]"
    skip_button_signup_modal = "//small[contains(text(),'Skip')]"

    #start order main page elements
    back_button = "//a/span[contains(text(),'Back')]" #NOTE: this only appears after naving to another page
    profile_login_button = "//div[@class='HeaderUserProfileLink-module--user--c70d8']"
    contact_us_button = "//div[@class='index-module--AttachedContent--212be index-module--TopSideButtons--965e5']//a[contains(text(),'Contact Us')]"
    contact_us_url = "https://hipointedrivein.appfront.app/contact-us/"
    send_a_gift_card_button = "//div[@class='index-module--AttachedContent--212be index-module--TopSideButtons--965e5']//a[contains(text(),'Send a Gift Card')]"
    image_button = "//img[@class='MuiAvatar-img mui-1hy9t21']"
    image_close_button = "//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium mui-vubbuv']"

    #start order left nav elements
    start_new_order_button = "//a/span[contains(text(),'Start New Order')]"
    serving_options_url = "https://hipointedrivein.appfront.app/serving-options/"
    pickup_button = "//a/div/span[contains(text(),'Pickup')]"
    delivery_button = "//a/div/span[contains(text(),'Delivery')]" 
    reorder_button = "//a/span[contains(text(),'Reorder')]"
    my_rewards_button = "//a/span[contains(text(),'My Rewards')]"

    #reorder modal elements
    close_button_reorder_modal = "//div/button[@id='close-btn']"
    modal_title_reorder_modal = "//div/p[contains(text(),'Login to see your previous orders')]"
    phone_number_field_reorder_modal = "//span/input[@name='phone']"
    login_button_reorder_modal = "//div/a[contains(text(),'Login')]"
    sign_up_button_reorder_modal = "//div/p/a[contains(text(),'Sign up')]"

    #my rewards modal elements 
    close_button_my_rewards_modal = "//button[@id='close-btn']"
    modal_title_my_rewards_modal = "//div/p[contains(text(),'Login to see your rewards and feel the love')]"
    phone_number_field_my_rewards_modal = "//span/input[@name='phone']"
    login_button_my_rewards_modal = "//div/a[contains(text(),'Login')]"
    sign_up_button_my_rewards_modal = "//div/p/a[contains(text(),'Sign up')]"

    #login modal elements
    close_button_login_modal = "//button[@id='close-btn']"
    modal_title_login_modal = "//div/p[contains(text(),'Login for faster ordering and special rewards.')]"
    phone_number_field_login_modal = "//input[@type='tel']"
    login_button_login_modal = "//div/a[contains(text(),'Login')]"
    sign_up_button_login_modal = "//div/p/a[contains(text(),'Sign up')]"
    skip_button_login_modal = "//small[contains(text(),'Skip')]"    

    #links at bottom of page
    powered_by_appfront_link = "//span[contains(text(),'Powered by')]"
    powered_by_appfront_url = "https://www.appfront.ai/?src=pwrdby"
    terms_of_service_link = "//span[contains(text(),'Terms of Service')]"

    tos_base_url = "https://hipointedrivein.appfront.app/tos/"
    back_path = "2F/"
    encoded_back_path = quote(back_path)
    terms_of_service_link_url_2 = f"{tos_base_url}?backPath=%{encoded_back_path}"

    privacy_policy_link = "//span[contains(text(),'Privacy Policy')]" 
    privacy_policy_link_url = "https://hipointedrivein.appfront.app/privacy-policy/"
    privacy_policy_link_url_2 = "https://hipointedrivein.appfront.app/privacy-policy/?backPath=%2F/"
    #NOTE: for fixing URL issue on privacy policy and tos URLs: https://stackoverflow.com/questions/1695183/how-can-i-percent-encode-url-parameters-in-python 
