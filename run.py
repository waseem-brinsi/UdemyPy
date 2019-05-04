import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options                     #import the option of the chrome browser
from cookies import save_cookie
from login import login_gmail
from onlinecourses import online_couses
from smartybro import smartybro
from Udemylinks import onlinecourses_link, smartybro_link
from Udemy_Enroll import udemy
chrome_options = Options()
chrome_options.add_extension("ChroPath.crx")  
chrome_options.add_argument('--no-sandbox')                            #added chropath extension to the chrome browser
chrome_options.add_experimental_option('excludeSwitches',['disable-sync'])#enable login to the chrome browser
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"./chromedriver")

login_gmail(browser)
time.sleep(10)
smartybro(browser)
smartybro_link(browser)
online_couses(browser)
onlinecourses_link(browser)
udemy(browser)

print("save_cookie")
save_cookie(browser)
print("we finshed thank you wassim")
time.sleep(10)
browser.close()