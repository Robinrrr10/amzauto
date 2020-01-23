import unittest
from Base import Page
from Pages import MainPage, ProductPage
from locator import *
from validator import ProductValidators

"This class will contain test"
class Tests(unittest.TestCase):
    
    "Test give scenario"
    def testScenario(self):
        
        #Intialize webdriver and open browser
        base = Page()
        driver = base.openPage()
        
        #Main page operation is below
        mainPage = MainPage(driver)
        mainPage.selectBook()
        mainPage.searchText("film")
        mainPage.selectCinemaAndBroadCast()
        mainPage.clickTopReviewed()
        mainPage.sortByPublishedDate()
        mainPage.givePriceRange("1000", "1500")
        mainPage.selectCheckBox(*MainPageLocator.PAPERBACK)
        mainPage.selectCheckBox(*MainPageLocator.KINDLE_EBOOKS)
        mainPage.selectCheckBox(*MainPageLocator.HARD_COVER)
        mainPage.selectFirstProductFromSearch()
        mainPage.switchToNextTab()
        
        #Product page operation is below
        productPage = ProductPage(driver)
        productTitle = productPage.getProductTitle()
        print("Product Title: "+productTitle)
        self.assertEqual(productTitle, ProductValidators.PRODUCT_TITLE, "Product title is not as expected")
        productPrice = productPage.getProductPrice()
        print("Product Price: "+productPrice)
        self.assertEqual(productPrice, ProductValidators.PRODUCT_PRICE, "Product Price is not as expected")
        productDesc = productPage.getProductDescription()
        print("Product Description: "+productDesc)
        
        #close and stop the browser
        base.quitBrowsers(driver)


test = Tests()

#calling the method to run the test
test.testScenario()   
    