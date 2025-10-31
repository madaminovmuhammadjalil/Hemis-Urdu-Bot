from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

xabarlar=InlineKeyboardMarkup(
    inline_keyboard=[
        [
             InlineKeyboardButton(text="📖 O'quv reja",callback_data='a'),
             InlineKeyboardButton(text="🗒 Dars jadvali",callback_data='b'),
        ],
        [
             InlineKeyboardButton(text="⏱ Davomat",callback_data='e'),
             InlineKeyboardButton(text="📝 O'zlashtirish",callback_data='f'),
        ],
        [
             InlineKeyboardButton(text="📘 Buyruqlar",callback_data='n'),
             InlineKeyboardButton(text="📃 Reyting daftarcha",callback_data='h'),
        ],
        [
             InlineKeyboardButton(text="📄 Talaba hujjati",callback_data='q'),
             InlineKeyboardButton(text="📄 Ma'lumotnomalar",callback_data='p'),
        ],
        [
            InlineKeyboardButton(text="🥇 Nazorat jadvali", callback_data='c'),
            InlineKeyboardButton(text="⬅ Tizimdan chiqish uchun /start ni bosing", callback_data='15'),
        ],
    ],
)


start=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👉 Ro'yhatdan o'tish",callback_data="1"),
        ],
    ],
    resize_keyboard=True
)

hafta=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hafta",callback_data="y"),
        ],
    ],
    resize_keyboard=True
)
nazoratjadvalii=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oraliq nazorat",callback_data='z'),
            InlineKeyboardButton(text="Yakuniy nazorat",callback_data='sh'),
        ],
    ],
    resize_keyboard=True
)
menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Asosiy menu',callback_data='as'),
        ],
    ],
    resize_keyboard=True
)

