from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
taomlar1_buttun =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sho'rva"),
            KeyboardButton(text="Ko'za Sho'rva")

        ],
        [
            KeyboardButton(text="Mastava"),
            KeyboardButton(text="Suyuq lag'mon")

        ],
        [
          KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)