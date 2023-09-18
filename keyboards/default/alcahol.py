from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

alcahols_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Vodka"),
            KeyboardButton(text="Wine")

        ],
        [
            KeyboardButton(text="Beer"),
            KeyboardButton(text="Cognac")

        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)