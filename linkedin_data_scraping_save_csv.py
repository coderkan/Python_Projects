from selenium import webdriver
import pandas as pd 
import time

mail = input( "mail : " )
pwd = input( "password : " )

# start webdriver
browser = webdriver.Chrome()

# get source code
linkedin_url = "https://www.linkedin.com/"
browser.get( linkedin_url ) 
time.sleep( 5 )

# click login button 
log_in = browser.find_element_by_class_name( 'nav__button-secondary' )
log_in.click()
time.sleep( 5 )

# enter your password end mail
usr = browser.find_element_by_xpath( "//*[@id='username']" )
pss = browser.find_element_by_xpath( "//*[@id='password']" )

# enter username and psw and click 
usr.send_keys( mail )
time.sleep( 5 )
pss.send_keys( pwd )
time.sleep( 5 )

# click sign in
log = browser.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button")
log.click()
time.sleep( 5 )

# click my network tab
my_net = browser.find_element_by_xpath('//*[@id="ember23"]')
my_net.click()
time.sleep( 5 )

# the selection do for this keyword 
key_word = ['Human','Software','HR','Leader','Manager','Founder','Recruitment',
            'Machine Learning','Data','Vision','Kocaeli' ]

sz = len( key_word )
count = 0
d = dict()
data = dict()
lst_name = list()
lst_role = list()

for i in range ( 0, 10 ):
    content = browser.find_element_by_class_name('discover-person-card__occupation')
    time.sleep( 3 ) 
    content_sp = content.text.split()
    var = False
    
    for k in range ( 0, sz ):    
        if  key_word[k] in content_sp: 
            var = True
            
    if var == True:
        name = browser.find_element_by_class_name('discover-person-card__name')
        
        lst_name.append( name.text )
        lst_role.append( content.text )
        
        print( "* " + name.text + " - " + content.text)

        d = { 'names' : lst_name, 'roles' : lst_role }
        data.update( d ) 
        df = pd.DataFrame( data )        

        time.sleep( 3 )
  
        button = browser.find_element_by_class_name('full-width')
        button.click()
        time.sleep( 3 )
        
        exit_b = browser.find_element_by_class_name('artdeco-card__dismiss')
        exit_b.click()
        time.sleep( 3 )
        count = count + 1
                
    else:
        exit_b = browser.find_element_by_class_name('artdeco-card__dismiss')
        exit_b.click()
        time.sleep( 3 )

print( f"\ntotal new connection = {count}" )
print( data )

# # Saving the data into a csv file
df.to_csv("data.csv",index=False) 

#close browser
browser.close()

