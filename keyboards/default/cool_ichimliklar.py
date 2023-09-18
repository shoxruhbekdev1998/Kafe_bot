from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sovuq_ichimliklar_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Still water"),
            KeyboardButton(text="Carbonated water")

        ],
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Fanta")

        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)