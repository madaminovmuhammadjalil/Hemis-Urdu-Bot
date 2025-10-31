import sqlite3

from aiogram.dispatcher.filters.builtin import Text,CommandStart

from data.config import ADMINS
from keyboards.inline.inlinekeyboard import xabarlar,start
from aiogram import types
from loader import dp, db, bot
from states.statess import startt
from aiogram.dispatcher.filters.state import State,StatesGroup
from data.GetDateFromDB import *





@dp.message_handler(CommandStart)
async def bot_start(message: types.Message):
    channels_format=str()
    # for channel in CHANNELS:
    #     chat = await bot.get_chat(channel)
    #     tashrif_linki= await chat.export_invite_link()
    #     channels_format=f"<a href '{tashrif_linki}'>{chat.title}</a>\n"

    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                   name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    # Adminga xabar beramiz
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\n"
                         f"Urganch davlat universitetining HEMIS Urdu rasmiy botiga xush kelibsiz\n"
                         f'{channels_format}'
                         , reply_markup=start
                         , disable_notification=True)

    await State.set(startt.til)

@dp.callback_query_handler(Text(equals='1'),state=startt.til)
async def bot_start(call: types.CallbackQuery):
    await call.message.answer("Hemis tizimidagi login va parolingizni mos ravishda shu ko'rinishda kiriting !.\n"
                         "Masalan \n xxxxxxxxx  yyyyyyyyy ")
    await startt.next()


@dp.message_handler(state=startt.logpar)
async def login(message: types.Message):
    try:
        obj1=bolimlar()

        text=message.text.split()
        login=text[0]
        parol=text[1]
        db.update_user_data(login,parol,message.from_user.id)

        url = "https://student.urdu.uz/rest/v1/auth/login"

        payload = json.dumps({
            "login": f"{login}",
            "password": f"{parol}"
        })
        headers = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ2MVwvYXV0aFwvbG9naW4iLCJhdWQiOiJ2MVwvYXV0aFwvbG9naW4iLCJleHAiOjE2NjkzNTY5ODIsImp0aSI6IjM0MTIwMTEwOTYwNSIsInN1YiI6IjM1NTg4In0.d91veAwleMVeehIzzSG_KxG1vNPLVYe7aeq_ozoWHJc',
            'Content-Type': 'application/json'

        }

        response = requests.request("POST", url, headers=headers, data=payload)

        dtoken = response.json()['data']['token']


        '''----------------------------------------------------------------'''

        url = "https://student.urdu.uz/rest/v1/account/me"

        payload = {}
        headers = {
            'Authorization': f'Bearer {dtoken}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        javob=response.json()['data']['first_name']
        javob1=response.json()['data']['second_name']
        javob2=response.json()['data']['image']

        await message.answer(f"✅ Tizimga muvaffaqiyatli kirdingiz!\n"
                             f"f'{javob2}\n "
                             f"Foydalanuvchi {javob},{javob1}",reply_markup=xabarlar)

        await startt.next()


    except :
        await message.answer('🔄 Login yoki parolingiz xato tekshirib qayta kiriting !  ')





