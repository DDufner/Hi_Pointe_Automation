from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class StartOrder: 
    order_online_url = "https://hipointedrivein.appfront.app/"
    order_online_url_with_get_started_modal = "https://hipointedrivein.appfront.app/?openSignup=true"
    
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
    send_a_gift_card_button = "//div[@class='index-module--AttachedContent--212be index-module--TopSideButtons--965e5']//a[contains(text(),'Send a Gift Card')]"
    image_button = "//img[@class='MuiAvatar-img mui-1hy9t21']"
    image_close_button = "//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium mui-vubbuv']"

    #start order left nav elements
    start_new_order_button = "//a/span[contains(text(),'Start New Order')]"
    pickup_button = "//a/div/span[contains(text(),'Pickup')]"
    delivery_button = "//a/div/span[contains(text(),'Delivery')]" 
    reorder_button = "//a/span[contains(text(),'Reorder')]"
    my_rewards_button = "//a/span[contains(text(),'My Rewards')]"

    #reorder modal elements
    login_modal_close_button = "//div/button[@id='close-btn']"
    login_modal_phone_number_field = "//span/input[@name='phone']"
    login_modal_login_button = "//div/a[contains(text(),'Login')]"
    login_modal_sign_up_button = "//div/p/a[contains(text(),'Sign up')]"

    #my rewards modal elements 
    my_rewards_modal_close_button = "//button[@id='close-btn']"
    my_rewards_modal_phone_number_field = "//span/input[@name='phone']"
    my_rewards_modal_login_button = "//div/a[contains(text(),'Login')]"
    my_rewards_modal_sign_up_button = "//div/p/a[contains(text(),'Sign up')]"

    #login modal elements
    login_modal_close_button = "//button[@id='close-btn']"
    login_modal_phone_number_field = "//input[@type='tel']"
    login_modal_login_button = "//div/a[contains(text(),'Login')]"
    login_modal_sign_up_button = "//div/p/a[contains(text(),'Sign up')]"
    login_modal_skip_button = "//small[contains(text(),'Skip')]"    

    #links at bottom of page
    powered_by_appfront_link = "//span[contains(text(),'Powered by')]"
    terms_of_service_link = "//span[contains(text(),'Terms of Service')]"
    privacy_policy_link = "//span[contains(text(),'Privacy Policy')]" 

    #NOTE: Need to move these to different object class
    enter_address_field = "//div/input[@id='mui-19']"
    enter_address_field2 = "//div/input[@placeholder='Enter city, address or zip ']"
    locate_me_button = "//button/span[contains(text(),'Locate Me')]" #NOTE: this element will need a 'wait until clickable' function
    order_for_later_button = "//div/a[contains(text(),'Order for later')]" #NOTE: only available at off hours.  May need to create one for each location.
    location_select_location_button = "//div[@class='index-module--ListItemActions--1ae4c']" #NOTE: General, will need to index for each location. might be able to use locations names with this xpath nested in it instead of using indexing. try child to parent association?
    cottleville = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Cottleville')]"