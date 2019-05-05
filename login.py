import time
from cookies import load_cookie
email ="your_gmail_emai"
Ude_password ="Udemy_password"
g_password ="gmail_password"
def login_udemy(browser):
    try:
        load_cookie(browser)
    except:
        pass
    try:
        browser.find_element_by_name("email").send_keys(email)
        browser.find_element_by_name("password").send_keys(Ude_password)
        time.sleep(20)
        browser.find_element_by_xpath("//input[@id='submit-id-submit']").click()
        time.sleep(30)
    except:
        browser.find_element_by_name("password").send_keys(Ude_password)
        time.sleep(20)
        browser.find_element_by_xpath("//input[@id='submit-id-submit']").click()
        time.sleep(30)
def login_gmail(browser):
    browser.get("https://accounts.google.com")
    try:
    	load_cookie(browser)
    except:
    	pass
    browser.find_element_by_xpath("//input[@id='identifierId']").send_keys(email)
    browser.find_element_by_xpath("//div[@id='identifierNext']").click()
    #browser.implicitly_wait(20)
    time.sleep(5)
    browser.find_element_by_xpath("//input[@name='password']").send_keys(g_password)
    browser.find_element_by_xpath("//div[@id='passwordNext']").click()
    time.sleep(5)
