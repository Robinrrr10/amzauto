README
------

1. Use python 2.7 or more
2. Should have selenium library. If not there use below command to install selenium lib
  EG:
   pip install selenium
3. Chrome browser should be installed

To run
------

Please run TestPages.py file to run the test


Class and its uses
----------------
Base.py  - Use this class to add webdriver and its path of driver. Here driver is in driver/chromedriver
locator  - Here we are maintaining all locators
Pages    - This is the helper class for each pages
validator - This has all expected value
TestPages  - This has test cases. Currently we have added only the given scenario



Changes done in scenario
------------------------
Below is the give steps

1. Go to Amazon.in
2. In the search dropdown list, choose the ‘Books’ option.
3. Enter search text ‘artificial intelligence’ and search.
4. Choose Arts, Film & Photography department
5. Choose Cinema & Broadcast as sub-department
6. Choose the Max of “Avg Customer Review” option
7. Sort the result by “Publication Date”
8. Make a filter of price with Maximum 1000 rupees and Minimum of 1500 Rupees
9. The Book should be available in all three formats like paperback, Kindle ebooks, and Hardcover. Apply those necessary filters
10. Choose the first test result (first product listed on the search result page) and read/record as many details related to that particular test result as possible.
11. Title of the book
12. Price of the book for different editions
13. Product details
14. Delivery of the product should be to the Pincode 600001


Changes are in step 3, step 8, step 14

In step 3, Instead of searching ‘artificial intelligence’ here we are searching 'film'. because 'artificial intelligence' is not giving the department in further steps
In step 8, price search max rupeer 1000 and min rupees 1500. This is incorrect search. min should be 1000 and max should be 1500. This also changed
In step 14, We are not handling delivery here because to delivery require sigin where we need to give credential which is confidencial


