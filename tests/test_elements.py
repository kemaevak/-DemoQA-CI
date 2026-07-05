import re

import allure
import pytest
from playwright.sync_api import expect

from pages.elements import (
    ButtonsPage,
    CheckBoxPage,
    DynamicPropertiesPage,
    LinksPage,
    RadioButtonPage,
    TextBoxPage,
    UploadDownloadPage,
    WebTablesPage,
)

pytestmark = pytest.mark.elements


@allure.feature("Elements")
@allure.story("Text Box")
class TestTextBox:

    @allure.title("Отправка формы с корректными данными")
    def test_submit_valid_data(self, page):
        form = TextBoxPage(page).open()
        form.fill_form(
            name="Иван Петров",
            email="ivan.petrov@example.com",
            current="Москва, ул. Ленина, 1",
            permanent="Москва, ул. Ленина, 1",
        )
        form.submit()
        expect(form.output).to_be_visible()
        expect(form.output_name).to_contain_text("Иван Петров")
        expect(form.output_email).to_contain_text("ivan.petrov@example.com")

    @allure.title("Email некорректного формата не проходит валидацию")
    def test_invalid_email_is_highlighted(self, page):
        form = TextBoxPage(page).open()
        form.email.fill("не-email")
        form.submit()
        # поле подсвечивается красным, данные не выводятся
        expect(form.email).to_have_class(re.compile("field-error"))
        expect(form.output_email).to_have_count(0)


@allure.feature("Elements")
@allure.story("Check Box")
class TestCheckBox:

    @allure.title("Выбор корневого чекбокса отмечает все вложенные")
    def test_select_all_via_root(self, page):
        checkbox = CheckBoxPage(page).open()
        checkbox.toggle("Home")
        # в дереве 17 элементов, все должны попасть в результат
        expect(checkbox.selected_items).to_have_count(17)
        assert "notes" in checkbox.selected_names()

    @allure.title("Выбор одного вложенного чекбокса")
    def test_select_single_item(self, page):
        checkbox = CheckBoxPage(page).open()
        checkbox.expand("Home")
        checkbox.expand("Desktop")
        checkbox.toggle("Notes")
        expect(checkbox.selected_items).to_have_count(1)
        assert checkbox.selected_names() == ["notes"]


@allure.feature("Elements")
@allure.story("Radio Button")
class TestRadioButton:

    @allure.title("Выбор варианта Yes")
    def test_select_yes(self, page):
        radio = RadioButtonPage(page).open()
        radio.yes_radio.click()
        expect(radio.result).to_have_text("Yes")

    @allure.title("Выбор варианта Impressive")
    def test_select_impressive(self, page):
        radio = RadioButtonPage(page).open()
        radio.impressive_radio.click()
        expect(radio.result).to_have_text("Impressive")

    @allure.title("Вариант No недоступен для выбора (BUG-001)")
    def test_no_is_disabled(self, page):
        # фиксируем текущее поведение, дефект описан в BUG-001
        radio = RadioButtonPage(page).open()
        expect(radio.no_radio_input).to_be_disabled()


@allure.feature("Elements")
@allure.story("Web Tables")
class TestWebTables:

    record = {
        "first": "Anna",
        "last": "Smirnova",
        "email": "anna.smirnova@example.com",
        "age": "29",
        "salary": "75000",
        "department": "QA",
    }

    @allure.title("Добавление новой записи в таблицу")
    def test_add_record(self, page):
        table = WebTablesPage(page).open()
        table.add_record(**self.record)
        expect(table.registration_form).to_be_hidden()
        expect(table.row_with_text("Smirnova")).to_have_count(1)

    @allure.title("Поиск по таблице")
    def test_search(self, page):
        table = WebTablesPage(page).open()
        table.search_input.fill("Cierra")
        expect(table.rows).to_have_count(1)
        expect(table.rows.first).to_contain_text("Cierra")

    @allure.title("Редактирование существующей записи")
    def test_edit_record(self, page):
        table = WebTablesPage(page).open()
        table.edit_row("Cierra")
        table.age.fill("45")
        table.submit_button.click()
        expect(table.row_with_text("Cierra")).to_contain_text("45")

    @allure.title("Удаление записи")
    def test_delete_record(self, page):
        table = WebTablesPage(page).open()
        table.delete_row("Alden")
        expect(table.row_with_text("Alden")).to_have_count(0)

    @allure.title("Пустая форма регистрации не отправляется")
    def test_empty_form_is_not_submitted(self, page):
        table = WebTablesPage(page).open()
        table.add_button.click()
        table.submit_button.click()
        # форма остаётся открытой, запись не создаётся
        expect(table.registration_form).to_be_visible()


