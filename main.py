import asyncio
from configparser import ConfigParser
from datetime import datetime
import json
import os
from pathlib import Path
import sys

from pyrogram import Client # pyrogram
from telegram import InputMediaVideo, InputMediaDocument, Update # python-telegram-bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler # python-telegram-bot

from localization import *


MAIN_DIRECTORY = Path(__file__).absolute().parent

USERS_JSON = MAIN_DIRECTORY / "users.json"
SUBSCRIBERS_JSON = MAIN_DIRECTORY / "subscribers.json"

cfg = ConfigParser(interpolation=None)
cfg.read(MAIN_DIRECTORY / "config.ini")

BOT_TOKEN = cfg.get("bot", "bot_token")
API_ID = cfg.get("pyrogram", "api_id")
API_HASH = cfg.get("pyrogram", "api_hash")

PALESTINEMOVIES_ID = int(cfg.get("bot", "palestinemovies_id"))
ADMIN_ID = cfg.get("bot", "admin_id")

application = ApplicationBuilder().token(BOT_TOKEN).build() # python-telegram-bot

# Define a dictionary to store album information
album = []
caption = ""

def load_json(file_path):
    if not file_path.is_file():
        with open(file_path, "w") as f:
            json.dump([], f)
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name or "n/a"
    username = update.message.from_user.username or "n/a"
    language_code = update.message.from_user.language_code
    date = int(datetime.now().timestamp())

    users = load_json(USERS_JSON)

    if user_id not in [user["user_id"] for user in users]:
        user_data = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "language_code": language_code,
            "date": date
        }
        users.append(user_data)
        save_json(USERS_JSON, users)

    await update.message.reply_text(get_localized_message(update, "START_COMMAND"), parse_mode="HTML")


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    async with Client(f"{MAIN_DIRECTORY}/palestinemoviesbot", api_id=API_ID, api_hash=API_HASH) as pyro:
        if not context.args:
            await update.message.reply_text(get_localized_message(update, "SEARCH_NO_QUERY"), parse_mode="HTML")
            return
        
        search_text = update.message.text.replace('/search ', '').replace('/search', '')
        search_text = search_text.replace('/cerca ', '').replace('/cerca', '')
        
        if len(search_text) < 4:
            await update.message.reply_text(get_localized_message(update, "SEARCH_SHORT_QUERY"), parse_mode="HTML")
            return
        
        if context.args:
            results = ""
            n = 0
            async for result in pyro.search_messages(chat_id=PALESTINEMOVIES_ID, query=search_text):
                if result.caption:
                    n += 1
                    title = result.caption.split('\n')[0].strip()
                    results += f"{n}. <a href=\"{result.link}\">{title}</a>\n\n"

                    if len(results) > 3950:
                        await update.message.reply_text(results, parse_mode="HTML", disable_web_page_preview=True)
                        results = ""
            
            user_id = update.message.from_user.id
            first_name = update.message.from_user.first_name
            last_name = update.message.from_user.last_name or "n/a"
            username = update.message.from_user.username or "n/a"
            language_code = update.message.from_user.language_code

            tracking_message = f"User ID: <code>{user_id}</code>\n" \
                                f"First name: {first_name}\n" \
                                f"Last name: {last_name}\n" \
                                f"Username: {username}\n" \
                                f"Language code: {language_code}\n" \
                                f"Search query: {search_text}\n\n"
            
            if results:
                await update.message.reply_text(results, parse_mode="HTML", disable_web_page_preview=True)
                # await context.bot.send_message(ADMIN_ID, f"{tracking_message}✅", parse_mode="HTML")
            else:
                await update.message.reply_text(get_localized_message(update, "SEARCH_NO_MEDIA_FOUND"), parse_mode="HTML", disable_web_page_preview=True)
                # await context.bot.send_message(ADMIN_ID, f"{tracking_message}❌", parse_mode="HTML")


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name or "n/a"
    username = update.message.from_user.username or "n/a"
    language_code = update.message.from_user.language_code
    date = int(datetime.now().timestamp())

    subscribers = load_json(SUBSCRIBERS_JSON)

    if user_id not in [subscriber["user_id"] for subscriber in subscribers]:
        subscriber_data = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "language_code": language_code,
            "date": date
        }
        subscribers.append(subscriber_data)
        save_json(SUBSCRIBERS_JSON, subscribers)
        await update.message.reply_text(get_localized_message(update, "SUBSCRIBE_SUCCESS"), parse_mode="HTML")
    else:
        await update.message.reply_text(get_localized_message(update, "SUBSCRIBE_ALREADY_SUBSCRIBED"), parse_mode="HTML")


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    subscribers = load_json(SUBSCRIBERS_JSON)

    if user_id in [subscriber["user_id"] for subscriber in subscribers]:
        subscribers = [subscriber for subscriber in subscribers if subscriber["user_id"] != user_id]
        save_json(SUBSCRIBERS_JSON, subscribers)
        await update.message.reply_text(get_localized_message(update, "UNSUBSCRIBE_SUCCESS"), parse_mode="HTML")
    else:
        await update.message.reply_text(get_localized_message(update, "UNSUBSCRIBE_NOT_SUBSCRIBED"), parse_mode="HTML")


