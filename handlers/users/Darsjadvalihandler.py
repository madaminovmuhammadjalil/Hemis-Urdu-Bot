from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from aiogram.types import InputFile
from loader import dp,db
from keyboards.inline.inlinekeyboard import hafta,menu
from aiogram.dispatcher import FSMContext
from data.GetDateFromDB import *
from states.statess import startt


@dp.callback_query_handler(Text(equals='b'),state=startt.bolimlar)
async def darsjadvalikun(call: types.CallbackQuery):
    try:
        obj1 = bolimlar()
        data = db.select_user(call.from_user.id)
        parol = data[3]
        login = data[2]

        await call.message.answer_photo(InputFile(path_or_bytesio=f"data/{obj1.Darsjadvali(login, parol)}"),
                                        reply_markup=hafta)
    except:
        await call.message.answer("Dars jadvali bo'limi ishlamayapdi")

@dp.callback_query_handler(Text(equals='y'),state=startt.bolimlar)
async def darsjadvalihafta(call: types.CallbackQuery):
    try:
        obj1 = bolimlar()

        data = db.select_user(call.from_user.id)
        parol = data[3]
        login = data[2]

        await call.message.answer_photo(InputFile(path_or_bytesio=f"data/{obj1.Darsjadvali1(login, parol)}"))
    except:
        await call.message.answer("Dars jadvali bo'limi ishlamayapdi")
