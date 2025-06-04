from telegram.ext import Application, MessageHandler, filters
from telegram import InputFile
import subprocess
import os

TOKEN = "8053122524:AAHaARpDd2ehY10CdvXlGTamtbPjpNDaB3E"  # Replace this with your real Bot Token

async def handle_message(update, context):
    url = update.message.text.strip()
    await update.message.reply_text("Downloading video...")

    output_path = "downloaded_video.mp4"

    try:
        subprocess.run(["yt-dlp", "-f", "best", "-o", output_path, url], check=True)
        with open(output_path, "rb") as f:
            await update.message.reply_video(video=InputFile(f))
        os.remove(output_path)
    except Exception as e:
        await update.message.reply_text(f"Failed to download. Error: {str(e)}")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running...")
    app.run_polling()
