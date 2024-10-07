import asyncio
from re import sub
from threading import Event
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from nobita.helper.data import GROUP

from config import *
from nobita import SUDO_USER 

commands = ["spam", "startspam", "slowspam", "fastspam"]
SPAM_COUNT = [0]


def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 999

async def extract_args(message, markdown=True):
    if not (message.text or message.caption):
        return ""

    text = message.text or message.caption

    text = text.markdown if markdown else text
    if " " not in text:
        return ""

    text = sub(r"\s+", " ", text)
    text = text[text.find(" ") :].strip()
    return text

@Client.on_message(filters.command(["dspam", "delayspam", "ds"], ".") & (filters.me | filters.user(SUDO_USER)))
async def delayspam(client: Client, message: Message):
    if message.chat.id in GROUP:
        return await message.reply_text(
            "**𝐒ᴏʀʀʏ 𝐁ᴀʙᴇ 𝐏ᴀʀ 𝐘ᴇ 𝐂ᴍᴅ 𝐘ᴀʜᴀ 𝐍ʜɪ 𝐇ᴏ 𝐒ᴀᴋᴛᴀ ☹️**"
        )
    delayspam = await extract_args(message)
    arr = delayspam.split()
    delay = float(arr[0])
    count = int(arr[1])
    spam_message = delayspam.replace(arr[0], "", 1)
    spam_message = spam_message.replace(arr[1], "", 1).strip()
    await message.delete()

    if not spam_allowed():
        return

    delaySpamEvent = Event()
    for i in range(0, count):
        if i != 0:
            delaySpamEvent.wait(delay)
        await client.send_message(message.chat.id, spam_message)
        limit = increment_spam_count()
        if not limit:
            break

    await client.send_message(
        LOG_GROUP, "**#𝐃ᴇʟᴀʏ_𝐒ᴘᴀᴍ**\n𝐃ᴇᴀʟᴀʏ_𝐒ᴘᴀᴍ 𝐖ᴀs 𝐄xᴇᴄᴜᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ"
    )


@Client.on_message(filters.command(commands, ".") & (filters.me | filters.user(SUDO_USER)))
async def sspam(client: Client, message: Message):
    if message.chat.id in GROUP:
        return await message.reply_text(
            "**𝐒ᴏʀʀʏ 𝐁ᴀʙᴇ 𝐏ᴀʀ 𝐘ᴇ 𝐂ᴍᴅ 𝐘ᴀʜᴀ 𝐍ʜɪ 𝐇ᴏ 𝐒ᴀᴋᴛᴀ ☹️**"
        )
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    cooldown = {"spam": 0.1, "startspam": 0.1, "slowspam": 0.9, "fastspam": 0}

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await client.send_message(message.chat.id, text)

        if message.command[0] == "statspam":
            await asyncio.sleep(0.1)
            await sent.delete()

        await asyncio.sleep(cooldown[message.command[0]])


@Client.on_message(filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], ".") & (filters.me | filters.user(SUDO_USER)))
async def spam_stick(client: Client, message: Message):
    if message.chat.id in GROUP:
        return await message.reply_text(
            "**𝐒ᴏʀʀʏ 𝐁ᴀʙᴇ 𝐏ᴀʀ 𝐘ᴇ 𝐂ᴍᴅ 𝐘ᴀʜᴀ 𝐍ʜɪ 𝐇ᴏ 𝐒ᴀᴋᴛᴀ ☹️**"
        )
    if not message.reply_to_message:
        await message.reply_text(
            "*𝐃ᴀʟʟᴇ 𝐒ᴛɪᴄᴋᴇʀ 𝐓ᴀɢ 𝐊ᴀʀᴋᴇ 𝐂ᴍᴅ 𝐔sᴇ 𝐊ᴀʀ 𝐓ᴀʙ 𝐇ᴏɢᴀ**"
        )
        return
    if not message.reply_to_message.sticker:
        await message.reply_text(
            "**𝐃ᴀʟʟᴇ 𝐒ᴛɪᴄᴋᴇʀ 𝐓ᴀɢ 𝐊ᴀʀᴋᴇ 𝐂ᴍᴅ 𝐔𝐬ᴇ 𝐊ᴀʀ 𝐓ᴀʙ 𝐇ᴏɢᴀ**"
        )
        return
    else:
        i = 0
        times = message.command[1]
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == enums.ChatType.PRIVATE:
            for i in range(int(times)):
                sticker = message.reply_to_message.sticker.file_id
                await client.send_sticker(message.chat.id, sticker)
                await asyncio.sleep(0.10)
