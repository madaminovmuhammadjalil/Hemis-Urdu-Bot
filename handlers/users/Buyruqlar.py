from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from loader import dp, db
from keyboards.inline.inlinekeyboard import menu
import requests, json
from data.GetDateFromDB import *
from states.statess import startt
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(Text(equals='n'), state=startt.bolimlar)
async def buyruqlar(call: types.CallbackQuery, state: FSMContext):
    # await call.message.delete()

    obj1 = bolimlar()
    data = db.select_user(call.from_user.id)
    parol = data[3]
    login = data[2]

    await call.message.answer(text=f'Buyruq raqami          Buyruq sanasi         Nomi       Buyruq turi        \n'
                                   f'{obj1.Buyruqlar(login, parol)}', reply_markup=menu)
