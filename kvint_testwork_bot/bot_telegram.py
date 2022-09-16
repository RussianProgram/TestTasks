from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from base_logic import cashier

import re
import logging
import os


#set-up the bot
API_TOKEN = os.environ.get('BOT_TOKEN')

#set-up logging
logging.basicConfig(level=logging.INFO)

#initialize bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def taking_order_handler(message: types.Message):
    cashier.start_taking_order()
    await message.answer('Какую вы хотите пиццу? Большую или маленькую')


@dp.message_handler()
async def order_handler(message: types.Message):
    # Какую вы хотите пиццу!!
    if re.match(r'большую',str(message.text).lower()):
        cashier.big()
        await message.answer(cashier.message)
    elif re.match(r'маленькую',str(message.text).lower()):
        cashier.small()
        await message.answer(cashier.message)

    # Оплата Наличкой или Банковской картой(картой)?
    if re.match(r'наличкой', str(message.text).lower()):
        cashier.cash()
        await message.answer(cashier.message)

    elif re.match(r'банковской картой|картой', str(message.text).lower()):
        cashier.with_card()
        await message.answer(cashier.message)

    # Вы хотите N пиццу, оплата - M?
    if re.match(r'да', str(message.text).lower()):
        cashier.yes()
        await message.answer(f'Спасибо за заказ! {cashier.message}')

    elif re.match(r'нет', str(message.text).lower()):
        cashier.no()
        await message.answer(f'Заказ отменен! {cashier.message}')



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)