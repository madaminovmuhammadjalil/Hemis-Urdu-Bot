from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from aiogram.types import InputFile
from loader import dp,db
from data.GetDateFromDB import *
from states.statess import startt
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(Text(equals='h'),state=startt.bolimlar)
async def reytingdaftarcha(call: types.CallbackQuery):
    try:
        obj1 = bolimlar()
        data = db.select_user(call.from_user.id)
        parol = data[3]
        login = data[2]

        await call.message.answer_photo(InputFile(path_or_bytesio=f"data/{obj1.Reytingdaftarcha(login, parol)}"))
    except:
        await call.message.answer("Reytingdaftarcha bo'limi ishlamayapdi")