async def request_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(get_localized_message(update, "REQUEST_EMPTY"), parse_mode="HTML")
        return
    
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name or "n/a"
    username = update.message.from_user.username or "n/a"
    language_code = update.message.from_user.language_code

    request_text = update.message.text.replace('/request ', '').replace('/request', '')
    request_text = request_text.replace('/richiedi ', '').replace('/richiedi', '')

    tracking_message = f"New request: {request_text}\n\n" \
                        f"User ID: <code>{user_id}</code>\n" \
                        f"First name: {first_name}\n" \
                        f"Last name: {last_name}\n" \
                        f"Username: {username}\n" \
                        f"Language code: {language_code}\n"
    await context.bot.send_message(ADMIN_ID, tracking_message, parse_mode="HTML")

    await update.message.reply_text(get_localized_message(update, "REQUEST_SUCCESS"), parse_mode="HTML")


async def contact_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(get_localized_message(update, "CONTACT_EMPTY"), parse_mode="HTML")
        return
    
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name or "n/a"
    username = update.message.from_user.username or "n/a"
    language_code = update.message.from_user.language_code

    contact_text = update.message.text.replace('/contact ', '').replace('/contact', '')
    contact_text = contact_text.replace('/contatta ', '').replace('/contatta', '')

    contact_message = f"New message from {first_name}:\n" \
                        f"{contact_text}\n\n" \
                        f"User ID: <code>{user_id}</code>\n" \
                        f"First name: {first_name}\n" \
                        f"Last name: {last_name}\n" \
                        f"Username: {username}\n" \
                        f"Language code: {language_code}\n"
    await context.bot.send_message(ADMIN_ID, contact_message, parse_mode="HTML")

    await update.message.reply_text(get_localized_message(update, "CONTACT_SUCCESS"), parse_mode="HTML")


async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(get_localized_message(update, "REPLY_EMPTY"), parse_mode="HTML")
        return
    
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    user_id = context.args[0]
    message_text = update.message.text.replace(f"/reply {user_id} ", "").replace(f"/reply {user_id}", "")
    message_text = message_text.replace(f"/rispondi {user_id} ", "").replace(f"/rispondi {user_id}", "")

    await context.bot.send_message(user_id, get_localized_message(update, "REPLY_HEADER") + message_text + get_localized_message(update, "REPLY_FOOTER"), parse_mode="HTML")
    

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = get_localized_message(update, "HELP_COMMAND_HEADER")
    if update.message.from_user.id == int(ADMIN_ID):
        help_message += get_localized_message(update, "ADMIN_HELP_COMMAND")
    help_message += get_localized_message(update, "HELP_COMMAND_FOOTER")
    await update.message.reply_text(help_message, parse_mode="HTML", disable_web_page_preview=True)