@allure.feature("Elements")
@allure.story("Buttons")
class TestButtons:

    @allure.title("Двойной клик")
    def test_double_click(self, page):
        buttons = ButtonsPage(page).open()
        buttons.double_click_button.dblclick()
        expect(buttons.double_click_message).to_have_text(
            "You have done a double click"
        )

    @allure.title("Клик правой кнопкой мыши")
    def test_right_click(self, page):
        buttons = ButtonsPage(page).open()
        buttons.right_click_button.click(button="right")
        expect(buttons.right_click_message).to_have_text(
            "You have done a right click"
        )

    @allure.title("Обычный клик по кнопке с динамическим id")
    def test_dynamic_click(self, page):
        buttons = ButtonsPage(page).open()
        buttons.dynamic_click_button.click()
        expect(buttons.dynamic_click_message).to_have_text(
            "You have done a dynamic click"
        )


@allure.feature("Elements")
@allure.story("Links")
class TestLinks:

    @allure.title("Простая ссылка открывает главную в новой вкладке")
    def test_simple_link_opens_new_tab(self, page):
        links = LinksPage(page).open()
        with page.expect_popup() as popup_info:
            links.simple_link.click()
        new_tab = popup_info.value
        assert new_tab.url.rstrip("/") == "https://demoqa.com"

    @allure.title("API-ссылка Created возвращает статус 201")
    def test_created_link_returns_201(self, page):
        links = LinksPage(page).open()
        links.created_link.click()
        # в тексте ответа на сайте опечатка "staus" — см. BUG-003
        expect(links.response).to_contain_text("201")
        expect(links.response).to_contain_text("Created")


@allure.feature("Elements")
@allure.story("Upload and Download")
class TestUploadDownload:

    @allure.title("Загрузка файла")
    def test_upload_file(self, page, tmp_path):
        upload_page = UploadDownloadPage(page).open()
        test_file = tmp_path / "резюме.txt"
        test_file.write_text("тестовый файл для загрузки", encoding="utf-8")
        upload_page.upload_input.set_input_files(test_file)
        expect(upload_page.uploaded_path).to_contain_text("резюме.txt")

    @allure.title("Скачивание файла")
    def test_download_file(self, page):
        upload_page = UploadDownloadPage(page).open()
        with page.expect_download() as download_info:
            upload_page.download_button.click()
        download = download_info.value
        assert download.suggested_filename == "sampleFile.jpeg"


@allure.feature("Elements")
@allure.story("Dynamic Properties")
class TestDynamicProperties:

    @allure.title("Кнопка становится активной через 5 секунд")
    def test_button_enables_after_delay(self, page):
        dynamic = DynamicPropertiesPage(page).open()
        expect(dynamic.enable_after_button).to_be_enabled(timeout=7_000)

    @allure.title("Кнопка меняет цвет текста")
    def test_button_changes_color(self, page):
        dynamic = DynamicPropertiesPage(page).open()
        expect(dynamic.color_change_button).to_have_class(
            re.compile("text-danger"), timeout=7_000
        )

    @allure.title("Кнопка появляется через 5 секунд")
    def test_button_appears_after_delay(self, page):
        dynamic = DynamicPropertiesPage(page).open()
        expect(dynamic.visible_after_button).to_be_visible(timeout=7_000)
