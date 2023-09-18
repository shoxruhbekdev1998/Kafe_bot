from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

foods2_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pilaf"),
            KeyboardButton(text="Shashlik qiyma uzbek")

        ],
        [
            KeyboardButton(text="Tovuq shashlik uzbek"),
            KeyboardButton(text="Somsa uzbek")

        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)