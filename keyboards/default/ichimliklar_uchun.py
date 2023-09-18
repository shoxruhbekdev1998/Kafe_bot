from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
ichimliklar_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Salqin ichimliklar"),
            KeyboardButton(text="Alkagollar")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)