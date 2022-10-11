from selenium.webdriver.common.by import By
from time import sleep


def test_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    sleep(30)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
