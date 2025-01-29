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


driver.get("https://hipointedrivein.appfront.app/")
try:

    time.sleep(2)
    driver.find_element(By.XPATH, "//a/span[contains(text(),'Reorder')]").click()
    driver.find_element(By.XPATH, "//div/p[contains(text(),'Login to see your previous orders')]")
    time.sleep(5)
    #driver.find_element(By.XPATH, "//div[@class='index-module--ListCardContent--b2979']//span[contains(text(),'Cottleville')]").click()
    time.sleep(5)
    assert True
    print("All elements found")
except:
    print("element is not clickable") 
time.sleep(5)

driver.quit()