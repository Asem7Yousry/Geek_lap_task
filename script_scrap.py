from selenium import webdriver
import time
from tkinter import messagebox # to show messages

#### data needed for log in process to twitter ####
username = 'Geekt973Geek'
email = 'geekt973@gmail.com'
password = 'ASMB2011asmb@'

#### scraping accounts urls #####
urls_required = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox'
]


### function for scrap tool ###
def scrap_method(interval_time , symbol , urls_required = urls_required):
    ## make the symbol letters in upper case ##
    symbol = symbol.upper()
    print(symbol)
    ## initialize number of symbol mentioned in the account ##
    number_mintioned = 0

    try:
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

        ### loop on the 10 urls ###
        for url in urls_required:
            ## request on specific url ##
            driver.get(url)
            ## interval time ##
            time.sleep(interval_time) ### delay to load all data of url account ###

            ### get all tweets(all articles) by article tag name in url ###
            tweets = driver.find_elements('xpath','//article[@data-testid="tweet"]')

            ### loop in tweets to get all spans ###
            for tweet in tweets:
                ## get all spans from requests that contains symbols in each tweet itself##
                spans = tweet.find_elements('xpath','.//span[@class="r-18u37iz"]')
                # time.sleep(40)

                ## loop in pans to print its symbol text ##
                for span in spans:
                    ## check if text of span is starts with '$' or not ##
                    if span.text.startswith('$'):
                        ## seperate the symbol from '$' and upper its letters ##
                        span_text = span.text[1:].upper()
                        ## check if span text is equal to symbol ##
                        if span_text==symbol:
                            number_mintioned +=1
        message = f"{symbol} mentioned {number_mintioned} in last {interval_time} seconds"
        print(number_mintioned)
        messagebox.showinfo("Done!", message)
    except:
        messagebox.ERROR("watch out!","error log in")