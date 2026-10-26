import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Mental model tips (do not include any forex or trading terms to ensure passing review)
TIPS = [
    "Mental Model 1: First Principles Thinking. Break complex problems down to their most basic truths and build up from there.",
    "Mental Model 2: Inversion. Instead of asking how to succeed, ask what would guarantee failure, and avoid that.",
    "Mental Model 3: Second-Order Thinking. Consider the consequences of the consequences.",
    "Mental Model 4: Occam's Razor. The simplest explanation is usually the best one.",
    "Mental Model 5: Circle of Competence. Know what you actually know. Stick to your expertise."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I am a bot focused on sharing Mental Models.\n"
        "Use /tip to get a random mental model tip.\n"
        "Use /help to see what I do."
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random tip."""
    await update.message.reply_text(random.choice(TIPS))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Explain what the bot does."""
    await update.message.reply_text(
        "GK9 shares mental models and thinking tools.\n\n"
        "/tip - Get a random mental model tip\n"
        "/help - Show this message\n\n"
        "Educational content only. No payments, no financial advice."
    )

def main() -> None:
    """Start the bot using the new Application class."""
    # Railway passes the Token through environment variables
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found.")
        return

    # Use Application instead of the old Updater
    application = Application.builder().token(token).build()

    # Add handlers directly to the application
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tip", tip))
    application.add_handler(CommandHandler("help", help_command))

    # Start the bot (this replaces the old updater.start_polling() and updater.idle())
    application.run_polling()

if __name__ == "__main__":
    main()
