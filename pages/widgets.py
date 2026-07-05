from pages.base_page import BasePage


class AccordionPage(BasePage):
    """Страница Widgets -> Accordion.

    В адресе страницы на сайте опечатка — accordian (см. BUG-005).
    """

    url = "/accordian"

    def __init__(self, page):
        super().__init__(page)
        container = page.locator("#accordianContainer")
        self.buttons = container.locator(".accordion-button")
        self.sections = container.locator(".accordion-item")

    def section_content(self, index):
        return self.sections.nth(index).locator(".accordion-collapse")


class SelectMenuPage(BasePage):
    """Страница Widgets -> Select Menu."""

    url = "/select-menu"

    def __init__(self, page):
        super().__init__(page)
        self.old_select = page.locator("#oldSelectMenu")


class ProgressBarPage(BasePage):
    """Страница Widgets -> Progress Bar."""

    url = "/progress-bar"

    def __init__(self, page):
        super().__init__(page)
        self.start_stop_button = page.locator("#startStopButton")
        self.bar = page.locator(".progress-bar")

    def value(self):
        return int(self.bar.get_attribute("aria-valuenow"))


class SliderPage(BasePage):
    """Страница Widgets -> Slider."""

    url = "/slider"

    def __init__(self, page):
        super().__init__(page)
        self.slider = page.locator(".range-slider")
        self.value_input = page.locator("#sliderValue")


class DatePickerPage(BasePage):
    """Страница Widgets -> Date Picker."""

    url = "/date-picker"

    def __init__(self, page):
        super().__init__(page)
        self.date_input = page.locator("#datePickerMonthYearInput")
        self.month_select = page.locator(".react-datepicker__month-select")
        self.year_select = page.locator(".react-datepicker__year-select")

    def pick_date(self, day, month_index, year):
        """Выбирает дату через календарь. month_index: 0 — январь."""
        self.date_input.click()
        self.month_select.select_option(str(month_index))
        self.year_select.select_option(str(year))
        day_class = f".react-datepicker__day--{day:03d}"
        self.page.locator(
            f"{day_class}:not(.react-datepicker__day--outside-month)"
        ).click()


class ToolTipsPage(BasePage):
    """Страница Widgets -> Tool Tips."""

    url = "/tool-tips"

    def __init__(self, page):
        super().__init__(page)
        self.button = page.locator("#toolTipButton")
        self.tooltip = page.locator(".tooltip-inner")

    def show_tooltip(self):
        """Наводит курсор на кнопку и дожидается подсказки.

        Сразу после загрузки страница может не успеть навесить
        обработчики, поэтому при необходимости наводим повторно.
        """
        for _ in range(3):
            self.button.hover()
            try:
                self.tooltip.wait_for(state="visible", timeout=3_000)
                return
            except Exception:
                # уводим курсор и пробуем ещё раз
                self.page.mouse.move(0, 0)
                self.page.wait_for_timeout(500)
        self.button.hover()
