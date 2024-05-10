# Geel_lap_task
scraping tool to get number of mentioned symbol in interval time through a group of twitter accounts using selenium library with fire fox webdriver. 

# the commits for whole task :-

## commit 1_ initialize environment for task 
- install selenium library 
- download webdriver for FireFox browser (geckodriver.exe) 
- put geckodriver in the same path of scraping script 

## commit 2_ test scrapping symbols that starts with '$' in one url in interval time 180 sec  
- install selenium library 
- download webdriver for FireFox browser (geckodriver.exe) 
- put geckodriver in the same path of scraping script 

## comit 3_ try to get number of specific symbol mention in one page in speceific interval time 
- put symbol 
- concatenation it with '$' in the begining of symbol after making all letters in upper 
- looping in all spans with '$' in begining to  count the number of mentioning it 

## comit 4_ try to get number of specific symbol mentions in all 10 pages in speceific interval time 
- put all urls il list 
- loop in list urls 
- request on each url 
- get all symbols in speceific interval time 
- loop on symbols to get specific symbol  

## comit 5_ make symbols catched and symbol in search be in upper case to compare between then .
- make symbol letters in search in upper case 
- seperate each span text from its '$' in its begining 
- make span text letters in upper case  
- compare between symbol and span text in upper case 

## comit 5_ make scraping tool only search for symbol in only tweets.
make scraping tool only search on tweets not in BIO or outer the tweets are , that happenes by :-
- after request on individual url we get all the tweets .
- each tweet is in tag name called article .  
- we fined elements that in tag name article.  
- then we search in each article for spans .

