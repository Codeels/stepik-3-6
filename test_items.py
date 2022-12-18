from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    flag = False
    browser.get(link)
    basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    if basket_button:
        flag = True
    else:
        flag = False
    assert flag, "basket button not present"
