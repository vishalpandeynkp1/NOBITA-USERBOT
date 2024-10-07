import os
from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
from nobita import SUDO_USER

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegram")
auth_url = r["auth_url"]

def get_text(message: Message) -> [None, str]:
    """𝐄xᴛʀᴀᴄᴛ 𝐓ᴇxᴛ 𝐅ʀᴏᴍ 𝐂ᴏᴍᴍᴀɴᴅs"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.command(["tg", "telegraph", "tm", "tgt"], ".") & (filters.me | filters.user(SUDO_USER)))
async def uptotelegraph(client: Client, message: Message):
    tex = await message.edit_text("`Processing . . .`")
    if not message.reply_to_message:
        await tex.edit(
            "**𝐁sᴅᴋ 𝐊ɪsɪ 𝐌ᴇᴅɪᴀ 𝐊ᴇ 𝐒ᴀᴛʜ 𝐓ᴀɢ 𝐊ᴀʀ.**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ 𝐀ʙ:** `{exc}`")
            os.remove(m_d)
            return
        U_done = (
            f"**https://telegra.ph/{media_url[0]}**"
        )
        await tex.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**ERROR:** `{exc}`")
            return
        wow_graph = f"**https://telegra.ph/{response['path']}"
        await tex.edit(wow_graph)
                                    
