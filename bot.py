from vkbottle.bot import Bot, Message # Импорт библиотеки
from loguru import logger
import random
from config import TokenPenis
from time import sleep
from sys import exit

if TokenPenis == 'None':
    print('Введите токен в файл config.py (файл можно открыть обычным блокнотом) \n'
          'Через 60 секунд программа сама закроется, или сам закрой, мне похуй')
    sleep(60)
    exit(0)

else:
    bot = Bot(TokenPenis)

@bot.on.message(text="/help") # Задаю хуйню, чтобы при появлении "/help" в чате, писалось сообщение
async def help_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id) # Получение информации о человеке, который ввёл команду
    await message.answer(f'[id{users_info[0].id}|{users_info[0].first_name}], вот что я могу:\n '
                         '\n'                        
                         '/help - выдаёт эту хуйню\n'
                         '/viewmap - онлайн-карта сервера\n'
                         '/staff - разрабы сервера'
                         ) # Сам текст, {users_info[0].id} - айди страницы человека, {users.info[0].first_name} - имя


@bot.on.message(text="/viewmap")
async def map_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer(f"[id{users_info[0].id}|{users_info[0].first_name}], карта сервера: http://n21.joinserver.ru:25663/")


@bot.on.message(text="/staff")
async def staff_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer(f'[id{users_info[0].id}|{users_info[0].first_name}], вот все разработчики сервера:\n'
                         '\n'
                         'Антон Шмагин (https://vk.com/aantoss) и Павел Одинцов (https://vk.com/errormaned)')

@bot.on.message(text="/ПРИКАЗ <text>")
async def prikaz_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    prikaz_number = random.randint(10,10000)
    if users_info[0].id == 231416101:
        await message.answer(f'ПО ПРИКАЗУ [id231416101|ДАНИИЛА] №{prikaz_number}')
    else:
        await message.answer(f'[id{users_info[0].id}|Ты] долбоёб?')




@bot.on.message(text="/lobanov_suka") # пасхалки
async def lobanov_handler(message: Message):
    await message.answer('Влад, иди нахуй пожалуйста')
@bot.on.message(text="/lzrd")
async def lizard_handler(message: Message):
    await message.answer('by LizardSquad dev')

bot.run_forever()
print('Copyright © 2022 vuwWolf')