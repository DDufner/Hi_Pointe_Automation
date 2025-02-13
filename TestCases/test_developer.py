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


driver.get("https://hipointedrivein.appfront.app/find-location/?servingOptionType=delivery/")
try:
    print("test start")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='mui-3']").send_keys("1110 Stone Hill Hwy, Hermann, MO 65041")
    time.sleep(5)
    print("typed address on field")
    driver.find_element(By.XPATH, "//ul//li[@id='react-autowhatever-1--item-0']").click()
    time.sleep(5)
    found_element = driver.find_element(By.XPATH, "//div[@class='index-module--ErrorMessage--f938d']")
    assert True
    print("success!")
except:
    print("something failed") 
time.sleep(5)

driver.quit()