from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    """Страница Alerts, Frame & Windows -> Browser Windows."""

    url = "/browser-windows"

    def __init__(self, page):
        super().__init__(page)
        self.new_tab_button = page.locator("#tabButton")
        self.new_window_button = page.locator("#windowButton")


class AlertsPage(BasePage):
    """Страница Alerts, Frame & Windows -> Alerts."""

    url = "/alerts"

    def __init__(self, page):
        super().__init__(page)
        self.alert_button = page.locator("#alertButton")
        self.confirm_button = page.locator("#confirmButton")
        self.confirm_result = page.locator("#confirmResult")
        # в id кнопки на сайте опечатка — promtButton (см. BUG-004)
        self.prompt_button = page.locator("#promtButton")
        self.prompt_result = page.locator("#promptResult")


class FramesPage(BasePage):
    """Страница Alerts, Frame & Windows -> Frames."""

    url = "/frames"

    def __init__(self, page):
        super().__init__(page)
        self.frame1 = page.frame_locator("#frame1")
        self.frame2 = page.frame_locator("#frame2")


class ModalDialogsPage(BasePage):
    """Страница Alerts, Frame & Windows -> Modal Dialogs."""

    url = "/modal-dialogs"

    def __init__(self, page):
        super().__init__(page)
        self.small_modal_button = page.locator("#showSmallModal")
        self.large_modal_button = page.locator("#showLargeModal")
        self.modal = page.locator(".modal-content")
        self.modal_title = page.locator(".modal-title")
        self.modal_body = page.locator(".modal-body")
        self.close_small_button = page.locator("#closeSmallModal")
        self.close_large_button = page.locator("#closeLargeModal")
