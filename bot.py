import logging

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

logging.basicConfig(level= logging.INFO,filename="py_log.log",filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

bot = Bot(token= TOKEN)
dp = Dispatcher(bot)

#admin_id = 1293493

russian = ['А','Б', 'В', 'Г', 'Д', 'Е','Ё','Ж','З', 'И','Й','К', 'Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ъ','Ь','Э','Ю','Я']
english = ['A', 'B', 'V', 'G', 'D', 'E', 'E', 'ZH', 'Z', 'I', 'I', 'K' ,'L','M','N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'KH', 'TS', 'CH', 'SH','SHCH', 'Y', 'IE', '', 'E' ,'IU', 'IA']
dictionary = dict(zip(russian,english))

def min (russian):
    return list(map(lambda x: x.lower(), russian))

smal_russian =  min (russian) 
#smal_english =  min (english)
smal_dictionary = dict(zip(smal_russian,english))
dictionary.update(smal_dictionary)
dictionary[' '] = ' '





def translete(word):
    new_word = ''
    for i in  word:
        new_word += dictionary.get(i)
    return new_word



@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello, {user_name}!\n'
    logging.info(f'{user_name=} {user_id=} sent message : {message.text}')
    await message.reply(text)

@dp.message_handler()   
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name=} {user_id=} sent message : {text}')
    await bot.send_message(user_id,translete(text))
    #await bot.send_message(admin_id,text)

if __name__ == '__main__':
    executor.start_polling(dp)
