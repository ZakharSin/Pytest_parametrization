import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_browserlanguage(browser):
    browser.get(link)
    time.sleep(30)
    a = browser.find_elements(By.XPATH, "//form[@id='add_to_basket_form']/button")
    assert len(a) > 0, 'no item'
    time.sleep(10)
    browser.quit()