import logging
from aiogram import Bot, Dispatcher, executor, types

from tokenvar import API_TOKEN
import asyncio

question_delay_timee = 5

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    await message.reply("Hi!\nI'm EchoBot!\nsay something pencil")
    await message.answer(message.chat.id)

@dp.message_handler()
async def echo(message: types.Message):

    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # await message.answer(message.text)
    await message.reply(message.text)

async def sheduled_question():
    await bot.send_message(361195698, 'pisadaspi')
    print('question')

def scheduler_1_func(action_func, loop):
    asyncio.ensure_future(action_func(), loop=loop)
    loop.call_later(question_delay_timee, scheduler_1_func, action_func, loop)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.call_later(question_delay_timee, scheduler_1_func, sheduled_question, loop)

    executor.start_polling(dp, skip_updates=True)
