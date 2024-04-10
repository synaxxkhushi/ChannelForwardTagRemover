import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TXT = """
𝐇𝐢 {}\n\n 𝐈'𝐦 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐚𝐠 𝐑𝐞𝐦𝐨𝐯𝐞𝐫 𝐁𝐨𝐭 🍃.\n\n𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐦𝐞 𝐬𝐨𝐦𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬,\n𝐢 𝐰𝐢𝐥𝐥 𝐫𝐞𝐦𝐨𝐯𝐞 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐚𝐠 𝐅𝐫𝐨𝐦 𝐓𝐡𝐞𝐦 🌷.\n\n𝐀𝐥𝐬𝐨 𝐜𝐚𝐧 𝐝𝐨 𝐢𝐭 𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬 🐰
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🇮🇳 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🇮🇳', url='https://t.me/synaxnetwork'),
        ]]
    )


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
            await m.delete()
        else:
            await m.copy(m.chat.id)
            await m.delete()
    except FloodWait as e:
        await asyncio.sleep(e.value)


@bot.on_message(filters.private | filters.group)
async def fwdrm(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
        else:
            await m.copy(m.chat.id)
    except FloodWait as e:
        await asyncio.sleep(e.value)


bot.run()
