import time
from selenium import webdriver

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_btn_add_to_basket(browser):
    browser.get(link)
    fidb = browser.find_element_by_css_selector(".btn-add-to-basket")
    # print(type(fidb))
    time.sleep(5)

    assert isinstance(fidb, webdriver.remote.webelement.WebElement), 'Site does not contain an add to backet'
