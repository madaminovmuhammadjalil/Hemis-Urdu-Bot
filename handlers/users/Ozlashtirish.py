from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from aiogram.types import InputFile
from loader import dp,db
from data.GetDateFromDB import *
from states.statess import startt




@dp.callback_query_handler(Text(equals='f'),state=startt.bolimlar)
async def ozlashtorish(call: types.CallbackQuery):
    try:
        obj1 = bolimlar()
        data = db.select_user(call.from_user.id)
        parol = data[3]
        login = data[2]

        await call.message.answer_photo(InputFile(path_or_bytesio=f"data/{obj1.Ozlashtirish(login, parol)}"))
    except:
        await call.message.answer("O'zlashtirish bo'limi ishlamayabdi")



