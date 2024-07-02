from aiogram import Bot
import asyncio 

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

bot = Bot('7043803455:AAELI3zwsJdp6MlGor3VL4ONP_jfwfY9fmg')
async def send_message(text: str, group_id: str):
    await bot.send_message(group_id, text)
    
async def main(text, group_id):
    t1 = asyncio.create_task(send_message(text, group_id))
    await t1
    



