from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class FindLocations: 
    def __init__(self, driver): #constructor that invokes objects for main page class.  
        self.driver = driver

    find_locations_pickup_url = "https://hipointedrivein.appfront.app/find-location/?servingOptionType=pickup/"
    find_locations_delivery_url = "https://hipointedrivein.appfront.app/find-location/?servingOptionType=delivery/"
    
    #pickup option elements, NOTE: need to be confirmed
    pickup_button = "//span[contains(text(),'Pickup')]"
    pickup_tab = "//li[@id='react-tabs-16']"
    enter_address_field = "//div/input[@id='mui-3']"
    enter_address_field_2 = "//div/input[@placeholder='Enter city, address or zip ']"
    locate_me_button = "//button/span[contains(text(),'Locate Me')]" #NOTE: this element will need a 'wait until clickable' function
    order_for_later_button = "//div/a[contains(text(),'Order for later')]" #NOTE: only available at off hours.  May need to create one for each location.
    location_select_location_button = "//div[@class='index-module--ListItemActions--1ae4c']" #NOTE: General, will need to index for each location. might be able to use locations names with this xpath nested in it instead of using indexing. try child to parent association?

    #delivery option elements, NOTE: need to be confirmed
    delivery_url = "https://hipointedrivein.appfront.app/find-location/?servingOptionType=delivery/"
    delivery_button = "//span[contains(text(),'Delivery')]"
    delivery_tab = "//li[@id='react-tabs-18']"
    delivery_address_field = "//input[@id='mui-3']"
    delivery_address_field_clear_button = "//button[@type='button']//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium mui-vubbuv']"
    delivery_first_address_suggestion = "//ul//li[@id='react-autowhatever-1--item-0']"
    valid_test_address = "6161 Delmar Blvd. St. Louis, MO 63112"
    invalid_test_address = "1110 Stone Hill Hwy, Hermann, MO 65041"
    no_locations_found_message = "//div[@class='index-module--ErrorMessage--f938d']"
    delivery_location_name_element = "//div[@class='index-module--ListCard--b1bd3 index-module--HasErrors--60a1c']//div[@class='index-module--ListCardTitle--a9e35']"


    #location elements 
    generic_location_element = "//a[@class='index-module--ListCard--b1bd3']"
    ballwin_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Ballwin')]"
    cottleville_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Cottleville')]"
    edwardsvile_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Edwardsville')]"
    kirkwood_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Kirkwood')]"
    mccausland_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'McCausland')]"
    ofallon_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'O'Fallon')]"
    district_chesterfield_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'The District - Chesterfield')]"
    wash_ave_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Wash Ave')]"

    def print_all_delivery_locations(self, target_element):
        print("start list creation")
        delivery_location_list = self.driver.find_elements(By.XPATH, target_element.text)
        print("end list creation")
        print(delivery_location_list)
        for item in delivery_location_list:
            print("location: " + item.text)
            driver.quit
        else:
            assert False
        