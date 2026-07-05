import pytest
from playwright.sync_api import expect

# demoqa.com иногда отвечает медленно, поэтому таймаут проверок
# увеличен относительно стандартных 5 секунд
expect.set_options(timeout=10_000)

# Рекламные и трекинговые домены. Их блокировка ускоряет загрузку
# страниц и убирает баннеры, которые перекрывают элементы интерфейса
# (см. BUG-008 в docs/bug-reports.md)
AD_HOSTS = (
    "googlesyndication.com",
    "doubleclick.net",
    "adservice.google",
    "google-analytics.com",
    "googletagmanager.com",
    "pagead2",
    "adsbygoogle",
)


@pytest.fixture(autouse=True)
def block_ads(context):
    def handle(route):
        if any(host in route.request.url for host in AD_HOSTS):
            route.abort()
        else:
            route.continue_()

    context.route("**/*", handle)
    # закреплённый баннер и футер перекрывают нижнюю часть страницы
    context.add_init_script(
        """
        window.addEventListener('DOMContentLoaded', () => {
            document.getElementById('fixedban')?.remove();
            document.querySelector('footer')?.remove();
        });
        """
    )
