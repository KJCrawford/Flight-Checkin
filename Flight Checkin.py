############################################################################### 
## Fill out below four inputs to enter into website and receive confirmation ##
###############################################################################
# confirmation_number = raw_input("What is your confirmation number?")
confirmation_number = '' 
first_name = ''
last_name = ''
email_address = ''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def find_flight(d):
    ##
    # Enter personal information
    ##  
    d.find_element_by_id("confirmationNumber").send_keys(confirmation_number)
    d.find_element_by_id("firstName").send_keys(first_name)
    d.find_element_by_id("lastName").send_keys(last_name)
    d.find_element_by_id("itineraryLookup").submit()

def confirm_checkin(d):
    ##
    # Pass through check-in confirmation
    ##
    d.find_element_by_id('printDocumentsButton').click()

def send_confirmation_email(d):
    ##
    # Send confirmation email to yourself
    ## 
    d.find_element_by_css('radio_button_align swa_check-in_option_email').click()
    d.find_element_by_id('emailAddress').clear()
    d.find_element_by_id('emailAddress').send_keys(email_address)
    d.find_element_by_id('checkin_button').click()


if __name__ == '__main__':
    ##
    # Open Browser
    ##
    # d = webdriver.PhantomJS(r"C:\..\phantomjs-2.0.0\bin\phantomjs.exe")
    d = webdriver.Chrome()
    d.get("https://www.southwest.com/flight/retrieveCheckinDoc.html")
    sleep(3)

    find_flight(d)
    sleep(3)
    
    confirm_checkin(d)
    sleep(3)
    
    send_confirmation_email(d)
    
    d.quit()