async def broadcast_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    if not update.message.reply_to_message:
        return
    
    subscribers = load_json(SUBSCRIBERS_JSON)
    for subscriber in subscribers:
        await context.bot.copy_message(subscriber["user_id"], update.message.from_user.id, update.message.reply_to_message.message_id)
        await asyncio.sleep(2)

    await update.message.reply_text("Broadcasted.")


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    users = load_json(USERS_JSON)
    subscribers = load_json(SUBSCRIBERS_JSON)
    await update.message.reply_text(f"<b>Users:</b> {len(users)}\n<b>Subscribers:</b> {len(subscribers)}", parse_mode="HTML")


async def restart_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    await update.message.reply_text("Restarting...")
    args = sys.argv[:]
    args.insert(0, sys.executable)
    os.chdir(os.getcwd())
    os.execv(sys.executable, args)


async def album_maker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    if update.message.caption:
        caption = update.message.caption
    
    if update.message.video:
        # if this is the first item in the album, add the caption, else don't add the caption
        if not album:
            media = InputMediaVideo(update.message.video.file_id, caption=caption, parse_mode="HTML")
        else:
            media = InputMediaVideo(update.message.video.file_id)
    elif update.message.document:
        if not album:
            media = InputMediaDocument(update.message.document.file_id, caption=caption, parse_mode="HTML")
        else:
            media = InputMediaDocument(update.message.document.file_id)
    else:
        return
    
    album.append(media)

    await update.message.reply_text("Media added to the album.")        


async def view_album(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    if not album:
        await update.message.reply_text("Album is empty.")
        return
    
    await context.bot.send_media_group(update.message.chat_id, album, parse_mode="HTML")


async def broadcast_album(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    subscribers = load_json(SUBSCRIBERS_JSON)
    for subscriber in subscribers:
        await context.bot.send_media_group(subscriber["user_id"], album, parse_mode="HTML")
        await asyncio.sleep(2)

    await update.message.reply_text("Album broadcasted.")


async def clear_album(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    
    album.clear()
    await update.message.reply_text("Album cleared.")


async def superbroadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != int(ADMIN_ID):
        return
    if not update.message.reply_to_message:
        return
    
    users = load_json(USERS_JSON)
    for user in users:
        await context.bot.copy_message(user["user_id"], update.message.from_user.id, update.message.reply_to_message.message_id)
        await asyncio.sleep(2)

    await update.message.reply_text("Broadcasted.")
    


if __name__ == "__main__":
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler, 1)

    search_handler = CommandHandler(("search", "cerca"), search)
    application.add_handler(search_handler, 2)

    subscribe_handler = CommandHandler(("subscribe", "iscrivimi"), subscribe)
    application.add_handler(subscribe_handler, 3)

    unsubscribe_handler = CommandHandler(("unsubscribe", "disiscrivimi"), unsubscribe)
    application.add_handler(unsubscribe_handler, 4)

    request_handler = CommandHandler(("request", "richiedi"), request_media)
    application.add_handler(request_handler, 5)

    contact_handler = CommandHandler(("contact", "contatta"), contact_admin)
    application.add_handler(contact_handler, 6)

    whisper_handler = CommandHandler(("reply", "rispondi"), whisper)
    application.add_handler(whisper_handler, 7)

    help_handler = CommandHandler("help", help)
    application.add_handler(help_handler, 8)

    broadcast_handler = CommandHandler("broadcast", broadcast_message)
    application.add_handler(broadcast_handler, 9)

    stats_handler = CommandHandler("stats", stats)
    application.add_handler(stats_handler, 10)

    restart_handler = CommandHandler(("restart", "riavvia"), restart_bot)
    application.add_handler(restart_handler, 11)

    view_album_handler = CommandHandler("view", view_album)
    application.add_handler(view_album_handler, 12)

    broadcast_album_handler = CommandHandler("broadcast_album", broadcast_album)
    application.add_handler(broadcast_album_handler, 13)

    clear_album_handler = CommandHandler("clear", clear_album)
    application.add_handler(clear_album_handler, 14)

    superbroadcast_handler = CommandHandler("superbroadcast", superbroadcast)
    application.add_handler(superbroadcast_handler, 15)

    album_maker_handler = MessageHandler(filters.VIDEO | filters.Document.ALL, album_maker)
    application.add_handler(album_maker_handler, 99)

    application.run_polling(drop_pending_updates=True)
