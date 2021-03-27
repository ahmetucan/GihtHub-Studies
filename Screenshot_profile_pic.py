from selenium import webdriver      
import time


driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)


time.sleep(2)

driver.maximize_window()
print(driver.title)
driver.save_screenshot("github.com-homepage.jpg")


url = "https://github.com/user"
driver.get(url)
print(driver.title)
if "ahmetucan" in driver.title:
    driver.save_screenshot("github-user.png")

time.sleep(2)

driver.back()
# driver.forward()

time.sleep(2)

driver.close()