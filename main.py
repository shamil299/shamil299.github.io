import my_env
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import json

async def process_game_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.effective_message.web_app_data.data
    parsed_data = json.loads(data)
    reaction_time_ms = parsed_data['reaction_time']
    await update.message.reply_text(f"Ваша реакция составила {reaction_time_ms} мс.")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[{
        'text': 'Играть в проверку скорости реакции',
        'web_app': {'url': 'https://shamil299.github.io'}
    }]]
    await update.message.reply_text("Нажмите кнопку ниже, чтобы сыграть!",
                                    reply_markup={'inline_keyboard': keyboard})

if __name__ == "__main__":
    application = ApplicationBuilder().token(my_env.token_bot).build()

    # Добавляем обработчики
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, process_game_result))
    application.add_handler(CommandHandler("start", start_command))

    application.run_polling()