from pyrogram import filters, Client
from pyrogram.types import Message
from nobita import SUDO_USER

@Client.on_message(filters.command(["addsudo", "addrandi"], ".") & (filters.me | filters.user(SUDO_USER)))
async def addsudo(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            if len(message.command) != 2:
                await message.reply_text("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐔sᴇʀ's 𝐌ᴇssᴀɢᴇ 𝐎ʀ 𝐆ɪᴠᴇ 𝐔sᴇʀɴᴀᴍᴇ/𝐔sᴇʀ_𝐈ᴅ.")
                return
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            user = await client.get_users(user)
            if user.id in SUDO_USER:
                await message.reply_text("{0} 𝐀ʟʀᴇᴀᴅʏ 𝐒ᴜᴅᴏ 𝐇ᴀɪ 𝐘ᴇ 𝐃ᴀʟʟᴀ.".format(user.mention))
                return
            SUDO_USER.append(user.id)
            await message.reply_text("𝐁ᴀɴ 𝐆ʏᴀ **{0}** 𝐆ᴀɴᴅᴜ 𝐒ᴜᴅᴏ.".format(user.mention))

        if message.reply_to_message.from_user.id in SUDO_USER:
            await message.reply_text("{0} 𝐀ʟʀᴇᴀᴅʏ 𝐒ᴜᴅᴏ 𝐇ᴀɪ 𝐘ᴇ 𝐃ᴀʟʟᴀ.".format(message.reply_to_message.from_user.mention))
            return
        SUDO_USER.append(message.reply_to_message.from_user.id)
        await message.reply_text("𝐁ᴀɴ 𝐆ʏᴀ **{0}** 𝐆ᴀɴᴅᴜ 𝐒ᴜᴅᴏ.".format(message.reply_to_message.from_user.mention))
    except Exception as e:
        await message.reply_text(f"**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐀ᴀɢʏᴀ 𝐄ʀʀᴏʀ:** `{e}`")
        return

@Client.on_message(filters.command(["delsudo", "rsudo", "randisudo"], ".") & (filters.me | filters.user(SUDO_USER)))
async def rmsudo(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            if len(message.command) != 2:
                await message.reply_text("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐔sᴇʀ's 𝐌ᴇssᴀɢᴇ 𝐎ʀ 𝐆ɪᴠᴇ 𝐔sᴇʀɴᴀᴍᴇ/𝐔sᴇʀ_𝐈ᴅ.")
                return
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            user = await client.get_users(user)
            if user.id not in SUDO_USER:
                await message.reply_text("**{0}** 𝐈s 𝐍ᴏᴛ 𝐀 𝐏ᴀʀᴛ 𝐎ғ 𝐁ᴏᴛ's 𝐒ᴜᴅᴏ.".format(user.mention))
                return 
            SUDO_USER.remove(user.id)
            await message.reply_text("ʀᴇᴍᴏᴠᴇᴅ **{0}** 𝐅ʀᴏᴍ 𝐁ᴏᴛ's 𝐒ᴜᴅᴏ 𝐔sᴇʀ".format(user.mention))
        user_id = message.reply_to_message.from_user.id
        if user_id not in SUDO_USER:
            return await message.reply_text("**{0}** 𝐈s 𝐍ᴏᴛ 𝐀 𝐏ᴀʀᴛ 𝐎ғ 𝐁ᴏᴛ's 𝐒ᴜᴅᴏ.".format(message.reply_to_message.from_user.mention))
        SUDO_USER.remove(user_id)
        await message.reply_text("ʀᴇᴍᴏᴠᴇᴅ **{0}** 𝐅ʀᴏᴍ 𝐁ᴏᴛ's 𝐒ᴜᴅᴏ 𝐔sᴇʀ".format(message.reply_to_message.from_user.mention))
    except Exception as e:
        await message.reply_text(f"**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐀ᴀɢʏᴀ 𝐄ʀʀᴏʀ:** `{e}`")
        return


@Client.on_message(filters.command(["sudolist", "sdl", "randilist"], ".") & (filters.me | filters.user(SUDO_USER)))
async def sudolist(client: Client, message: Message):
    users = SUDO_USER
    ex = await message.edit_text("`𝐇ᴏ 𝐑ᴀʜᴀ 𝐒ᴀʙᴀʀ 𝐊ᴀʀ 𝐃ᴀʟʟᴇ...`")
    if not users:
        await ex.edit("𝐍ᴏ 𝐔sᴇʀs 𝐇ᴀᴠᴇ 𝐁ᴇᴇɴ 𝐒ᴇᴛ 𝐘ᴇᴛ")
        return
    sudo_list = "**𝐒ᴜᴅᴏ 𝐔sᴇʀs:**\n"
    count = 0
    for i in users:
        count += 1
        sudo_list += f"**{count} -** `{i}`\n"
    await ex.edit(sudo_list)
    return 
