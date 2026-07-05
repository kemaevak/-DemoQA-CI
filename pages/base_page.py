from playwright.sync_api import Page


class BasePage:
    """Базовый класс страницы. Хранит общую логику для всех Page Object."""

    url = ""

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")
        return self
