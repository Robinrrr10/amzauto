from selenium.webdriver.common.keys import Keys
from Base import Page
from locator import *
from time import sleep

"This class is Main page helper"
class MainPage(Page):
    
    "Here we declare driver and locator"
    def __init__(self, driver):
        self.locator = MainPageLocator
        self.driver = driver
    
    "This method will search given product"
    def searchText(self, item):
        self.driver.find_element(*self.locator.SEARCH).send_keys(item)
        self.driver.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
        
    "This method will select book in search drop down box"
    def selectBook(self):
        self.driver.find_element(*self.locator.SEARCH_DROPDOWN_BOX_BOOKS).click()
    
    "This method will select cinema and broadcast in department"
    def selectCinemaAndBroadCast(self):
        self.driver.find_element(*self.locator.DEPARTMENTS_SEE_MORE).click()
        self.driver.find_element(*self.locator.DEPARTMENTS_ART_AND_OTHERS).click()
        self.driver.find_element(*self.locator.SUB_DEPARTMENTS_BROADCAST).click()
        
    "This will click top reviewed product in top"
    def clickTopReviewed(self):
        self.driver.find_element(*self.locator.TOP_REVIEWS).click()
    
    "This will sort in publishing date"
    def sortByPublishedDate(self):
        self.driver.find_element(*self.locator.SORT).click()
        self.driver.find_element(*self.locator.PUBLISHED_DATE).click()
        
    "Search based on price range"
    def givePriceRange(self, minPrice, maxPrice):
        self.driver.find_element(*self.locator.MIN_PRICE).send_keys(minPrice)
        self.driver.find_element(*self.locator.MAX_PRICE).send_keys(maxPrice)
        self.driver.find_element(*self.locator.PRICE_SEARCH).click()
        
    "To select checkbox use this method"
    def selectCheckBox(self, *checkBox):
        checkBoxElement = self.driver.find_element(*checkBox)
        self.driver.execute_script("arguments[0].click();", checkBoxElement)
        
    "This method is used to select first product in search list"
    def selectFirstProductFromSearch(self):
        self.driver.find_element(*self.locator.SEARCH_FIRST_PRODUCT).click()
        
    "This is used to switch to next tab"
    def switchToNextTab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(10) #Have to wait until the page load
        
class ProductPage(Page):
    
    "to declare driver and locator"
    def __init__(self, driver):
        self.locator = ProductPageLocator
        self.driver = driver
        
    "This will give product title"
    def getProductTitle(self):
        productTitle = self.driver.find_element(*self.locator.PRODUCT_TITLE).text
        return productTitle
    
    "This will give product price"
    def getProductPrice(self):
        productPrice = self.driver.find_element(*self.locator.PRODUCT_PRICE).text
        return productPrice
    
    "This will give product description"
    def getProductDescription(self):
        productDesc = self.driver.find_element(*self.locator.PRODUCT_DESCRIPTION).text
        return productDesc
    