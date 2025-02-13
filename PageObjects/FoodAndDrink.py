from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action = ActionChains(driver)

class FoodAndDrink:
    food_and_drink_url = "https://hipointedrivein.com/menu/"
    instagram_icon_food_and_drink = "//img[@src='https://hipointedrivein.com/wp-content/uploads/2017/04/hpdi_post-500x500.jpg']"
    burgers_menu_section_header = "//h2[contains(text(),'Burgers')]"
    sandwiches_menu_section_header = "//h2[contains(text(),'Sandwiches')]"
    salads_menu_section_header = "//h2[contains(text(),'Salads')]"
    sides_menu_section_header = "//h2[contains(text(),'Sides')]"
    kids_menu_section_header = "//h2[contains(text(),'Kids')]"
    shakes_and_soda_menu_section_header = "//h2[contains(text(),'Shakes & Soda Floats')]"