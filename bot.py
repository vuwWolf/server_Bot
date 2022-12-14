from vkbottle.bot import Bot, Message # Импорт библиотеки

TokenPenis = input("Введите токен: ")
bot = Bot(token=TokenPenis) # Вместо TokenPenis ввести токен (не забудь, что кавычки обязательны)

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
                         'Антон "shmgn" Шмагин (https://vk.com/aantoss) - ХУЙ\n'
                         'Паша "ХУЙ" Одинцов (https://vk.com/errormaned) - ХУЙ'
                         )

@bot.on.message(text="Лобанов, пососи-ка мой пятиярдовый хуй") # пасхалОЧКА
async def lobanov_handler(message: Message):
    await message.answer("Влад, иди нахуй пожалуйста")

bot.run_forever()