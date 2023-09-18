from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
taomlar_buttun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 - Taomlar "),
            KeyboardButton(text="2 - Taomlar")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]

    ],
    resize_keyboard=True

)