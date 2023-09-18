from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
drinkss_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cool drinks"),
            KeyboardButton(text="Alcohols")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)