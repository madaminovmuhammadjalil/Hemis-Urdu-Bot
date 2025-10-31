from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from loader import dp,db
import json,requests
from states.statess import startt
from data.GetDateFromDB import *
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(Text(equals='p'),state=startt.bolimlar)
async def malumotnomalar(call: types.CallbackQuery,state: FSMContext):

    obj1 = bolimlar()
    data = db.select_user(call.from_user.id)
    parol = data[3]
    login = data[2]

    await call.message.answer(text=f"Hujjat raqami          O'quv yili        Kurs       Semester\n"
                                   f'{(obj1.Malumotlar(login,parol))}')


