import telegram
import asyncio

token = "6721469751:AAFB8RMFOy3NXaTjTVDdJ_sy8S9i8hPEO58"
bot = telegram.Bot(token = token)
## chat_id = "6757409161"
text = 'test'
public_chat_name = '@hxrintest'
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(bot.sendMessage(chat_id = public_chat_name, text = text))
