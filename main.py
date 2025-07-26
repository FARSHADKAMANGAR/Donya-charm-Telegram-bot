from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8479592:AAGCDvqDSXvtYZSXz7UnRHrWYn0JE"

MESSAGE_TEXT = """*ربات در حال بروزرسانی است و در دسترس نیست . . . 🌜*
*منتظر بمانید یا اگر مشکلی دارید ، با پشتیبان ربات در ارتباط باشید ♻️*

*iD : @DONYA_CHARM_SUPPORT*"""

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            MESSAGE_TEXT,
            parse_mode=ParseMode.MARKDOWN
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.ALL, reply_message))

    print("ربات راه‌اندازی شد و منتظر پیام‌هاست...")
    app.run_polling()
