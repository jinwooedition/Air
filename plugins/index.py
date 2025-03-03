import logging
import logging.config
import ntplib
from time import ctime, sleep

# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from lazybot import LazyPrincessBot

from util.keepalive import ping_server
from lazybot.clients import initialize_clients


PORT = "8080"
LazyPrincessBot.start()
loop = asyncio.get_event_loop()


def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        print(f"Time before sync: {ctime()}")
        print(f"Time after sync: {ctime(response.tx_time)}")
    except Exception as e:
        print(f"Could not sync time: {e}")


async def Lazy_start():
    print('\n')
    print(' Initalizing Telegram Bot ')
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    await initialize_clients()
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats , lz_verified = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    temp.LAZY_VERIFIED_CHATS = lz_verified
    await Media.ensure_indexes()
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    LazyPrincessBot.username = '@' + me.username
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if ON_HEROKU else BIND_ADRESS
    await web.TCPSite(app, bind_address, PORT).start()
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    await idle()


if __name__ == '__main__':
    sync_time()
    sleep(5)  # Add a delay to ensure time sync before starting the bot
    try:
        loop.run_until_complete(Lazy_start())
        logging.info('-----------------------🧐 Service running in Lazy Mode 😴-----------------------')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')import logging
import logging.config
import ntplib
from time import ctime, sleep

# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import idle
from lazybot import LazyPrincessBot

from util.keepalive import ping_server
from lazybot.clients import initialize_clients


PORT = "8080"
LazyPrincessBot.start()
loop = asyncio.get_event_loop()


def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        print(f"Time before sync: {ctime()}")
        print(f"Time after sync: {ctime(response.tx_time)}")
    except Exception as e:
        print(f"Could not sync time: {e}")


async def Lazy_start():
    print('\n')
    print(' Initalizing Telegram Bot ')
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    bot_info = await LazyPrincessBot.get_me()
    LazyPrincessBot.username = bot_info.username
    await initialize_clients()
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats , lz_verified = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    temp.LAZY_VERIFIED_CHATS = lz_verified
    await Media.ensure_indexes()
    me = await LazyPrincessBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    LazyPrincessBot.username = '@' + me.username
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0" if ON_HEROKU else BIND_ADRESS
    await web.TCPSite(app, bind_address, PORT).start()
    logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    await idle()


if __name__ == '__main__':
    sync_time()
    sleep(5)  # Add a delay to ensure time sync before starting the bot
    try:
        loop.run_until_complete(Lazy_start())
        logging.info('-----------------------🧐 Service running in Lazy Mode 😴-----------------------')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')
                        [InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="requireauth") ],
                        [InlineKeyboardButton('⨳  C L Ф S Ξ  ⨳', callback_data='cancel')]]
            reply_markup = InlineKeyboardMarkup(buttons)
            file = getattr(message, message.media.value)
            filename = file.file_name
            filesize = humanize.naturalsize(file.file_size) 
            k = await message.reply(
                                f"\n⨳ *•.¸♡ LΛＺ𝐲 ＭⓄｄ𝓔 ♡¸.•* ⨳\n\n🤩 Do you know LazyPrincess can do a lot of things at a time...\nWould you like to try some of it's amazing features... \n\n🪬Chat ID/ Username: <code>{chat_id}</code>\nℹ️Last Message ID: <code>{last_msg_id}</code> \n\n🎞**File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`",
                                reply_to_message_id=message.id,
                                reply_markup=reply_markup)
            await asyncio.sleep(600)
            await k.delete()
    else:
        await message.reply('🎉\n\n\n❤️ Thank You For the Contribution, Wait For My Moderators to verify the files.\n\n\n🎁')
 

@Client.on_message(filters.command('setskip') & filters.user(ADMINS))
async def set_skip_number(bot, message):
    if ' ' in message.text:
        _, skip = message.text.split(" ")
        try:
            skip = int(skip)
        except:
            return await message.reply("Skip number should be an integer.")
        await message.reply(f"Successfully set SKIP number as {skip}")
        temp.CURRENT = int(skip)
    else:
        await message.reply("Give me a skip number")

  async def index_files_to_db(lst_msg_id, chat, msg, bot):
    total_files = 0
    duplicate = 0
    errors = 0
    deleted = 0
    no_media = 0
    unsupported = 0
    async with lock:
        try:
            current = temp.CURRENT
            temp.CANCEL = False
            async for message in bot.iter_messages(chat, lst_msg_id, temp.CURRENT):
                if temp.CANCEL:
                    await msg.edit(f"Successfully Cancelled!!\n\nSaved <code>{total_files}</code> files to dataBase!\nDuplicate Files Skipped: <code>{duplicate}</code>\nDeleted Messages Skipped: <code>{deleted}</code>\nNon-Media messages skipped: <code>{no_media + unsupported}</code>(Unsupported Media - `{unsupported}` )\nErrors Occurred: <code>{errors}</code>")
                    break
                current += 1
                if current % 20 == 0:
                    can = [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
                    reply = InlineKeyboardMarkup(can)
                    await msg.edit_text(
                        text=f"Total messages fetched: <code>{current}</code>\nTotal messages saved: <code>{total_files}</code>\nDuplicate Files Skipped: <code>{duplicate}</code>\nDeleted Messages Skipped: <code>{deleted}</code>\nNon-Media messages skipped: <code>{no_media + unsupported}</code>(Unsupported Media - `{unsupported}` )\nErrors Occurred: <code>{errors}</code>",
                        reply_markup=reply)
                if message.empty:
                    deleted += 1
                    continue
                elif not message.media:
                    no_media += 1
                    continue
                elif message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
                    unsupported += 1
                    continue
                media = getattr(message, message.media.value, None)
                if not media:
                    unsupported += 1
                    continue
                media.file_type = message.media.value
                media.caption = message.caption
                
                Retry logic for msg_id errors
                for attempt in range(3):
                    try:
                        aynav, vnay = await save_file(media)
                        break  # Exit the retry loop if successful
                    except BadMsgNotification as e:
                        if e.error_code == 16:  # msg_id is too low
                            await asyncio.sleep(1)  # Wait for a second before retrying
                        else:
                            raise
                
                if aynav:
                    total_files += 1
                elif vnay == 0:
                    duplicate += 1
                elif vnay == 2:
                    errors += 1
        except Exception as e:
            logger.exception(e)
            await msg.edit(f'Error baby: {e}')
        else:
            await msg.edit(f'Successfully saved <code>{total_files}</code> to dataBase!\nDuplicate Files Skipped: <code>{duplicate}</code>\nDeleted Messages Skipped: <code>{deleted}</code>\nNon-Media messages skipped: <code>{no_media + unsupported}</code>(Unsupported Media - `{unsupported}` )\nErrors Occurred: <code>{errors}</code>')
