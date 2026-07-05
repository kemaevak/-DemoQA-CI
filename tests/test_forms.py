import allure
import pytest
from playwright.sync_api import expect

from pages.forms import PracticeFormPage

pytestmark = pytest.mark.forms


@allure.feature("Forms")
@allure.story("Practice Form")
class TestPracticeForm:

    @allure.title("Отправка формы, заполненной полностью")
    def test_submit_full_form(self, page):
        form = PracticeFormPage(page).open()
        form.first_name.fill("Мария")
        form.last_name.fill("Иванова")
        form.email.fill("maria.ivanova@example.com")
        form.gender_female.click()
        form.mobile.fill("9161234567")
        form.add_subject("Maths")
        form.hobby_sports.click()
        form.current_address.fill("Санкт-Петербург, Невский пр., 10")
        form.select_state("NCR")
        form.select_city("Delhi")
        form.submit()

        expect(form.modal_title).to_have_text("Thanks for submitting the form")
        assert form.result_value("Student Name") == "Мария Иванова"
        assert form.result_value("Student Email") == "maria.ivanova@example.com"
        assert form.result_value("Mobile") == "9161234567"
        assert form.result_value("State and City") == "NCR Delhi"

    @allure.title("Отправка формы только с обязательными полями")
    def test_submit_required_fields_only(self, page):
        form = PracticeFormPage(page).open()
        form.first_name.fill("Пётр")
        form.last_name.fill("Сидоров")
        form.gender_male.click()
        form.mobile.fill("9037654321")
        form.submit()

        expect(form.modal_title).to_have_text("Thanks for submitting the form")
        assert form.result_value("Student Name") == "Пётр Сидоров"

    @allure.title("Форма не отправляется с коротким номером телефона")
    def test_short_phone_number_blocks_submit(self, page):
        form = PracticeFormPage(page).open()
        form.first_name.fill("Пётр")
        form.last_name.fill("Сидоров")
        form.gender_male.click()
        form.mobile.fill("12345")  # нужно 10 цифр
        form.submit()

        expect(form.modal).to_be_hidden()

    @allure.title("Форма не отправляется без обязательных полей")
    def test_empty_form_is_not_submitted(self, page):
        form = PracticeFormPage(page).open()
        form.submit()
        expect(form.modal).to_be_hidden()
