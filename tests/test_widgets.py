import allure
import pytest
from playwright.sync_api import expect

from pages.widgets import (
    AccordionPage,
    DatePickerPage,
    ProgressBarPage,
    SelectMenuPage,
    SliderPage,
    ToolTipsPage,
)

pytestmark = pytest.mark.widgets


@allure.feature("Widgets")
@allure.story("Accordion")
class TestAccordion:

    @allure.title("Первая секция раскрыта по умолчанию")
    def test_first_section_open_by_default(self, page):
        accordion = AccordionPage(page).open()
        expect(accordion.buttons.first).to_have_text("What is Lorem Ipsum?")
        expect(accordion.section_content(0)).to_be_visible()
        expect(accordion.section_content(1)).to_be_hidden()

    @allure.title("Клик по заголовку раскрывает секцию")
    def test_open_second_section(self, page):
        accordion = AccordionPage(page).open()
        accordion.buttons.nth(1).click()
        expect(accordion.section_content(1)).to_be_visible()
        expect(accordion.section_content(0)).to_be_hidden()


@allure.feature("Widgets")
@allure.story("Select Menu")
class TestSelectMenu:

    @allure.title("Выбор значения в классическом select")
    def test_old_style_select(self, page):
        menu = SelectMenuPage(page).open()
        menu.old_select.select_option(label="Green")
        expect(menu.old_select).to_have_value("2")


@allure.feature("Widgets")
@allure.story("Progress Bar")
class TestProgressBar:

    @allure.title("Прогресс-бар останавливается по кнопке Stop")
    def test_start_and_stop(self, page):
        progress = ProgressBarPage(page).open()
        assert progress.value() == 0
        progress.start_stop_button.click()
        page.wait_for_timeout(1_500)
        progress.start_stop_button.click()
        assert 0 < progress.value() < 100


@allure.feature("Widgets")
@allure.story("Slider")
class TestSlider:

    @allure.title("Перемещение ползунка стрелками клавиатуры")
    def test_move_slider_with_keyboard(self, page):
        slider = SliderPage(page).open()
        expect(slider.value_input).to_have_value("25")
        slider.slider.click()
        for _ in range(5):
            slider.slider.press("ArrowRight")
        value = int(slider.value_input.input_value())
        assert value > 25


@allure.feature("Widgets")
@allure.story("Date Picker")
class TestDatePicker:

    @allure.title("Выбор даты через календарь")
    def test_pick_date(self, page):
        picker = DatePickerPage(page).open()
        picker.pick_date(day=10, month_index=4, year=1995)
        expect(picker.date_input).to_have_value("05/10/1995")


@allure.feature("Widgets")
@allure.story("Tool Tips")
class TestToolTips:

    @allure.title("Подсказка появляется при наведении на кнопку")
    def test_tooltip_on_hover(self, page):
        tooltips = ToolTipsPage(page).open()
        tooltips.show_tooltip()
        expect(tooltips.tooltip).to_have_text("You hovered over the Button")
