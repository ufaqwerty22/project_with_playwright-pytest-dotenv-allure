import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class LoginComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator("//*[@id='login']"))
        self.username_input = InputControl(page, self.wrapper.locator("#username"))
        self.password_input = InputControl(page, self.wrapper.locator("#password"))
        self.login_button = ButtonControl(page, self.wrapper.locator("button[type='submit']"))

    def input_username(self, username):
        with allure.step("Ввод логина"):
            return self.username_input.fill_value(username)

    def input_password(self, password):
        with allure.step("Ввод пароля"):
            return self.password_input.fill_value(password)

    def click_login_button(self):
        with allure.step("Нажатие на кнопку логина"):
            return self.login_button.click()