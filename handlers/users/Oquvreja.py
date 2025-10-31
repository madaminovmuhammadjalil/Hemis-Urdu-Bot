from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from aiogram.types import InputFile
from loader import dp,db
from states.statess import startt
from data.GetDateFromDB import *
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(Text(equals='a'),state=startt.bolimlar)
async def oquvreja(call: types.CallbackQuery):
    try:
        # await call.message.delete()

        obj1 = bolimlar()
        data = db.select_user(call.from_user.id)
        parol = data[3]
        login = data[2]

        await call.message.answer_photo(InputFile(path_or_bytesio=f"data/{obj1.Oquvreja(login, parol)}"))

    except:
        await call.message.answer("O'quv reja ishlamayapdi")
