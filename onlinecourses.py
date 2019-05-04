import time
from find_element import find_h3_tage
def online_couses(browser):
    browser.get("https://onlinecourses.ooo/")
    with open("onlinecourses","r",encoding='utf-8') as coursesfile:
        lastcours=coursesfile.readline()
        print("the last couse is :=======>>"+lastcours)
    page=0
    with open("onlinecourses","w",encoding='utf-8') as coursesfile:
        while True:
            page+=1
            titles=find_h3_tage(browser)
            for ti in titles:
                href = ti.find_element_by_tag_name("a").get_attribute("href")
                currentcours,currentcours1=href,href+"\n"
                if (lastcours==currentcours)or(lastcours==currentcours1):
                    print(ti.text+"====> is enrolled course")
                    coursesfile.write(lastcours)
                    time.sleep(5)
                    break
                elif (lastcours!=currentcours)or(lastcours!=currentcours1):
                    print(ti.text+"====> is now course")
                    coursesfile.write(href+'\n')
                else:
                    print("some thing is worring")
                    pass
            if (lastcours==currentcours)or(lastcours==currentcours1):
                break
            else:
                while True:
                    next_page = browser.find_element_by_xpath("//a[@class='next page-numbers']")
                    try:
                        browser.execute_script("arguments[0].scrollIntoView();",next_page)
                        next_page.click()
                        print("Page",page)
                    except:
                        browser.find_element_by_xpath("//button[@title='Close (Esc)']").click()
                        browser.execute_script("arguments[0].scrollIntoView();",next_page)
                        next_page.click()
                        print("Page",page)
                    break
        print("we finshed")