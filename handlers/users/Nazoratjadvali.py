from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from aiogram.types import InputFile
from loader import dp, db
import requests, json, datetime
from keyboards.inline.inlinekeyboard import nazoratjadvalii
from states.statess import startt
from data.GetDateFromDB import *
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(Text(equals='c'), state=startt.bolimlar)
async def nazorat(call: types.CallbackQuery):
    await call.message.answer(text="Kerakli bo'limni tanlang", reply_markup=nazoratjadvalii)
    await startt.next()


@dp.callback_query_handler(Text(equals='z'), state=startt.kichikbolim)
async def oraliqnazorat(call: types.CallbackQuery, state: FSMContext):
    # await call.message.delete()

    obj1 = bolimlar()
    data = db.select_user(call.from_user.id)
    parol = data[3]
    login = data[2]

    await call.message.answer(text=f'{obj1.NazoratjadvaliO(login, parol)}')
    photo_file = InputFile(path_or_bytesio="featured-image-creation-with-python.png")
    await call.message.reply_photo(photo_file)


"-------------------------------------------------------------------------------------"


@dp.callback_query_handler(Text(equals='sh'), state=startt.kichikbolim)
async def yauniynazorat(call: types.CallbackQuery, state: FSMContext):
    obj1 = bolimlar()
    data = db.select_user(call.from_user.id)
    parol = data[3]
    login = data[2]

    await call.message.answer(text=f'{obj1.NazoratjadvaliY(login, parol)}')
    photo_file = InputFile(path_or_bytesio="featured-image-creation-with-python.png")
    await call.message.reply_photo(photo_file)
