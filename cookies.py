import pickle

def save_cookie(browser):
    with open("cookies.pkl","wb") as cookiesfile:
        pickle.dump( browser.get_cookies() ,cookiesfile)
        
def load_cookie(browser):
    with open("cookies.pkl", "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            browser.add_cookie(cookie)