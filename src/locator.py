from selenium.webdriver.common.by import By

class MainPageLocator(object):
    SEARCH_DROPDOWN_BOX_BOOKS = (By.XPATH, "//select[@id='searchDropdownBox']/option[text()='Books']")
    SEARCH = (By.ID, "twotabsearchtextbox")
    DEPARTMENTS_SEE_MORE = (By.XPATH, "//*[@id='departments']/ul/li[5]/span/div/a/span")
    DEPARTMENTS_ART_AND_OTHERS = (By.XPATH, "//*[@id='departments']/ul/li[5]/span/div/div/ul/li[1]")
    SUB_DEPARTMENTS_BROADCAST = (By.XPATH, "//*[@id='departments']/ul/li[4]")
    TOP_REVIEWS = (By.XPATH, "//*[@id='reviewsRefinements']/ul/li[1]")
    SORT = (By.XPATH, "//*[@id='a-autoid-0-announce']/span[1]")
    PUBLISHED_DATE = (By.ID, "s-result-sort-select_4")
    MIN_PRICE = (By.ID, "low-price")
    MAX_PRICE = (By.ID, "high-price")
    PRICE_SEARCH = (By.XPATH, "//*[@id='a-autoid-1']/span/input")
    PAPERBACK = (By.XPATH, ".//*[contains(text(), 'Paperback')]")
    KINDLE_EBOOKS = (By.XPATH, ".//*[contains(text(), 'Kindle eBooks')]")
    HARD_COVER = (By.XPATH, ".//*[contains(text(), 'Hardcover')]")
    SEARCH_FIRST_PRODUCT = (By.XPATH, "//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")

class ProductPageLocator(object):
    PRODUCT_TITLE = (By.ID, "productTitle")    
    PRODUCT_PRICE = (By.XPATH, "//*[@id='a-autoid-2-announce']/span[2]/span")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "content")