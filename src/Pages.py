from selenium.webdriver.common.keys import Keys
from Base import Page
from locator import *
from time import sleep


class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocator
        self.driver = driver
    
    def searchText(self, item):
        self.driver.find_element(*self.locator.SEARCH).send_keys(item)
        self.driver.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        
    def selectBook(self):
        self.driver.find_element(*self.locator.SEARCH_DROPDOWN_BOX_BOOKS).click()
    
    def selectBroadCast(self):
        self.driver.find_element(*self.locator.DEPARTMENTS_SEE_MORE).click()
        self.driver.find_element(*self.locator.DEPARTMENTS_ART_AND_OTHERS).click()
        self.driver.find_element(*self.locator.SUB_DEPARTMENTS_BROADCAST).click()
        
    def clickTopReviewed(self):
        self.driver.find_element(*self.locator.TOP_REVIEWS).click()
    
    def sortByPublishedDate(self):
        self.driver.find_element(*self.locator.SORT).click()
        self.driver.find_element(*self.locator.PUBLISHED_DATE).click()
        
    def givePriceRange(self, minPrice, maxPrice):
        self.driver.find_element(*self.locator.MIN_PRICE).send_keys(minPrice)
        self.driver.find_element(*self.locator.MAX_PRICE).send_keys(maxPrice)
        self.driver.find_element(*self.locator.PRICE_SEARCH).click()
        
    def selectCheckBox(self, *checkBox):
        checkBoxElement = self.driver.find_element(*checkBox)
        self.driver.execute_script("arguments[0].click();", checkBoxElement)
        
    def selectFirstProductFromSearch(self):
        self.driver.find_element(*self.locator.SEARCH_FIRST_PRODUCT).click()
        
    def switchToNextTab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(10)
        
class ProductPage(Page):
    def __init__(self, driver):
        self.locator = ProductPageLocator
        self.driver = driver
        
    def getProductTitle(self):
        productTitle = self.driver.find_element(*self.locator.PRODUCT_TITLE).text
        return productTitle
    
    def getProductPrice(self):
        productPrice = self.driver.find_element(*self.locator.PRODUCT_PRICE).text
        return productPrice
    
    def getProductDescription(self):
        productDesc = self.driver.find_element(*self.locator.PRODUCT_DESCRIPTION).text
        return productDesc
    
        