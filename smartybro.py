import time
from find_element import find_h2_tage, next_page
def smartybro(browser):
    browser.get("https://smartybro.com")
    with open("smartybro","r",encoding='utf-8') as coursesfile:
        lastcours=coursesfile.readline()
        print("the last couse is :=======>>"+lastcours)
    
    with open("smartybro","w",encoding='utf-8') as coursesfile:
        page=0
        while True:
            page+=1
            titles=find_h2_tage(browser)
            for ti in titles:
                try:
                    href = ti.find_element_by_tag_name("a").get_attribute("href")
                except:
                    pass
                currentcours,currentcours1=href,href+"\n"
                if (lastcours==currentcours)or(lastcours==currentcours1):
                    print(ti.text+"====> is enrolled course")
                    coursesfile.write(lastcours)
                    time.sleep(5)
                    break
                elif (lastcours!=currentcours)or(lastcours!=currentcours1):
                    try:
                        print(ti.text+"====> is now course")
                        coursesfile.write(href+'\n')
                    except:
                        pass
                else:
                    print("some thing is worring")
                    pass
            if (lastcours==currentcours)or(lastcours==currentcours1):
                break
            else:
                next_page(browser).click()
                time.sleep(5)
                print("Page",page)
        print("we finshed")