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


driver.get("https://hipointedrivein.appfront.app/?openSignup=true")
try:
    time.sleep(2)
    # driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
    # driver.refresh()
    # time.sleep(2)
    # driver.find_element(By.XPATH, "//button[@id='close-btn']").click()
    # driver.refresh()
    # time.sleep(2)
    driver.find_element(By.XPATH, "//input[@class='MuiSelect-nativeInput mui-1k3x8v3']").click()
    
    driver.find_element(By.XPATH, "//a[@class='index-module--Button--6cadf noselect index-module--Centered--18426']").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Terms of Service')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Policy')]").click()
    driver.find_element(By.XPATH, "//small[contains(text(),'Skip')]").click()   
    time.sleep(10)
    assert True
    print("All elements found")
except:
    print("element is not clickable") 
time.sleep(5)

driver.quit()