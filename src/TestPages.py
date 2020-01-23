import unittest
from Base import Page
from Pages import MainPage, ProductPage
from locator import *
class Tests(unittest.TestCase):
    
    def testScenario(self):
        base = Page()
        driver = base.openPage()
        
        mainPage = MainPage(driver)
        mainPage.selectBook()
        mainPage.searchText("film")
        mainPage.selectBroadCast()
        mainPage.clickTopReviewed()
        mainPage.sortByPublishedDate()
        mainPage.givePriceRange("1000", "1500")
        mainPage.selectCheckBox(*MainPageLocator.PAPERBACK)
        mainPage.selectCheckBox(*MainPageLocator.KINDLE_EBOOKS)
        mainPage.selectCheckBox(*MainPageLocator.HARD_COVER)
        mainPage.selectFirstProductFromSearch()
        mainPage.switchToNextTab()
        
        productPage = ProductPage(driver)
        productTitle = productPage.getProductTitle()
        print("Product Title: "+productTitle)
        productPrice = productPage.getProductPrice()
        print("Product Price: "+productPrice)
        productDesc = productPage.getProductDescription()
        print("Product Description: "+productDesc)
        
        base.quitBrowsers(driver)

test = Tests()
test.testScenario()   
    