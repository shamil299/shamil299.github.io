import my_env
import asyncio
import random
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Красный экран", callback_data='red')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Начало теста реакции.', reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat.id
    message_id = query.message.message_id

    if data == 'red':
        # Изменяем кнопку на зеленую через случайное время
        delay = random.uniform(1, 5)
        await asyncio.sleep(delay)
        new_keyboard = [[InlineKeyboardButton("Зеленый экран", callback_data='green')]]
        await context.bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=InlineKeyboardMarkup(new_keyboard))

    elif data == 'green':
        # Измеряем время реакции
        start_time = float(query.message.text.split(':')[1].strip())
        elapsed_time = round(time.time() - start_time, 3)
        await context.bot.answer_callback_query(callback_query_id=query.id, text=f"Твоя реакция: {elapsed_time:.3f} сек.", show_alert=True)
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)

async def play_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем первоначальное сообщение с красной кнопкой
    await start(update, context)

def main():
    app = ApplicationBuilder().token(my_env.token_bot).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))

    print("Запускаю бот...")
    app.run_polling()

if __name__ == '__main__':
    main()