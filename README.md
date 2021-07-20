Проект бота на Python. Бот выводит сведения о текущей погоде с сайта OpenWetherMap  (https://openweathermap.org).
## Настройка доступа к API OpenWetherMap
***
Пример работы с API OpenWetherMap на Python рассмотрен в https://github.com/jony67/openweather.
***
### Требования к программному обеспечению 
Python >= 3.7.0
## Загрузка на  сервис Heroku
1. Зарегистрироваться на сайте Heroku, получить API KEY.
2. Зайти в терминал и клонировать проект в свою папку:

`$ git clone https://github.com/jony67/telegram-aiogram` 

3. Перейти в папку, куда был распакован проект и развернуть его на Heroku:

`$ heroku login`

`$ heroku create my-tel-bot`

`$ heroku git:remote -a my-tel-bot` 

`$ git push heroku main`

### Внимание!
Если вы не хотите держать свои приватные данные в файле config.py,
Вы можете развернуть приложение на Heroku без этого файла. А сами данные передать в виде переменных окружения.
Тогда Вам нужно:
#### Изменить строки:
- в файле bot.py:
1) закоменировать строку: `from config import TOKEN`
2) раскоментировать строки:
`import os`
`TOKEN = os.getenv("TOKEN")`

- в файле  openweather.py:
1) закоменировать строку: `from config import TOKEN`
2) раскоментировать строки:
`import os`
`KEY = os.getenv("KEY")`
   
#### Настроить переменные окружения в проекте Heroku, после его создания:

`$ heroku config:set TOKEN = 0123456789` (вместо 0123456789 - Ваши данные без ковычек)

`$ heroku config:set KEY = 0123456789` (вместо 0123456789 - Ваши данные без ковычек)

# Пример работы бота
![Пример работы](/img/examp.png)
