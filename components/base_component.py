from playwright.sync_api import Page, Locator


class BaseComponent:
    def __init__(self, page: Page, wrapper: Locator):
        self.page: Page = page
        self.wrapper: Locator = wrapper

    def waitForLoad(self):
        return self.wrapper.wait_for()

    def waitForLoadInDOM(self):
        return self.wrapper.wait_for(state="attached")