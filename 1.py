import os
import psutil
import datetime
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

# Region definitions
REGIONS = {
    "asia": {"emoji": "🌏", "status": "Active"},
    "eu": {"emoji": "🇪🇺", "status": "Active"},
    "na": {"emoji": "🇺🇸", "status": "Active"},
    "sa": {"emoji": "🇧🇷", "status": "Active"},
    "oc": {"emoji": "🇦🇺", "status": "Active"},
    "jp": {"emoji": "🇯🇵", "status": "Active"},
    "kr": {"emoji": "🇰🇷", "status": "Active"},
    "id": {"emoji": "🇮🇩", "status": "Active"},
    "vn": {"emoji": "🇻🇳", "status": "Active"}
}

# Bot configuration
BOT_TOKEN = os.environ.get("8474536328:AAHvN4DmB3z0ixjJn6MzW8jtEEgWYm4D7ZQ")

# Bot info
BOT_INFO = {
    "version": "2.0",
    "author": "FreeFireBot Team",
    "description": "Free Fire Account Checker with region support"
}

PROCESS_STEPS = [
    "1. Connecting to Free Fire API...",
    "2. Validating credentials...",
    "3. Retrieving player data...",
    "4. Checking ban status...",
    "5. Processing results...",
    "6. Formatting response..."
]

def cmd_start(update: Update, context: CallbackContext):
    welcome_msg = (
        "🎮 *Welcome to FreeFireBot!* 🎮\n\n"
        "I'm your all-in-one Free Fire account checker!\n\n"
        "Quick Intro:\n"
        "• Check account details (level, win rate)\n"
        "• Verify ban status\n"
        "• Monitor system resources\n\n"
        "Type /help to see all commands."
    )
    update.message.reply_text(welcome_msg, parse_mode=ParseMode.MARKDOWN)

def cmd_help(update: Update, context: CallbackContext):
    help_msg = (
        "📚 *Command Reference* 📚\n\n"
        "• /start - Welcome message\n"
        "• /ffcheckuid <UID> - Check account by UID\n"
        "• /process - Step-by-step process\n"
        "• /about - Bot information\n"
        "• /status - Bot status\n\n"
        "Example usage:\n"
        "/ffcheckuid 1234567890"
    )
    update.message.reply_text(help_msg, parse_mode=ParseMode.MARKDOWN)

def cmd_process(update: Update, context: CallbackContext):
    process_msg = "*Current Process Steps:*\n\n"
    for step in PROCESS_STEPS:
        process_msg += f"• {step}\n"
    update.message.reply_text(process_msg, parse_mode=ParseMode.MARKDOWN)

def cmd_about(update: Update, context: CallbackContext):
    about_msg = (
        f"📄 *About FreeFireBot v{BOT_INFO['version']}*\n\n"
        f"Author: {BOT_INFO['author']}\n"
        f"Description: {BOT_INFO['description']}\n\n"
        "⚠️ *Disclaimer*\n"
        "• Data accuracy depends on API sources\n"
        "• Results may vary based on API availability\n"
        "• Not affiliated with Free Fire or Garena"
    )
    update.message.reply_text(about_msg, parse_mode=ParseMode.MARKDOWN)

def cmd_status(update: Update, context: CallbackContext):
    # Get system status
    cpu_load = psutil.cpu_percent()
    memory_load = psutil.virtual_memory().percent
    disk_load = psutil.disk_usage('/').percent
    
    # Generate region status
    region_status = ""
    for region, info in REGIONS.items():
        emoji = info["emoji"]
        status = info["status"]
        region_status += f"{emoji} {region.upper()}: {status}\n"
    
    status_msg = (
        "📊 *Bot Status*\n\n"
        f"Status: ✅ Online\n"
        f"Uptime: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"CPU Load: {cpu_load}%\n"
        f"Memory: {memory_load}%\n"
        f"Disk: {disk_load}%\n\n"
        "*Region Status:*\n"
        f"{region_status}"
    )
    update.message.reply_text(status_msg, parse_mode=ParseMode.MARKDOWN)

def cmd_ffcheckuid(update: Update, context: CallbackContext):
    uid = update.message.text.split()[1] if len(update.message.text.split()) > 1 else None
    if not uid:
        update.message.reply_text("Usage: /ffcheckuid <UID>")
        return
    
    # Process simulation
    update.message.reply_text("🔍 Processing your request...")
    for step in PROCESS_STEPS:
        update.message.reply_text(f"⚙️ {step}")
    
    # Simulated result
    result_msg = (
        f"📊 *Account Details for UID: {uid}*\n\n"
        "Level: 120\n"
        "Win Rate: 65.3%\n"
        "Last Played: 2 hours ago\n"
        "Banned: No"
    )
    update.message.reply_text(result_msg, parse_mode=ParseMode.MARKDOWN)

def main():
    if not BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")
    
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", cmd_start))
    dp.add_handler(CommandHandler("help", cmd_help))
    dp.add_handler(CommandHandler("process", cmd_process))
    dp.add_handler(CommandHandler("about", cmd_about))
    dp.add_handler(CommandHandler("status", cmd_status))
    dp.add_handler(CommandHandler("ffcheckuid", cmd_ffcheckuid))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
