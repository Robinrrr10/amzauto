from selenium import webdriver

class Page(object):
        
    def openPage(self):
        localdriverPath = "../drivers/chromedriver";
        self.driver = webdriver.Chrome(localdriverPath)
        self.driver.get("http://amazon.in")
        self.driver.maximize_window()
        return self.driver
    
    def quitBrowsers(self, driver):
        self.driver.quit()