from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from nobita import SUDO_USER, spam_chats

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@Client.on_message(filters.command("all", ".") & (filters.me | filters.user(SUDO_USER)))
async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**𝐒ᴇɴᴅ 𝐌ᴇ 𝐀 𝐌ᴇssᴀɢᴇ 𝐎ʀ 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 4:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@Client.on_message(filters.command("cancel", ".") & (filters.me | filters.user(SUDO_USER)))
async def cancel_spam(client: Client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("**𝐈ᴛ 𝐒ᴇᴇᴍs 𝐓ʜᴇʀᴇ 𝐈s 𝐍ᴏ 𝐓ᴀɢ 𝐀ʟʟ 𝐇ᴇʀᴇ.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**𝐂ᴀɴᴄᴇʟ 𝐇ᴏ 𝐆ʏᴀ.**")
