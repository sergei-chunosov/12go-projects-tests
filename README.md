## Проект по тестированию сайта 12go.asia
> <a target="_blank" href="https://12go.asia">Ссылка на сайт</a>

#### Список проверок, реализованных в web автотестах
- [x] Проверка выбора валюты
- [x] Проверка изменение языка
- [x] Проверка поиска и добавления билета в корзину
- [x] Проверка авторизации
- [x] Проверка logout
- [x] Проверка перехода на страницу 'About us'
- [x] Проверка перехода на страницу 'Terms and Conditions'
- [x] Проверка изменения профиля пользователя

#### Список проверок, реализованных в mobile автотестах
- [x] Проверка смены даты отправления
- [x] Проверка смены валюты 
- [x] Проверка изменения язвка приложения
- [x] Проверка зеркальной смены направления
- [x] Проверка изменения количества пассажиров
- [x] Проверка выбора направления

#### Список проверок, реализованных в api автотестах
- [x] Проверка успешной авторизации
- [x] Проверка авторизации с невалидными данными 

### Структура проекта

### Проект реализован с использованием
Python Pytest PyCharm Selenoid Selene Jenkins Allure Report Telegram AllureTestOps 

<img src="/resources/python-original.svg" alt="Image 1" width="45" height="45"><img src="/resources/pytest-original.svg" alt="Image 2" width="45" height="45"><img src="/resources/PyCharm_Icon.svg" alt="Image 3" width="45" height="45"><img src="/resources/selenoid.png" alt="Image 4" width="45" height="45"><img src="/resources/jenkins-original.svg" alt="Image 5" width="45" height="45">
<img src="/resources/allure.png" alt="Image 6" width="45" height="45"><img src="/resources/telegram.svg" alt="Image 7" width="45" height="45"><img src="/resources/AllureTestOps.png" alt="Image 8" width="45" height="45">

# Для запуска автотестов используется Jenkins

### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/tests_12go/">проект</a>

![This is an image](/resources/screens/Jenkins_main.png)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить версию браузера
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/resources/screens/allure_report.png)

### Локальный запуск автотестов
1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команд:
  ```bash
  pytest -sv -m mobile tests/mobile/
  pytest -sv -m web
  pytest -sv -m api
  ```

Получение отчёта allure:
```bash
allure serve allure-results
```

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/resources/screens/bot.png)

### Интеграция с jira
![This is an image](/resources/screens/jira.png)

### Пример видеозаписи прохождения мобильных тестов тестов
![This is an image](/resources/screens/mobile.gif)

