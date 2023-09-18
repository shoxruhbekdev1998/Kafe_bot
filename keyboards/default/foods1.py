from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
foods1_buttun =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Soup"),
            KeyboardButton(text="Pitcher Soup")

        ],
        [
            KeyboardButton(text="Mastava uzbek"),
            KeyboardButton(text="Suyuq lag'mon uzbek")

        ],
        [
          KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)