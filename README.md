# Простой ВК бот для беседы /server/

<p align="center">
  <img src="https://img.shields.io/badge/version-0.3-green">
  <img src="https://img.shields.io/badge/for-VK-blue">
  <img src="https://img.shields.io/badge/python-3.11%2B-yellow">
</p>
  
## Инструкция по запуску
### Шаг 1. Подготовка сообщества к работе бота
Зайти в настройки сообщества, во вкладке "Сообщения" включить опцию "Сообщения сообществу".

![image](https://user-images.githubusercontent.com/63950114/207946750-9d76be00-5686-4517-ab5c-4faf5b986dec.png)
![image](https://user-images.githubusercontent.com/63950114/207947497-dabb401e-5f8e-44bf-80ce-612a26af0c89.png)
____
Перейти в подкладку "Настройки для бота" и включить опцию "Возможности ботов", а также поставить галочку на "Разрешать добавлять сообщество в чаты".

![image](https://user-images.githubusercontent.com/63950114/207947896-32ac52b7-bd86-4c68-a22d-7fdd7a4a509d.png)
____
Перейти во вкладку "Настройки" и подкладку "Работа с API", откройте "Long Poll API" и включить данную функцию

![image](https://user-images.githubusercontent.com/63950114/207948967-2cd817b1-bc77-4268-ac0d-a559f5450e8f.png)
____
Перейти в "Типы событий" и поставить галочки, как на скрине

![image](https://user-images.githubusercontent.com/63950114/207948591-a7b346c4-ffc8-4a9b-9cb7-d29802d8b3d7.png)
____
### Шаг 2. Получение токена
Зайдите во вкладку "Настройки" и подкладку "Работа c API", "Ключи доступа" и нажмите кнопку "Создать ключ"

![image](https://user-images.githubusercontent.com/63950114/207949676-5cd1d957-0a64-472d-a128-60b609f810d2.png)
____
В "Создание ключа доступа" выберите пункты "Разрешить приложению доступ к управлению сообществом", чтобы я украл ваш уёбищный паблик, и "Разрешить приложению доступ к сообщениям сообщества", чтобы я писал всем подписчикам, что их гифки с гигачадом дерьмище ебаное.

![image](https://user-images.githubusercontent.com/63950114/207950078-18247bb2-2987-46bc-9b1a-a4eda5b42aa0.png)
____
Из окошка копируем полученный токен.

![image](https://user-images.githubusercontent.com/63950114/207950467-241a77d6-4a8e-417e-b194-bf016f9bb1f5.png)
____
### Шаг 3. Дрочим письку
Скачиваем бота и распаковываем в папку где удобно

![image](https://user-images.githubusercontent.com/63950114/211202817-5613fdd5-83b6-4ab7-8ae2-1ec0cebaade3.png)
____
Заходим на офф. сайт Питона (https://www.python.org/) и наводимся на вкладку Downloads, скачиваем и устанавливаем.

![image](https://user-images.githubusercontent.com/63950114/211203356-5f6606cc-f665-4114-b38f-a902205720bc.png)
____
Открываем консоль от имени администратора и вписываем команду cd и путь до папки с ботом. Затем введите команду `pip install -r requirements.txt`. Начнётся установка всех требуемых библиотек.

![image](https://user-images.githubusercontent.com/63950114/211203444-7b2a1ea7-c3da-45b4-8498-c24d7c5d3091.png)
![image](https://user-images.githubusercontent.com/63950114/211203768-daa0e994-951a-41fa-8ebc-b23f39dc98cd.png)
____
Открываем config.py обычным Блокнотом и вводим туда токен, который мы получили ранее. В той же консоли, которой мы пользовались ранее, запускаем bot.py командой `python bot.py` или `py bot.py`.
