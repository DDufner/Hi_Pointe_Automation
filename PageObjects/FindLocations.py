from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class FindLocations: 
    find_locations_pickup_url = "https://hipointedrivein.appfront.app/find-location/?servingOptionType=pickup/"
    find_locations_delivery_url = "https://hipointedrivein.appfront.app/find-location/?servingOptionType=delivery/"
    
    #pickup option elements, NOTE: need to be confirmed
    enter_address_field = "//div/input[@id='mui-3']"
    enter_address_field_2 = "//div/input[@placeholder='Enter city, address or zip ']"
    locate_me_button = "//button/span[contains(text(),'Locate Me')]" #NOTE: this element will need a 'wait until clickable' function
    order_for_later_button = "//div/a[contains(text(),'Order for later')]" #NOTE: only available at off hours.  May need to create one for each location.
    location_select_location_button = "//div[@class='index-module--ListItemActions--1ae4c']" #NOTE: General, will need to index for each location. might be able to use locations names with this xpath nested in it instead of using indexing. try child to parent association?
    cottleville_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Cottleville')]"
    ballwin_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Ballwin')]"
    edwardsvile_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Edwardsville')]"
    kirkwood_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Kirkwood')]"
    mccausland_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'McCausland')]"
    ofallon_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'O'Fallon')]"
    district_chesterfield_location = "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'The District - Chesterfield')]"