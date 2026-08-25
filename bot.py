import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 **OSINT Bot (Termux Edition)**\n\n"
        "Commands:\n"
        "• `/ip <IP_ADDRESS>` - IP info trace karein"
    )
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

# IP Lookup Feature
async def ip_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: `/ip 8.8.8.8`", parse_mode='Markdown')
        return

    ip = context.args[0]
    await update.message.reply_text(f"🔍 Searching IP: {ip}...")

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response.get("status") == "fail":
            await update.message.reply_text("❌ Invalid IP Address!")
            return

        result = (
            f"🌐 **IP OSINT Result:**\n"
            f"• **IP:** {response.get('query')}\n"
            f"• **Country:** {response.get('country')}\n"
            f"• **City:** {response.get('city')}\n"
            f"• **ISP:** {response.get('isp')}\n"
            f"• **Org:** {response.get('org')}"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception:
        await update.message.reply_text("⚠️ API Error!")

# Main function
if __name__ == '__main__':
    # APNA TELEGRAM BOT TOKEN YAHAN DALEIN
    TOKEN = "8190169571:AAHF3gk4lUzjnlPOHyw08gNgfP66xohUWVY"

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ip", ip_lookup))

    print("🚀 Termux Bot running...")
    app.run_polling()

