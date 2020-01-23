from selenium import webdriver

class Page(object):

    "This method will intialize webdriver and open website in browser"       
    def openPage(self):
        localdriverPath = "../drivers/chromedriver";
        self.driver = webdriver.Chrome(localdriverPath)
        self.driver.get("http://amazon.in")
        self.driver.maximize_window()
        return self.driver
    
    "This method is used to close/quit the driver"
    def quitBrowsers(self, driver):
        self.driver.quit()