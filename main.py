import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from memory import init_db, store_message, get_history, clear_history

load_dotenv()
init_db()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I'm Zara AI powered by zencripts 🤖\nAsk me anything!")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    user_id = update.message.from_user.id

    store_message(user_id, f"User: {user_msg}")
    history = get_history(user_id)
    prompt = "\n".join(history[-10:] + [f"User: {user_msg}"])

    try:
        response = model.generate_content(prompt)
        bot_reply = response.text.strip()

        store_message(user_id, f"Zara: {bot_reply}")
        await update.message.reply_text(bot_reply)
    except Exception as e:
        await update.message.reply_text(f"⚠️ zencripts Error: {e}")

async def forget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    clear_history(user_id)
    await update.message.reply_text("🧠 Memory cleared!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("forget", forget))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()
