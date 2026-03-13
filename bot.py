import os
import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes
from telegram.constants import ChatMemberStatus

BOT_TOKEN = os.environ["BOT_TOKEN"]

async def track_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member

    # Only care about new members joining
    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    joined = (
        old_status in [ChatMemberStatus.LEFT, ChatMemberStatus.BANNED]
        and new_status == ChatMemberStatus.MEMBER
    )

    if not joined:
        return

    chat = result.chat
    bot: Bot = context.bot

    # Get current member count
    count = await bot.get_chat_member_count(chat.id)

    message = f"На каналі *{chat.title}* нарахували *{count}* геїв"
    await bot.send_message(
        chat_id=chat.id,
        text=message,
        parse_mode="Markdown"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatMemberHandler(track_member, ChatMemberHandler.CHAT_MEMBER))
    print("Bot is running...")
    app.run_polling(allowed_updates=["chat_member"])

if __name__ == "__main__":
    main()
