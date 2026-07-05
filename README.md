# Тестирование веб-приложения DemoQA

![UI-тесты](https://github.com/kemaevak/-DemoQA-CI/actions/workflows/tests.yml/badge.svg)

Учебный QA-проект: полный цикл тестирования сайта
[demoqa.com](https://demoqa.com) — от тест-плана и ручного прохождения
кейсов до автотестов на Playwright и запуска в CI.

## Что сделано

- составлен [тест-план](docs/test-plan.md) с областью тестирования и рисками;
- проведено исследовательское и ручное тестирование по [чек-листам](docs/checklist.md);
- написано [46 тест-кейсов](docs/test-cases.md) по пяти разделам сайта;
- найдено и оформлено [9 дефектов](docs/bug-reports.md) со скриншотами;
- регрессионные сценарии покрыты **42 автотестами** (Python + pytest + Playwright);
- настроен запуск тестов в GitHub Actions с сохранением Allure-результатов.

## Стек

| Инструмент | Зачем |
|---|---|
| Python + pytest | ядро автотестов |
| Playwright | управление браузером, автоожидания |
| Page Object | селекторы и действия отделены от проверок |
| Allure | отчёты о прогонах |
| pytest-rerunfailures | перезапуск упавших тестов (сайт учебный и нестабильный) |
| GitHub Actions | прогон тестов на каждый push |

## Структура проекта

```
├── docs/                    # тест-документация
│   ├── test-plan.md         # тест-план
│   ├── checklist.md         # чек-листы по разделам
│   ├── test-cases.md        # тест-кейсы
│   ├── bug-reports.md       # баг-репорты
│   └── screenshots/         # скриншоты к баг-репортам
├── pages/                   # Page Object'ы
│   ├── base_page.py
│   ├── elements.py          # Text Box, Check Box, Web Tables...
│   ├── forms.py             # Practice Form
│   ├── alerts_windows.py    # алерты, фреймы, окна
│   ├── widgets.py           # аккордеон, слайдер, календарь...
│   └── interactions.py      # drag and drop
├── tests/                   # автотесты (по разделам сайта)
│   ├── conftest.py          # блокировка рекламы, таймауты
│   ├── test_elements.py
│   ├── test_forms.py
│   ├── test_alerts_windows.py
│   ├── test_widgets.py
│   └── test_interactions.py
└── .github/workflows/tests.yml
```

## Запуск

```bash
# установка
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

# все тесты
pytest

# только один раздел
pytest -m elements

# в видимом браузере
pytest --headed
```

Скриншоты упавших тестов сохраняются в `test-results/`.

## Отчёт Allure

Результаты каждого прогона пишутся в `allure-results/`. Чтобы открыть
отчёт, нужен [Allure CLI](https://allurereport.org/docs/install/):

```bash
allure serve allure-results
```

## Особенности, с которыми пришлось разбираться

- **Реклама на сайте.** Баннеры грузятся с задержкой, смещают вёрстку
  и перехватывают клики. В `conftest.py` рекламные домены блокируются
  на уровне контекста браузера — тесты стали стабильнее и быстрее.
- **jQuery UI и drag-and-drop.** Стандартный `drag_to` не работает на
  странице Droppable: jQuery UI требует промежуточных событий движения
  мыши, а обработчики навешиваются с задержкой. Пришлось ждать
  инициализации (класс `ui-draggable`) и двигать мышь по шагам.
- **Медленные ответы сервера.** Сайт учебный, время ответа плавает.
  Таймауты проверок увеличены до 10 секунд, упавшие тесты
  перезапускаются один раз.

## Найденные дефекты (кратко)

| ID | Что не так | Серьёзность |
|---|---|---|
| BUG-001 | Radio Button: вариант «No» нельзя выбрать | Major |
| BUG-002 | Text Box: форма отправляется пустой, обязательных полей нет | Minor |
| BUG-003 | Links: опечатка «staus» в сообщении о статусе | Trivial |
| BUG-004 | Alerts: id кнопки с опечаткой — promtButton | Trivial |
| BUG-005 | «Accordian» вместо «Accordion» в URL и заголовке | Trivial |
| BUG-006 | Practice Form: в поле для фото загружается любой файл | Minor |
| BUG-007 | Web Tables: принимается возраст 0 и зарплата 0 | Minor |
| BUG-008 | Реклама смещает контент и мешает кликам | Minor |
| BUG-009 | Text Box: нет текста ошибки при некорректном email | Minor |

Подробности — в [bug-reports.md](docs/bug-reports.md).
