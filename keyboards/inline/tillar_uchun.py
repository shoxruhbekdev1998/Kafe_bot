from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
tillar_buttun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data="til1"),
            InlineKeyboardButton(text="Rus tili",callback_data="til3")
        ],
        [
            InlineKeyboardButton(text="Hamkorlar",url="https://t.me/yoshlaragentligi"),
            InlineKeyboardButton(text="Ulashish",switch_inline_query="Bu bot sizga istalgan taomingizni yetqizib beradi")
        ]
    ]
)