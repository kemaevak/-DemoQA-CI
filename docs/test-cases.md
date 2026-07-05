# Тест-кейсы

Общее предусловие для всех кейсов: открыт сайт https://demoqa.com,
браузер Chromium, разрешение 1280x720.

Кейсы со статусом **Failed** ссылаются на дефект в
[bug-reports.md](bug-reports.md). Колонка «Авто» показывает, покрыт ли
кейс автотестом (название теста в каталоге `tests/`).

## Elements

### Text Box

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-01 | Отправка формы с корректными данными | 1. Открыть /text-box<br>2. Заполнить Full Name, Email, Current Address, Permanent Address корректными данными<br>3. Нажать Submit | Под формой появляется блок с введёнными данными без искажений | High | Passed | test_submit_valid_data |
| TC-02 | Ввод email некорректного формата | 1. Открыть /text-box<br>2. В поле Email ввести строку без @ (например «не-email»)<br>3. Нажать Submit | Поле Email подсвечивается как ошибочное, данные не выводятся | High | Passed | test_invalid_email_is_highlighted |
| TC-03 | Сообщение об ошибке валидации email | 1. Повторить шаги TC-02 | Рядом с полем выводится текст с описанием ошибки | Medium | **Failed** ([BUG-009](bug-reports.md#bug-009)) | — |
| TC-04 | Отправка пустой формы | 1. Открыть /text-box<br>2. Ничего не заполняя, нажать Submit | Обязательные поля подсвечиваются, форма не отправляется | Medium | **Failed** ([BUG-002](bug-reports.md#bug-002)) | — |

### Check Box

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-05 | Выбор корневого чекбокса | 1. Открыть /checkbox<br>2. Отметить чекбокс Home | Все 17 вложенных элементов отмечены и перечислены в результате | High | Passed | test_select_all_via_root |
| TC-06 | Выбор одного вложенного чекбокса | 1. Открыть /checkbox<br>2. Раскрыть узлы Home и Desktop<br>3. Отметить Notes | В результате только notes, соседние элементы не отмечены | High | Passed | test_select_single_item |

### Radio Button

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-07 | Выбор варианта Yes | 1. Открыть /radio-button<br>2. Выбрать Yes | В результате выводится «Yes» | High | Passed | test_select_yes |
| TC-08 | Выбор варианта Impressive | 1. Открыть /radio-button<br>2. Выбрать Impressive | В результате выводится «Impressive» | High | Passed | test_select_impressive |
| TC-09 | Выбор варианта No | 1. Открыть /radio-button<br>2. Выбрать No | Вариант доступен, в результате выводится «No» | Medium | **Failed** ([BUG-001](bug-reports.md#bug-001)) | test_no_is_disabled (фиксирует текущее поведение) |

### Web Tables

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-10 | Добавление записи | 1. Открыть /webtables<br>2. Нажать Add<br>3. Заполнить все поля корректными данными<br>4. Нажать Submit | Форма закрывается, запись появляется в таблице | High | Passed | test_add_record |
| TC-11 | Поиск по таблице | 1. Открыть /webtables<br>2. Ввести в поиск «Cierra» | В таблице остаётся одна строка с Cierra | High | Passed | test_search |
| TC-12 | Редактирование записи | 1. Открыть /webtables<br>2. Нажать иконку редактирования у строки Cierra<br>3. Изменить Age на 45<br>4. Нажать Submit | Изменение сохраняется, в строке отображается 45 | High | Passed | test_edit_record |
| TC-13 | Удаление записи | 1. Открыть /webtables<br>2. Нажать иконку удаления у строки Alden | Строка исчезает из таблицы | High | Passed | test_delete_record |
| TC-14 | Отправка пустой формы регистрации | 1. Открыть /webtables<br>2. Нажать Add<br>3. Нажать Submit | Форма не отправляется, пустые поля подсвечиваются | Medium | Passed | test_empty_form_is_not_submitted |
| TC-15 | Граничные значения возраста и зарплаты | 1. Открыть /webtables<br>2. Нажать Add<br>3. Заполнить форму, указав Age = 0 и Salary = 0<br>4. Нажать Submit | Значения отклоняются как недопустимые | Low | **Failed** ([BUG-007](bug-reports.md#bug-007)) | — |

### Buttons

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-16 | Двойной клик | 1. Открыть /buttons<br>2. Дважды кликнуть Double Click Me | Появляется сообщение «You have done a double click» | Medium | Passed | test_double_click |
| TC-17 | Клик правой кнопкой | 1. Открыть /buttons<br>2. Кликнуть правой кнопкой Right Click Me | Появляется сообщение «You have done a right click» | Medium | Passed | test_right_click |
| TC-18 | Клик по кнопке с динамическим id | 1. Открыть /buttons<br>2. Кликнуть Click Me | Появляется сообщение «You have done a dynamic click» | Medium | Passed | test_dynamic_click |

### Links

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-19 | Переход по простой ссылке | 1. Открыть /links<br>2. Кликнуть Home | Главная страница открывается в новой вкладке | Medium | Passed | test_simple_link_opens_new_tab |
| TC-20 | API-ссылка Created | 1. Открыть /links<br>2. Кликнуть Created | Выводится корректное сообщение о статусе 201 без опечаток | Medium | **Failed** ([BUG-003](bug-reports.md#bug-003)) | test_created_link_returns_201 (проверяет статус) |

### Upload and Download

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-21 | Загрузка файла | 1. Открыть /upload-download<br>2. Нажать Choose File и выбрать текстовый файл | Имя файла отображается на странице | Medium | Passed | test_upload_file |
| TC-22 | Скачивание файла | 1. Открыть /upload-download<br>2. Нажать Download | Скачивается файл sampleFile.jpeg | Medium | Passed | test_download_file |

### Dynamic Properties

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-23 | Активация кнопки по таймеру | 1. Открыть /dynamic-properties<br>2. Подождать 5 секунд | Кнопка Will enable 5 seconds становится активной | Medium | Passed | test_button_enables_after_delay |
| TC-24 | Смена цвета кнопки | 1. Открыть /dynamic-properties<br>2. Подождать 5 секунд | Текст кнопки Color Change становится красным | Low | Passed | test_button_changes_color |
| TC-25 | Появление кнопки по таймеру | 1. Открыть /dynamic-properties<br>2. Подождать 5 секунд | Появляется кнопка Visible After 5 Seconds | Medium | Passed | test_button_appears_after_delay |

## Forms / Practice Form

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-26 | Отправка полностью заполненной формы | 1. Открыть /automation-practice-form<br>2. Заполнить все поля: имя, фамилия, email, пол, телефон, предмет, хобби, адрес, штат, город<br>3. Нажать Submit | Открывается модальное окно «Thanks for submitting the form», данные в таблице соответствуют введённым | High | Passed | test_submit_full_form |
| TC-27 | Отправка только обязательных полей | 1. Открыть /automation-practice-form<br>2. Заполнить имя, фамилию, пол, телефон<br>3. Нажать Submit | Форма отправляется, модальное окно открывается | High | Passed | test_submit_required_fields_only |
| TC-28 | Телефон короче 10 цифр | 1. Открыть /automation-practice-form<br>2. Заполнить обязательные поля, телефон — «12345»<br>3. Нажать Submit | Форма не отправляется, поле подсвечивается | High | Passed | test_short_phone_number_blocks_submit |
| TC-29 | Отправка пустой формы | 1. Открыть /automation-practice-form<br>2. Нажать Submit | Форма не отправляется, обязательные поля подсвечиваются | Medium | Passed | test_empty_form_is_not_submitted |
| TC-30 | Загрузка не-изображения в Select Picture | 1. Открыть /automation-practice-form<br>2. В поле Select Picture выбрать файл .txt | Файл отклоняется, выводится сообщение о допустимых форматах | Low | **Failed** ([BUG-006](bug-reports.md#bug-006)) | — |

## Alerts, Frame & Windows

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-31 | Открытие новой вкладки | 1. Открыть /browser-windows<br>2. Нажать New Tab | Открывается вкладка с текстом «This is a sample page» | Medium | Passed | test_new_tab |
| TC-32 | Простой alert | 1. Открыть /alerts<br>2. Нажать Click me у первого алерта | Появляется alert «You clicked a button», закрывается по Ok | Medium | Passed | test_simple_alert |
| TC-33 | Подтверждение confirm | 1. Открыть /alerts<br>2. Нажать кнопку confirm-диалога<br>3. Выбрать Ok | На странице выводится «You selected Ok» | Medium | Passed | test_confirm_accept |
| TC-34 | Отмена confirm | 1. Открыть /alerts<br>2. Нажать кнопку confirm-диалога<br>3. Выбрать Cancel | На странице выводится «You selected Cancel» | Medium | Passed | test_confirm_dismiss |
| TC-35 | Ввод текста в prompt | 1. Открыть /alerts<br>2. Нажать кнопку prompt-диалога<br>3. Ввести имя, нажать Ok | Введённое имя выводится в результате | Medium | Passed | test_prompt_with_text |
| TC-36 | Содержимое фреймов | 1. Открыть /frames | Оба iframe содержат текст «This is a sample page» | Low | Passed | test_frame_content |
| TC-37 | Маленькое модальное окно | 1. Открыть /modal-dialogs<br>2. Нажать Small Modal<br>3. Закрыть окно кнопкой Close | Окно открывается с заголовком «Small Modal» и закрывается | Medium | Passed | test_small_modal |
| TC-38 | Большое модальное окно | 1. Открыть /modal-dialogs<br>2. Нажать Large Modal<br>3. Закрыть окно кнопкой Close | Окно открывается с заголовком «Large Modal» и закрывается | Medium | Passed | test_large_modal |

## Widgets

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-39 | Accordion: состояние по умолчанию | 1. Открыть /accordian | Первая секция раскрыта, остальные свёрнуты | Low | Passed | test_first_section_open_by_default |
| TC-40 | Accordion: переключение секций | 1. Открыть /accordian<br>2. Кликнуть по заголовку второй секции | Вторая секция раскрывается, первая сворачивается | Low | Passed | test_open_second_section |
| TC-41 | Select Menu: классический select | 1. Открыть /select-menu<br>2. В Old Style Select Menu выбрать Green | Выбранное значение отображается в селекте | Medium | Passed | test_old_style_select |
| TC-42 | Progress Bar: запуск и остановка | 1. Открыть /progress-bar<br>2. Нажать Start<br>3. Через 1–2 секунды нажать Stop | Прогресс останавливается на промежуточном значении | Medium | Passed | test_start_and_stop |
| TC-43 | Slider: перемещение клавиатурой | 1. Открыть /slider<br>2. Кликнуть по ползунку<br>3. Нажать стрелку вправо 5 раз | Значение в поле увеличивается | Medium | Passed | test_move_slider_with_keyboard |
| TC-44 | Date Picker: выбор даты | 1. Открыть /date-picker<br>2. Открыть календарь<br>3. Выбрать 10 мая 1995 | В поле отображается 05/10/1995 | Medium | Passed | test_pick_date |
| TC-45 | Tool Tips: подсказка на кнопке | 1. Открыть /tool-tips<br>2. Навести курсор на кнопку | Появляется подсказка «You hovered over the Button» | Low | Passed | test_tooltip_on_hover |

## Interactions

| ID | Название | Шаги | Ожидаемый результат | Приоритет | Статус | Авто |
|---|---|---|---|---|---|---|
| TC-46 | Droppable: перетаскивание | 1. Открыть /droppable<br>2. Перетащить Drag me в зону Drop here | Текст зоны меняется на «Dropped!», зона подсвечивается | Medium | Passed | test_drag_and_drop |

## Итоги

- Всего кейсов: 46
- Passed: 40
- Failed: 6 (все дефекты задокументированы в [bug-reports.md](bug-reports.md);
  ещё три дефекта — BUG-004, BUG-005, BUG-008 — найдены при
  исследовательском тестировании вне кейсов)
- Покрыто автотестами: 42
