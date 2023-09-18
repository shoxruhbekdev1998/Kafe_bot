from aiogram import types
from aiogram.types import ContentTypes
from loader import dp, bot, base

# Echo bot

#osh media
# menular = base.select_all_menu()
# @dp.message_handler()
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/2"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Osh narxi--20 000 so'm \n"
#                          "Nomi Toshken oshi")

# @dp.message_handler(text="Pilaf")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/2"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Osh narxi--20 000 so'm \n"
#                          "Nomi Toshken oshi")
#
# #sho'rva media
#
# @dp.message_handler(text="Sho'rva")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/3"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Sho'rva narxi--15 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Ko'za Sho'rva")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/4"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Ko'za Sho'rva narxi--25 000 so'm \n"
#                          "Mol Go'shtida")
#
#
# #eng sho'rva
# @dp.message_handler(text="Soup")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/3"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Sho'rva narxi--15 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Pitcher Soup")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/4"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Ko'za Sho'rva narxi--25 000 so'm \n"
#                          "Mol Go'shtida")
#
#
#
# @dp.message_handler(text="Mastava")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/5"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Mastava narxi--15 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Mastava uzbek")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/5"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Mastava narxi--15 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Suyuq lag'mon")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/6"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Suyuq lag'mon narxi--15 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Suyuq lag'mon uzbek")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/6"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Suyuq lag'mon narxi--15 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
#
# # 2-taomlar
#
# @dp.message_handler(text="Shashlik qiyma")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/7"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Shashlik qiyma narxi--11 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Shashlik qiyma uzbek")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/7"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Shashlik qiyma narxi--11 000 so'm \n"
#                          "Mol Go'shti Sho'rva")
#
# @dp.message_handler(text="Tovuq shashlik")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/8"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Tovuq shashlik narxi--12 000 so'm \n"
#                          )
#
# @dp.message_handler(text="Tovuq shashlik uzbek")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/8"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Tovuq shashlik narxi--12 000 so'm \n"
#                          )
#
# @dp.message_handler(text="Somsa")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/9"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Somsa 1 juft narxi--15 000 so'm \n"
#                          "Mol Go'shtida")
#
# @dp.message_handler(text="Somsa uzbek")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/9"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Somsa 1 juft narxi--15 000 so'm \n"
#                          "Mol Go'shtida")
#
# #Ichimliklar
#
# @dp.message_handler(text="Gazsiz Suv")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/10"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Gazsiz Suv 1 l narxi--3 000 so'm \n"
#                          )
#
# @dp.message_handler(text="Still water")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/10"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Gazsiz Suv 1 l narxi--3 000 so'm \n"
#                          )
#
# @dp.message_handler(text="Gazli Suv")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/11"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Gazli Suv 1 l narxi--3 000 so'm \n"
#                          )
#
#
# @dp.message_handler(text="Carbonated water")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/11"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Carbonated water 1 l narxi--3 000 so'm \n"
#                          )
#
# @dp.message_handler(text="Pepsi")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/12"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Pepsi 1 l narxi--10 000 so'm \n"
#                          )
#
#
# @dp.message_handler(text="Fanta")
# async def bot_echo(message: types.Message):
#     rasm_manzili = "https://t.me/meningkanalim1898/13"
#     user_id = message.from_user.id
#     await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Fanta 1 l narxi--10 000 so'm \n"
#                          )
