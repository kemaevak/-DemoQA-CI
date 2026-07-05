import allure
import pytest
from playwright.sync_api import expect

from pages.alerts_windows import (
    AlertsPage,
    BrowserWindowsPage,
    FramesPage,
    ModalDialogsPage,
)

pytestmark = pytest.mark.alerts_windows


@allure.feature("Alerts, Frame & Windows")
@allure.story("Browser Windows")
class TestBrowserWindows:

    @allure.title("Кнопка New Tab открывает новую вкладку")
    def test_new_tab(self, page):
        windows = BrowserWindowsPage(page).open()
        with page.expect_popup() as popup_info:
            windows.new_tab_button.click()
        new_tab = popup_info.value
        expect(new_tab.locator("#sampleHeading")).to_have_text(
            "This is a sample page"
        )


@allure.feature("Alerts, Frame & Windows")
@allure.story("Alerts")
class TestAlerts:

    @allure.title("Простой alert открывается и закрывается")
    def test_simple_alert(self, page):
        alerts = AlertsPage(page).open()
        messages = []
        page.once("dialog", lambda d: (messages.append(d.message), d.accept()))
        alerts.alert_button.click()
        assert messages == ["You clicked a button"]

    @allure.title("Подтверждение confirm-диалога")
    def test_confirm_accept(self, page):
        alerts = AlertsPage(page).open()
        page.once("dialog", lambda d: d.accept())
        alerts.confirm_button.click()
        expect(alerts.confirm_result).to_have_text("You selected Ok")

    @allure.title("Отмена confirm-диалога")
    def test_confirm_dismiss(self, page):
        alerts = AlertsPage(page).open()
        page.once("dialog", lambda d: d.dismiss())
        alerts.confirm_button.click()
        expect(alerts.confirm_result).to_have_text("You selected Cancel")

    @allure.title("Ввод текста в prompt-диалог")
    def test_prompt_with_text(self, page):
        alerts = AlertsPage(page).open()
        page.once("dialog", lambda d: d.accept("Дмитрий"))
        alerts.prompt_button.click()
        expect(alerts.prompt_result).to_contain_text("Дмитрий")


@allure.feature("Alerts, Frame & Windows")
@allure.story("Frames")
class TestFrames:

    @allure.title("Чтение содержимого iframe")
    def test_frame_content(self, page):
        frames = FramesPage(page).open()
        expect(frames.frame1.locator("#sampleHeading")).to_have_text(
            "This is a sample page"
        )
        expect(frames.frame2.locator("#sampleHeading")).to_have_text(
            "This is a sample page"
        )


@allure.feature("Alerts, Frame & Windows")
@allure.story("Modal Dialogs")
class TestModalDialogs:

    @allure.title("Открытие и закрытие маленького модального окна")
    def test_small_modal(self, page):
        modals = ModalDialogsPage(page).open()
        modals.small_modal_button.click()
        expect(modals.modal_title).to_have_text("Small Modal")
        modals.close_small_button.click()
        expect(modals.modal).to_be_hidden()

    @allure.title("Открытие и закрытие большого модального окна")
    def test_large_modal(self, page):
        modals = ModalDialogsPage(page).open()
        modals.large_modal_button.click()
        expect(modals.modal_title).to_have_text("Large Modal")
        modals.close_large_button.click()
        expect(modals.modal).to_be_hidden()
