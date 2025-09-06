import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🔑 কীওয়ার্ড-ভিত্তিক রিপ্লাই ম্যাপ
KEYWORD_REPLIES = {
    "loan": "💰 আপনি লোন নিতে চান? বিস্তারিত জানাতে ইনবক্স করুন।",
    "hello": "👋 হ্যালো! কেমন আছেন?",
    "hi": "🙂 হাই! কিভাবে সাহায্য করতে পারি?",
    "help": "🆘 হেল্প দরকার? অ্যাডমিনকে ট্যাগ করুন।",
    "contact": "📞 আমাদের কন্টাক্ট: +8801XXXXXXXXX",
}

DEFAULT_REPLY = "✅ আপনার মেসেজ পেয়েছি, শিগগিরই রিপ্লাই করা হবে।"

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return

    text = update.message.text.lower() if update.message.text else ""

    # কোন কীওয়ার্ড মিলে সেটি রিপ্লাই দেবে
    reply = None
    for keyword, response in KEYWORD_REPLIES.items():
        if keyword in text:
            reply = response
            break

    if not reply:
        reply = DEFAULT_REPLY

    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # শুধু টেক্সট মেসেজ ধরবে
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

    app.run_polling()

if __name__ == "__main__":
    main()
