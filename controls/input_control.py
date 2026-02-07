from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class InputControl(BaseControl):
    def __init__(self, page, wrapper):
        super().__init__(page, wrapper)

    def fill_value(self, value):
        return self.wrapper.fill(value)