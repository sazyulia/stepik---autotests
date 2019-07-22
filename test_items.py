import pytest
from selenium import webdriver

import time
#import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print('\nquit browser..')
    browser.quit()

def test_links(browser):
    browser.get(f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    result=browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket').text
    assert result == 'Добавить в корзину', "message is not 'Добавить в корзину'"