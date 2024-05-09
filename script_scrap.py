from selenium import webdriver
import time


#### data needed for log in process to twitter ####
username = 'Geekt973Geek'
email = 'geekt973@gmail.com'
password = 'ASMB2011asmb@'


### make instance of FireFox browser webdriver ###
driver = webdriver.Firefox()
## #### #### log in  process #### ##### ##
## request on log in page ##
driver.get('https://twitter.com/login')
## time delay ##
time.sleep(5)

## enter email ##
driver.find_element('tag name','input').send_keys(email)
time.sleep(5)
## next button sumbit ##
driver.find_element('xpath',"//span[text()='Next']").click()
time.sleep(5)
## enter username ##
driver.find_element('tag name','input').send_keys(username)
time.sleep(5)
## next button submit ##
driver.find_element('xpath',"//span[text()='Next']").click()
time.sleep(5)
## enter password ##
driver.find_element('xpath','//input[@type="password"]').send_keys(password)
time.sleep(5)
## Log in button submit ##
driver.find_element('xpath',"//span[text()='Log in']").click()
time.sleep(5)

## request on specific url ##
driver.get('https://twitter.com/Mr_Derivatives')
time.sleep(180) ### delay to load all data of url account ###

## get all spans from requests that contains symbols ##
spans = driver.find_elements('xpath','//span[@class="r-18u37iz"]')
# time.sleep(40)

## loop in pans to print its symbol text ##
for span in spans:
    ## check if text of span is starts with '$' or not ##
    if span.text[0]=='$':
        print(span.text)
    