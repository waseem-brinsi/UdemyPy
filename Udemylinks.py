def onlinecourses_link(browser):
    i=0
    coursesfile = open("onlinecourses","r")
    for url in coursesfile:
        i+=1
        print(i,"-",url)
        browser.get(url)  
        link=browser.find_element_by_xpath("//div[@class='link-holder']").find_element_by_tag_name("a").get_attribute("href")
        udemyfile = open("Udemy","a")
        udemyfile.write(link+"\n")

    udemyfile.close()    
    coursesfile.close()    
    
def smartybro_link(browser):
    i=0
    with open("smartybro","r")  as coursesfile:
        for url in coursesfile:
            i+=1
            print(i,"-",url) 
            try:
                browser.get(url)
                findlink = browser.find_element_by_xpath("//a[@class='fasc-button fasc-size-xlarge fasc-type-flat']")
                link = findlink.get_attribute("href")
            except:
                pass
            with open("Udemy","a") as udemyfile :
                udemyfile.write(link+"\n")