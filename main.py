from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup
)
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    CallbackQueryHandler, ContextTypes
)
import asyncio

TOKEN = "توکن خودت"
CHANNEL_USERNAME = "Charm_World"

JOIN_MESSAGE = """*سلام 👋*

*من ربات خرید و فروش محصولات دنیای چرم هستم 🤗*

*برای استفاده از من و ادامه خرید، داخل کانال فروشگاهمون عضو شو 😅*

*با استفاده از دکمه زیر داخل کانال جوین شو و بعد روی دکمه "جوین شدم ✅️" کلیک کن*"""

RULES_MESSAGE = """*🔖 قوانین فروشگاه و ربات به این صورت می‌باشد 🔖*

*1 : از ارسال رسید فیک خودداری کنید.*
در صورت ارسال رسید فیک به جای پرداخت واقعی، ربات شما را مسدود می‌کند 🚫

*2 : حتما قبل از تایید آدرس، از درستی مکان وارد شده اطمینان حاصل کنید.*
در صورت وارد کردن اطلاعات غلط، ما هیچ مسئولیتی در قبال نرسیدن محصول نداریم 📜

*3 : در انتخاب محصول خود دقت کنید زیرا پس از پرداخت، محصول ثبت شده و لغو نمی‌شود ⛔️*

*کلیک روی دکمه زیر به معنی تایید قوانین ما است 👇*"""

CATEGORIES_MESSAGE = """*🛒 محصول مورد نظر شما از کدام دسته بندی است ❓️*

*از لیست زیر نوع محصول خود را انتخاب کنید 👇📜*"""

TYPE_MESSAGE_TEMPLATE = """*کدوم نوع از {} رو می‌خواین ❓️*

*از دکمه‌های زیر استفاده کنید 👇*"""

def join_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_USERNAME}")],
        [InlineKeyboardButton("✅ جوین شدم", callback_data="check_join")]
    ])

def rules_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("☑️ قوانین را خوانده‌ام و قبول دارم ☑️", callback_data="accept_rules")]
    ])

def category_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👞 کفش 👠", callback_data="cat_shoes"),
         InlineKeyboardButton("💼 کیف 👜", callback_data="cat_bag")],
        [InlineKeyboardButton("🧤 اکسسوری 🪮", callback_data="cat_accessory"),
         InlineKeyboardButton("🥋 کمربند 🧣", callback_data="cat_belt")]
    ])

def type_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👨 مردانه 👨", callback_data="gender_male"),
         InlineKeyboardButton("👩 زنانه 👩", callback_data="gender_female")]
    ])

async def is_user_joined(user_id, context):
    try:
        member = await context.bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if await is_user_joined(user_id, context):
        if context.user_data.get("rules_accepted"):
            await update.message.reply_text(
                CATEGORIES_MESSAGE,
                reply_markup=category_keyboard(),
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await update.message.reply_text(
                RULES_MESSAGE,
                reply_markup=rules_keyboard(),
                parse_mode=ParseMode.MARKDOWN
            )
    else:
        await update.message.reply_text(
            JOIN_MESSAGE,
            reply_markup=join_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "check_join":
        if await is_user_joined(user_id, context):
            await query.message.delete()
            await query.message.chat.send_message(
                RULES_MESSAGE,
                reply_markup=rules_keyboard(),
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await query.answer("❌ هنوز عضو نشدی!", show_alert=True)

    elif query.data == "accept_rules":
