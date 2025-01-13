from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By  
import time

#Chome option
#service = Service(executable_path='/Users/dominickdufner/Coding/chromedriver')
#chrome_options = Options()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service)
#action=ActionChains(driver)

#Firefox option
service = Service(executable_path='/Users/dominickdufner/Coding/eclipse-2023-workspace/geckodriver')
firefox_options = Options()
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service)
action=ActionChains(driver)


driver.get("https://hipointedrivein.com/menu/")
try:
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='https://hipointedrivein.com/wp-content/uploads/2017/04/hpdi_post-500x500.jpg']").click()
    time.sleep(5)

    print("elements are present.")
except:
    print("element is not clickable") 
time.sleep(5)

driver.quit()