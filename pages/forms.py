from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    """Страница Forms -> Practice Form."""

    url = "/automation-practice-form"

    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.gender_male = page.locator('label[for="gender-radio-1"]')
        self.gender_female = page.locator('label[for="gender-radio-2"]')
        self.mobile = page.locator("#userNumber")
        self.subjects_input = page.locator("#subjectsInput")
        self.hobby_sports = page.locator('label[for="hobbies-checkbox-1"]')
        self.current_address = page.locator("#currentAddress")
        self.state_dropdown = page.locator("#state")
        self.city_dropdown = page.locator("#city")
        self.submit_button = page.locator("#submit")
        self.modal = page.locator(".modal-content")
        self.modal_title = page.locator("#example-modal-sizes-title-lg")
        self.close_modal_button = page.locator("#closeLargeModal")

    def add_subject(self, subject):
        self.subjects_input.fill(subject)
        self.subjects_input.press("Enter")

    def select_state(self, state):
        self.state_dropdown.click()
        self.page.get_by_text(state, exact=True).click()

    def select_city(self, city):
        self.city_dropdown.click()
        self.page.get_by_text(city, exact=True).click()

    def submit(self):
        self.submit_button.click()

    def result_value(self, label):
        """Возвращает значение из таблицы результатов по названию поля."""
        row = self.modal.locator("tr", has_text=label)
        return row.locator("td").nth(1).inner_text()
