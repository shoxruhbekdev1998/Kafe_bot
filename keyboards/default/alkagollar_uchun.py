from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

alkagollar_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Aroq"),
            KeyboardButton(text="Vino")

        ],
        [
            KeyboardButton(text="Piva"),
            KeyboardButton(text="Kanyak")

        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)