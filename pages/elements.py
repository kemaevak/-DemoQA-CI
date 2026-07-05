from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """Страница Elements -> Text Box."""

    url = "/text-box"

    def __init__(self, page):
        super().__init__(page)
        self.full_name = page.locator("#userName")
        self.email = page.locator("#userEmail")
        self.current_address = page.locator("#currentAddress")
        self.permanent_address = page.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output = page.locator("#output")
        self.output_name = page.locator("#output #name")
        self.output_email = page.locator("#output #email")

    def fill_form(self, name, email, current, permanent):
        self.full_name.fill(name)
        self.email.fill(email)
        self.current_address.fill(current)
        self.permanent_address.fill(permanent)

    def submit(self):
        self.submit_button.click()


class CheckBoxPage(BasePage):
    """Страница Elements -> Check Box.

    Дерево построено на компоненте rc-tree, кнопки «развернуть всё»
    на странице нет — узлы раскрываются по одному.
    """

    url = "/checkbox"

    def __init__(self, page):
        super().__init__(page)
        self.result = page.locator("#result")
        self.selected_items = page.locator("#result .text-success")

    def node(self, title):
        return self.page.locator(f'.rc-tree-treenode:has(span[title="{title}"])')

    def expand(self, title):
        """Раскрывает узел дерева по названию."""
        self.node(title).locator(".rc-tree-switcher").click()

    def toggle(self, title):
        """Отмечает или снимает чекбокс по названию."""
        self.node(title).locator(".rc-tree-checkbox").click()

    def selected_names(self):
        return self.selected_items.all_inner_texts()


class RadioButtonPage(BasePage):
    """Страница Elements -> Radio Button."""

    url = "/radio-button"

    def __init__(self, page):
        super().__init__(page)
        self.yes_radio = page.locator('label[for="yesRadio"]')
        self.impressive_radio = page.locator('label[for="impressiveRadio"]')
        self.no_radio_input = page.locator("#noRadio")
        self.result = page.locator(".text-success")


class WebTablesPage(BasePage):
    """Страница Elements -> Web Tables."""

    url = "/webtables"

    def __init__(self, page):
        super().__init__(page)
        self.add_button = page.locator("#addNewRecordButton")
        self.search_input = page.locator("#searchBox")
        self.registration_form = page.locator(".modal-content")
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.age = page.locator("#age")
        self.salary = page.locator("#salary")
        self.department = page.locator("#department")
        self.submit_button = page.locator("#submit")
        self.rows = page.locator("table tbody tr")

    def add_record(self, first, last, email, age, salary, department):
        self.add_button.click()
        self.fill_registration_form(first, last, email, age, salary, department)
        self.submit_button.click()

    def fill_registration_form(self, first, last, email, age, salary, department):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.age.fill(age)
        self.salary.fill(salary)
        self.department.fill(department)

    def row_with_text(self, text):
        return self.rows.filter(has_text=text)

    def edit_row(self, text):
        self.row_with_text(text).locator('span[title="Edit"]').click()

    def delete_row(self, text):
        self.row_with_text(text).locator('span[title="Delete"]').click()


class ButtonsPage(BasePage):
    """Страница Elements -> Buttons."""

    url = "/buttons"

    def __init__(self, page):
        super().__init__(page)
        self.double_click_button = page.locator("#doubleClickBtn")
        self.right_click_button = page.locator("#rightClickBtn")
        # у третьей кнопки динамический id, ищем по точному тексту
        self.dynamic_click_button = page.get_by_role("button", name="Click Me", exact=True)
        self.double_click_message = page.locator("#doubleClickMessage")
        self.right_click_message = page.locator("#rightClickMessage")
        self.dynamic_click_message = page.locator("#dynamicClickMessage")


class LinksPage(BasePage):
    """Страница Elements -> Links."""

    url = "/links"

    def __init__(self, page):
        super().__init__(page)
        self.simple_link = page.locator("#simpleLink")
        self.created_link = page.locator("#created")
        self.response = page.locator("#linkResponse")


class UploadDownloadPage(BasePage):
    """Страница Elements -> Upload and Download."""

    url = "/upload-download"

    def __init__(self, page):
        super().__init__(page)
        self.upload_input = page.locator("#uploadFile")
        self.uploaded_path = page.locator("#uploadedFilePath")
        self.download_button = page.locator("#downloadButton")


class DynamicPropertiesPage(BasePage):
    """Страница Elements -> Dynamic Properties."""

    url = "/dynamic-properties"

    def __init__(self, page):
        super().__init__(page)
        self.enable_after_button = page.locator("#enableAfter")
        self.color_change_button = page.locator("#colorChange")
        self.visible_after_button = page.locator("#visibleAfter")
