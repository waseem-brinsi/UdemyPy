import time
from login import login_udemy
from cookies import load_cookie
from find_element import enroll_button,count_fileline
captch_page ="Access to this page has been denied."
udemy_page ="Online Courses - Anytime, Anywhere | Udemy"

def udemy(browser):
    browser.get("https://www.udemy.com/join/login-popup/?next=/home/my-courses/learning/")
    time.sleep(5)
    page_title = browser.title
    print(page_title) 
    try:
        if page_title == udemy_page:
            login_udemy(browser)
            print("login to Udemy is done")
        elif page_title == captch_page :
            yes = input("1-entre the captcha code(yes):")
            if yes =="yes":
                print("1-wait....")
                login_udemy(browser)
            else:
                print("1-entre the captcha to continous")
        else:
            print("1-worring page")
    except :
        pass
    time.sleep(5)
    page_title = browser.title
    print(page_title)
    while True:
        if (page_title == captch_page):
            yes = input("11-entre the captcha code(yes):")
            if yes =="yes":
                print("11-wait....")
            else:
                print("11-entre the captcha to continous")
        else:
            break
        break
        
    print("captcha ===> Done")
    numb=0
    udemyfile = open("Udemy","r")
    for line in udemyfile:
        numb+=1
        browser.get(line)
        time.sleep(10)
        try:
            page_title = browser.title
            print(numb," - ",page_title)
            if page_title == captch_page :
                yes = input("2-entre the captcha code(yes):")
                if yes =="yes":
                    print("2-wait....")
                    enroll_button(browser)
                    time.sleep(10)
                else:
                    print("entre the captcha again")
            else:
                enroll_button(browser)
                time.sleep(10)
        except :
            print("pass to the next course")
    ncourses=count_fileline("Udemy", "r")
    if ncourses==numb:
        with open("Udemy","w") as remove:
            pass
    else:
        pass
    udemyfile.close()