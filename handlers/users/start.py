import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import *

from data.config import ADMINS
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    # await message.answer(text=f"Asssalomu alaykum {message.from_user.full_name}""\n"
    #                           "🇺🇿Botdan foydalanish uchun o'zingizga qulay tilni tanlang!""\n"
    #                           "🇬🇧Choose your preferred language to use the bot!""\n"
    #                           "🇷🇺Выберите предпочитаемый язык для использования бота!", reply_markup=start)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
