import pytz
import telegram
import asyncio
import schedule
import datetime

token = "6721469751:AAFB8RMFOy3NXaTjTVDdJ_sy8S9i8hPEO58"
public_chat_name = "@hxrintest"
bot = telegram.Bot(token=token)

async def send_message():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    # 오후 11시부터 아침 6시까지 방해 금지 모드
    if now.hour >= 23 or now.hour <= 6:
        return
    
    message_text = "current time = " + str(now)
    
    await bot.sendMessage(chat_id=public_chat_name, text=message_text)

def job():
    asyncio.create_task(send_message())

async def main():
    # 30분마다 메세지 출력
    schedule.every(30).minutes.do(job)
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
