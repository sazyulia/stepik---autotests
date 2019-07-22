import pytest
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_item_button_exists(browser):
	browser.get(link)
	add_item_button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
	assert add_item_button != None, "Button is not exist"