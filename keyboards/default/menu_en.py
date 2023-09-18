from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu_buttun_en = ReplyKeyboardMarkup(
    keyboard =[
        [
        KeyboardButton(text="Foods"),
        KeyboardButton(text="Drinks")
        ],
        [
            KeyboardButton(text="Contact",request_contact=True),
            KeyboardButton(text="Location",request_location=True)
        ]
    ],
    resize_keyboard=True
)