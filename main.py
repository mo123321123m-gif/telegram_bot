import os, requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت شغال 24 ساعة - دز رابط TikTok / Insta / YouTube")

async def dl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    if "http" not in txt:
        return
    await update.message.reply_text("⏳ جاري التحميل...")
    try:
        r = requests.get(f"https://www.tikwm.com/api/?url={txt}", timeout=30).json()
        vid = r.get("data", {}).get("play")
        if vid:
            await update.message.reply_video(vid, caption="✅ بدون علامة")
        else:
            await update.message.reply_text("❌ الرابط مو عام او مو مدعوم")
    except Exception as e:
