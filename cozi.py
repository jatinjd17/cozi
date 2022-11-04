from selenium import webdriver
from time import sleep

import names
from random import randrange




from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument(r"--user-data-dir=C:\Users\jatin\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument('profile-directory=Default')
options.add_argument('--window-size=1920,1080')
# options.add_argument("--headless")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# options.add_argument("--start-fullscreen")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# The place we will direct our WebDriver to


# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome(chrome_options=options)


gname = '@gmail.com'
fullname = names.get_full_name()
firstname = fullname.split(" ",1)
email = fullname.replace(" ","")+str(randrange(4000))+gname
print(email)

# Directing the driver to the defined url
# driver.get('https://www.sps-software.net/')
driver.get('https://my.cozi.com/signup/')

sleep(10)



######################################################STSRT##########################################
driver.find_element_by_xpath("//*[@id='first_name']").send_keys(firstname[0])
#####################################################
sleep(1)

driver.find_element_by_xpath("//*[@id='email']").send_keys(email)
#####################################################
sleep(1)

driver.find_element_by_xpath("//*[@id='password']").send_keys("Jatin@123")
#####################################################
sleep(1)

driver.find_element_by_xpath("//*[@id='household_name']").send_keys(firstname[0])
#####################################################
sleep(1)

driver.find_element_by_xpath("//*[@id='app']/main/div[2]/div/div[1]/div/div[1]/div/button") \
    .click()

#
# sleep(20)
#
# element = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div")
#
# textin = element.get_attribute('innerText')
#
# print(textin)

print('Done!!!!!!!!')

sleep(15)

# elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/h1")
#
# source_code = elem.get_attribute("outerHTML")
# print(source_code)
# sleep(3)
###########################################################END##########################################################################


driver.quit()
