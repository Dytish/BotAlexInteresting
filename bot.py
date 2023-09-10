from internal import handlers
from internal.dispatcher import dp, bot 
import asyncio

# Запуск процесса поллинга новых апдейтов
async def main():

    # dp.include_router(handlers.handlerAP.router)
    # dp.include_router(handlers.questionnaire.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    # executor.start_polling(dp) 
    asyncio.run(main())
