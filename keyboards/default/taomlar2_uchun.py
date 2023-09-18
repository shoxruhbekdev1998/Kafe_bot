from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

taomlar2_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Shashlik qiyma")

        ],
        [
            KeyboardButton(text="Tovuq shashlik"),
            KeyboardButton(text="Somsa")

        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)