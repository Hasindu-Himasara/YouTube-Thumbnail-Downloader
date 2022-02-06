# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
import ytthumb
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('🌷 Join Updates Channel', url='https://t.me/Altex_Updates')]])

Bot = Client(
    "YouTube-Thumbnail-Downloader",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def send_thumbnail(bot, update):
    message = await update.reply_text(
        text="Analysing...",
        disable_web_page_preview=True,
        quote=True
    )
    try:
        if " | " in update.text:
            video = update.text.split(" | ", -1)[0]
            quality = update.text.split(" | ", -1)[1]
        else:
            video = update.text
            quality = "sd"
        thumbnail = ytthumb.thumbnail(
            video=video,
            quality=quality
        )
        await update.reply_photo(
            photo=thumbnail,
            reply_markup=BUTTONS,
            quote=True
        )
        await message.delete()
    except Exception as error:
        await message.edit_text(
            text=error,
            disable_web_page_preview=True,
            reply_markup=BUTTONS
        )


Bot.run()
