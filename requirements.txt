import os
import logging
from telegram import Update, ChatAction
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()
    chat_type = update.message.chat.type

    # در گروه فقط به پیام‌هایی که با بگاعیل شروع شدن جواب بده
    if chat_type in ["group", "supergroup"]:
        if not message_text.startswith(("بگاعیل", "begail")):
            return

    # ارسال جلوه تایپ
    await update.message.chat.send_action(action=ChatAction.TYPING)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="سلام! من بگاعیل هستم، ربات برنامه‌نویس شما 👨‍💻✨")

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    application.run_polling()
