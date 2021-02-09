from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# logging in with the following credentials.
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()


# getting the length of same className elements and generating random number within that length.
lis = driver.find_elements_by_xpath("//button[@class ='btn_primary btn_inventory']")
random_number = random.randint(2, len(lis))

# selecting random no.of "add to cart" button.
for i in range(0, random_number):
    driver.find_element_by_class_name("btn_primary").click()


# Moving to cart page and then to checkout page.
driver.find_element_by_xpath("//a[@href='./cart.html']").click()
driver.find_element_by_xpath("//a[@href='./checkout-step-one.html']").click()


# filling in the details of user.
driver.find_element_by_id("first-name").send_keys("standard")
driver.find_element_by_id("last-name").send_keys("user")
driver.find_element_by_id("postal-code").send_keys("123456")
driver.find_element_by_xpath("//input[@value='CONTINUE']").click()


# completing the process by checking out.
driver.find_element_by_xpath("//a[@href='./checkout-complete.html']").click()

# closing the browser.
driver.quit()
