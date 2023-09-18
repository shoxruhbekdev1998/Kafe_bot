from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

salqin_ichimliklar_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gazsiz Suv"),
            KeyboardButton(text="Gazli Suv")

        ],
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Fanta")

        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)