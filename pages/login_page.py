import os

from pages.base_page import BasePage
from components.login_component import LoginComponent

class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        super().__init__(self.page, os.getenv('LOGIN_PAGE'))

    def get_login_component(self):
        return LoginComponent(self.page)