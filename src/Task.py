from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By


class Automate:
    def testSearch(self):
        localdriverPath = "../drivers/chromedriver";
        driver = webdriver.Chrome(localdriverPath)
        driver.get("https://www.google.com")
        sleep(4)
        title = driver.title
        print("Title is:", title)
        driver.find_element_by_name("q").send_keys("automation")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        sleep(4)
        title = driver.title
        print("Title after search is:", title)
        driver.quit()
        
    def amazon(self):
        localdriverPath = "../drivers/chromedriver";
        driver = webdriver.Chrome(localdriverPath)
        driver.get("https://www.amazon.in")
        driver.maximize_window()
        sleep(1)
        title = driver.title
        print("Title is:", title)
        #driver.find_element_by_name("q").send_keys("automation")
        #driver.find_element_by_name("q").send_keys(Keys.ENTER)
        #sleep(4)
        #title = driver.title
        #print("Title after search is:", title)
        
        driver.find_element_by_xpath("//select[@id='searchDropdownBox']/option[text()='Books']").click()
        driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("flim") #artificial intelligence 
        driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys(Keys.ENTER)
        
        driver.find_element_by_xpath("//*[@id='departments']/ul/li[5]/span/div/a/span").click()
        driver.find_element_by_xpath("//*[@id='departments']/ul/li[5]/span/div/div/ul/li[1]").click()
        driver.find_element_by_xpath("//*[@id='departments']/ul/li[4]").click()
        
        driver.find_element_by_xpath("//*[@id='reviewsRefinements']/ul/li[1]").click()
        
        driver.find_element_by_xpath("//*[@id='a-autoid-0-announce']/span[1]").click()
        driver.find_element_by_xpath("//*[@id='s-result-sort-select_4']").click()
        
        driver.find_element_by_xpath("//input[@id='low-price']").send_keys("1000")
        driver.find_element_by_xpath("//input[@id='high-price']").send_keys("1500")
        driver.find_element_by_xpath("//*[@id='a-autoid-1']/span/input").click()
        
        #driver.find_element_by_xpath("//*[@id='p_n_binding_browse-bin/1318376031']/span/a/div/label/i").click()
        #driver.find_element_by_xpath("//*[@id='p_n_binding_browse-bin/1634951031']/span/a/div/label/i").click()
        #driver.find_element_by_xpath("//*[@id='p_n_binding_browse-bin/1318375031']/span/a/div/label/i").click()
        
        #driver.find_element_by_xpath("//*[@id='filters']/ul[3]/li[1]/span/a/div/label/input").click()
        #driver.find_element_by_xpath("//*[@id='filters']/ul[3]/li[2]/span/a/div/label/input").click()
        #driver.find_element_by_xpath("//*[@id='filters']/ul[3]/li[3]/span/a/div/label/input").click()
        
        el1 = driver.find_element_by_xpath(".//*[contains(text(), 'Paperback')]")
        driver.execute_script("arguments[0].click();", el1)
        el2 = driver.find_element_by_xpath(".//*[contains(text(), 'Kindle eBooks')]")
        driver.execute_script("arguments[0].click();", el2)
        el3 = driver.find_element_by_xpath(".//*[contains(text(), 'Hardcover')]")
        driver.execute_script("arguments[0].click();", el3)
        #driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
        driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span").click()
        #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span
        sleep(8)
        driver.switch_to.window(driver.window_handles[1])
        title = driver.title
        print("Title2 is:", title)
        
        driver.find_element(By.XPATH, "").click()
        
        productTileEle = driver.find_element_by_xpath("//*[@id='productTitle']")
        productTile = productTileEle.text
        print("Product Title:"+productTile)
        price = driver.find_element_by_xpath("//*[@id='a-autoid-2-announce']/span[2]/span").text
        print("Price is:"+price)
        #//*[@id="detail_bullets_id"]/table/tbody/tr/td/div
        description = driver.find_element_by_xpath("//*[@class='content']").text
        print("Product description:"+description)
        
        driver.quit()
g1 = Automate()
#g1.testSearch()
g1.amazon()