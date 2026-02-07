import os
import time
import allure
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

@allure.title("Позитивное тестирование авторизации")
def test_login_with_valid_data(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.get_login_component().input_username(os.getenv('VALID_USERNAME'))
    login_page.get_login_component().input_password(os.getenv('VALID_PASSWORD'))
    login_page.get_login_component().click_login_button()
    time.sleep(1)

    expect(page).to_have_url(os.getenv('SUCCESS_AUTH_PAGE'))
    expect(page.locator('div[class="flash success"]')).to_contain_text("You logged into a secure area!")


@allure.title("Негавтивное тестирование авторизации")
def test_login_with_non_valid_data(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.get_login_component().input_username(os.getenv('NON_VALID_USERNAME'))
    login_page.get_login_component().input_password(os.getenv('VALID_PASSWORD'))
    login_page.get_login_component().click_login_button()
    time.sleep(1)

    expect(page).to_have_url(os.getenv('SUCCESS_AUTH_PAGE'))
    expect(page.locator('div[class="flash success"]')).to_contain_text("You logged into a secure area!")