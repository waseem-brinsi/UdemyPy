#https://smartybro.com/
def find_h2_tage(browser):
    content = browser.find_element_by_xpath("//div[@class='col-md-9 cont-grid']")  # bring the title of the coursees
    titles = content.find_elements_by_tag_name("h2")                 # useing tage name <h2>
    return titles

def next_page(browser):
    pagination= browser.find_element_by_xpath("//div[@class='pagination']")
    next_page= pagination.find_element_by_xpath("//a[@class='next page-numbers']")
    return next_page

#===============================================================================
# 
#===============================================================================
def find_h3_tage(browser):
    content = browser.find_element_by_xpath("//div[@id='content']")  # bring the title of the coursees
    titles = content.find_elements_by_tag_name("h3")                 # useing tage name <h3>
    return titles
def enroll_button(browser):
    buy_box = browser.find_element_by_xpath("//div[@class='buy-box']")
    buy_box1 = buy_box.find_element_by_xpath("//div[@class='buy-box__element buy-box__element--row']")
    enroll_button= buy_box1.find_element_by_xpath("//button[contains(text(),'Enroll now')]")
    return enroll_button.click()
def count_fileline(file,mode):
    with open(file,mode) as udemy:
        numl=0
        for line in udemy:
            numl+=1
    return numl
