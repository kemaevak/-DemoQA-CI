from pages.base_page import BasePage


class DroppablePage(BasePage):
    """Страница Interactions -> Droppable."""

    url = "/droppable"

    def __init__(self, page):
        super().__init__(page)
        self.draggable = page.locator("#draggable")
        self.drop_target = page.locator("#simpleDropContainer #droppable")

    def drag_to_target(self):
        """Перетаскивает элемент с промежуточными движениями мыши.

        Обычный drag_to здесь не срабатывает: страница построена на
        jQuery UI, которому нужны события mousemove между нажатием
        и отпусканием кнопки.
        """
        # jQuery UI навешивает обработчики не сразу после загрузки:
        # пока у элемента нет класса ui-draggable, тащить его бесполезно
        self.page.locator("#draggable.ui-draggable").wait_for()
        self.draggable.hover()
        mouse = self.page.mouse
        mouse.down()
        # небольшой сдвиг, чтобы jQuery UI начал перетаскивание
        source = self.draggable.bounding_box()
        mouse.move(source["x"] + 5, source["y"] + 5, steps=2)
        target = self.drop_target.bounding_box()
        mouse.move(
            target["x"] + target["width"] / 2,
            target["y"] + target["height"] / 2,
            steps=15,
        )
        self.page.wait_for_timeout(300)
        mouse.up()
