import allure
import pytest
from playwright.sync_api import expect

from pages.interactions import DroppablePage

pytestmark = pytest.mark.interactions


@allure.feature("Interactions")
@allure.story("Droppable")
class TestDroppable:

    @allure.title("Перетаскивание элемента в зону сброса")
    def test_drag_and_drop(self, page):
        droppable = DroppablePage(page).open()
        droppable.drag_to_target()
        expect(droppable.drop_target).to_have_text("Dropped!")
