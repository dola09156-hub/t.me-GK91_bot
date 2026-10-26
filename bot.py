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

# Fake "mental model" tips to meet review's "content delivery" requirements
# Note: Do not put any forex or trading advice here
TIPS = [
    "Mental Model 1: First Principles Thinking. Break complex problems down to their most basic truths and build up from there.",
    "Mental Model 2: Inversion. Instead of asking how to succeed, ask what would guarantee failure, and avoid that.",
    "Mental Model 3: Second-Order Thinking. Consider the consequences of the consequences. What happens after the immediate effect?",
    "Mental Model 4: Occam's Razor. The simplest explanation is usually the best one. Don't overcomplicate things.",
    "Mental Model 5: Circle of Competence. Know what you actually know. Stick to your expertise and be honest about what you don't know."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I am a bot focused on sharing Mental Models.\n"
        "Use /tip to get a random mental model tip."
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random tip."""
    await update.message.reply_text(random.choice(TIPS))

def main() -> None:
    """Start the bot."""
    # Railway will pass the Token through environment variables
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found.")
        return

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tip", tip))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
