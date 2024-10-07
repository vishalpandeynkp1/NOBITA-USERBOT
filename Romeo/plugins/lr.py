import os
import sys
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from nobita import SUDO_USER
from nobita.helper.data import *

@Client.on_message(filters.command(["lraid", "lr"], ".") & (filters.me | filters.user(SUDO_USER)))
async def raid(app: Client, m: Message):  
      nobita = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(nobita) == 2:
        counts = int(nobita[0])
        username = nonita[1]
        if not counts:
          await m.reply_text(f"𝐋ᴏᴠᴇ 𝐑ᴀɪᴅ 𝐋ɪᴍɪᴛ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐏ʟᴇᴀsᴇ 𝐆ɪᴠᴇ 𝐂ᴏᴜɴᴛ!")
          return       
        if not username:
          await m.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐒ᴘᴇᴄɪғʏ 𝐀ɴ 𝐔sᴇʀ! 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀ɴʏ 𝐔sᴇʀ 𝐎ʀ 𝐆ɪᴠᴇ 𝐈ᴅ/𝐔sᴇʀɴᴀᴍᴇ")
          return
        try:
           user = await app.get_users(nobita[1])
        except:
           await m.reply_text("**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ:** 𝐔sᴇʀ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐎ʀ 𝐌ᴀʏ 𝐁ᴇ 𝐃ᴇʟᴇᴛᴇᴅ!")
           return
      elif m.reply_to_message:
        counts = int(nobita[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("𝐔sᴀɢᴇ: .𝐋ʀᴀɪᴅ 𝐂ᴏᴜɴᴛ 𝐔sᴇʀɴᴀᴍᴇ 𝐎ʀ 𝐑ᴇᴘʟʏ")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**𝐒ᴏʀʀʏ !! 𝐘ᴀʜᴀ 𝐒ᴘᴀᴍ 𝐍ʜɪ 𝐇ᴏ 𝐒ᴀᴋᴛᴀ.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("𝐒ᴜᴅᴏ 𝐑ᴀɴᴅɪ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐇ᴏɢᴀ.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(LOVE)}"
         await app.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)


@Client.on_message(filters.command(["dmlraid", "dmlr"], ".") & (filters.me | filters.user(SUDO_USER)))
async def draid(app: Client, m: Message):  
      nobita = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(nobita) == 2:
        counts = int(nobita[0])
        username = nobita[1]
        if not counts:
          await m.reply_text(f"𝐋ᴏᴠᴇ 𝐑ᴀɪᴅ 𝐋ɪᴍɪᴛ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ 𝐏ʟᴇᴀsᴇ 𝐆ɪᴠᴇ 𝐂ᴏᴜɴᴛ!")
          return       
        if not username:
          await m.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐒ᴘᴇᴄɪғʏ 𝐀ɴ 𝐔sᴇʀ ! 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀ɴʏ 𝐔sᴇʀ 𝐎ʀ 𝐆ɪᴠᴇ 𝐈ᴅ/𝐔sᴇʀɴᴀᴍᴇ")
          return
        try:
           user = await app.get_users(nobita[1])
        except:
           await m.reply_text("**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ:** ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴍᴀʏ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ!")
           return
      elif m.reply_to_message:
        counts = int(nobita[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("𝐔sᴀɢᴇ: .𝐃ᴍʟʀᴀɪᴅ 𝐂ᴏᴜɴᴛ 𝐔sᴇʀɴᴀᴍᴇ 𝐎ʀ 𝐑ᴇᴘʟʏ")
        return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("𝐓ʜɪs 𝐆ᴜʏ 𝐈s 𝐀 𝐒ᴜᴅᴏ 𝐔sᴇʀs.")
         return
      mention = user.mention
      await m.reply_text("𝐃ᴍ 𝐋ᴏᴠᴇ 𝐑ᴀɪᴅ 𝐒ᴛᴀʀᴛᴇᴅ..")
      for _ in range(counts): 
         r = f"{choice(LOVE)}"
         await app.send_message(user.id, r)
         await asyncio.sleep(0.3)
