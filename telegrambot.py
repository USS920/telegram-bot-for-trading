from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler 
#pip install python-telegram-bot -U --pre
import json
from datetime import datetime as dt, timedelta
import sys
import pandas as pd
import time
import os

async def Start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""\
        Actions:
        \n/CloseTrade: Select the trades from list to close.
        \n/FetchMTM: Fetch strategy MTM.
        """)
    #create async def of FetchMTM in the same way of CloseTrade

async def CloseTrade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Some Text like /CloseTrade1\n\n/CloseTrade2")
    #CloseTrade1 and 2 are below

async def CloseTrade1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Call the python code here which closes the trade
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Trad 1 closed Successfully.\n\n/start")

async def CloseTrade2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Call the python code here which closes the trade
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Trad 1 closed Successfully.\n\n/start")

if __name__ == '__main__':
    application = ApplicationBuilder().token('5815892603:AAH8wLQ48y8qasdasdfYUYNQPwCnrFNfFp3E').build() #Bot Token
    start_handler = CommandHandler('Start', Start)
    application.add_handler(start_handler)
    start_handler = CommandHandler('CloseTrade', CloseTrade)
    application.add_handler(start_handler)
    start_handler = CommandHandler('CloseTrade1', CloseTrade1)
    application.add_handler(start_handler)
    start_handler = CommandHandler('CloseTrade2', CloseTrade2)
    application.add_handler(start_handler)
    application.run_polling()
