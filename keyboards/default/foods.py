from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
foods_uchun= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 - Food "),
            KeyboardButton(text="2 - Food ")
        ],
        [
            KeyboardButton(text="back")
        ]

    ],
    resize_keyboard=True

)