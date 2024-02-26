from random import choice
from pyrogram import filters, Client
from pyrogram.types import Message
from Romeo.helper.data import REPLY_RAID, VERIFIED_USERS, GROUP
from Romeo import SUDO_USER

ACTIVATE_RLIST = []

@Client.on_message(filters.command(["rr", "replyraid", "raidreply"], ".") & (filters.me | filters.user(SUDO_USER)))
async def rr(client: Client, message: Message):
    r = await message.edit_text("**𝐒ᴀʙᴀʀ 𝐊ᴀʀ 𝐃ᴀʟʟᴇ**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = message.text.split(None, 1)[1]
        if not user:
            await r.edit("**USER_ID 𝐃ᴏ 𝐘ᴀ 𝐈sᴋᴏ 𝐑ᴇᴘʟʏ 𝐊ᴀʀᴋᴇ 𝐊ᴀʀᴏ**")
            return
    user = await client.get_users(user)
    if int(message.chat.id) in GROUP:
        await r.edit("`𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐒ᴘᴀᴍ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ`")
        return
    if int(user.id) in VERIFIED_USERS:
        await r.edit("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐒ᴘᴀᴍ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
        return
    elif int(user.id) in SUDO_USER:
        await r.edit("𝐘ᴇ 𝐒ᴀʟᴀ 𝐒ᴜᴅᴏ 𝐑ᴀɴᴅɪ 𝐇ᴀɪ.")
        return
    elif int(user.id) in ACTIVATE_RLIST:
        await r.edit("𝐀ʟʀᴇᴀᴅʏ 𝐑ᴀɪᴅ 𝐒ᴇ 𝐂ʜᴜᴅ 𝐑ᴀʜᴀ 𝐇ᴀɪ 𝐘ᴇ 𝐓ᴏʜ.")
        return
    ACTIVATE_RLIST.append(user.id)
    await r.edit(f"**𝐂ʜᴏᴅɴᴇ 𝐊ᴇ 𝐋ɪʏᴇ 𝐑ᴇᴘʟʏʀᴀɪᴅ 𝐋ᴀɢ {user.first_name} 𝐆ʏɪ**")

@Client.on_message(filters.command(["drr", "dreplyraid", "draidreply"], ".") & (filters.me | filters.user(SUDO_USER)))
async def drr(client: Client, message: Message):
    r = await message.edit_text("**𝐒ᴀʙᴀʀ 𝐊ᴀʀ 𝐃ᴀʟʟᴇ**")
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = message.text.split(None, 1)[1]
        if not user:
            await r.edit("ᴜsᴇʀɴᴀᴍᴇ 𝐃ᴏ 𝐘ᴀ 𝐈ᴅ 𝐘ᴀ 𝐑ᴇᴘʟʏ 𝐊ᴀʀᴋᴇ 𝐊ᴀʀᴏ 𝐓ᴀʙʜɪ 𝐑ᴇᴘʟʏʀᴀɪᴅ 𝐎ғғ 𝐇ᴏɢᴀ")
            return
    user = await client.get_users(user)
    if int(user.id) not in ACTIVATE_RLIST:
        await r.edit("𝐈sᴋᴏ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐋ᴀɢᴀ 𝐇ᴜᴀ.")
        return
    ACTIVATE_RLIST.remove(user.id)
    await r.edit(f"**𝐉ᴀᴀ 𝐁ᴀᴄʜᴇ 𝐌ᴀғғ 𝐊ɪʏᴀ 𝐇ᴀᴛᴀ 𝐃ɪ 𝐑ᴀɪᴅ {user.first_name}, 𝐋ᴏʟ**")


@Client.on_message(filters.incoming)
async def watch_raids(client: Client, message: Message):
    try:
        if not message:
            return
        if not message.from_user:
            return
        user = message.from_user.id
        userr = message.from_user
        mention = f"[{userr.first_name}](tg://user?id={userr.id})"
        raid = f"{mention} {choice(REPLY_RAID)}"
        if int(user) in VERIFIED_USERS:
            return
        elif int(user) in SUDO_USER:
            return
        if int(message.chat.id) in GROUP:
            return
        try:
            if not message.from_user.id in ACTIVATE_RLIST:
                return
        except AttributeError:
            return
        try:
            if message.from_user.id in ACTIVATE_RLIST:
                await message.reply_text(raid)
        except Exception as a:
            print(f"𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ (a): {str(a)}")
    except Exception as b:
        print(f"𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ (b): {str(b)}")
