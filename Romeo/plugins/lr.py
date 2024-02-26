import os
import sys
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from Romeo import SUDO_USER
from Romeo.helper.data import *

@Client.on_message(filters.command(["lraid", "lr"], ".") & (filters.me | filters.user(SUDO_USER)))
async def raid(app: Client, m: Message):  
      Romeo = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Romeo) == 2:
        counts = int(Romeo[0])
        username = Romeo[1]
        if not counts:
          await m.reply_text(f"ʟᴏᴠᴇ ʀᴀɪᴅ ʟɪᴍɪᴛ ɴᴏᴛ ғᴏᴜɴᴅ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛ!")
          return       
        if not username:
          await m.reply_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀɴ ᴜsᴇʀ! ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ")
          return
        try:
           user = await app.get_users(Romeo[1])
        except:
           await m.reply_text("**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ:** ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴍᴀʏ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ!")
           return
      elif m.reply_to_message:
        counts = int(Romeo[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("ᴜsᴀɢᴇ: .ʟʀᴀɪᴅ ᴄᴏᴜɴᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**sᴏʀʀʏ !! ʏᴀʜᴀ sᴘᴀᴍ ɴʜɪ ʜᴏ sᴀᴋᴛᴀ.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("sᴜᴅᴏ ʀᴀɴᴅɪ ᴘᴀʀ ʀᴀɪᴅ ɴʜɪ ʜᴏɢᴀ.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(LOVE)}"
         await app.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)


@Client.on_message(filters.command(["dmlraid", "dmlr"], ".") & (filters.me | filters.user(SUDO_USER)))
async def draid(app: Client, m: Message):  
      Romeo = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Romeo) == 2:
        counts = int(Romeo[0])
        username = Romeo[1]
        if not counts:
          await m.reply_text(f"ʟᴏᴠᴇ ʀᴀɪᴅ ʟɪᴍɪᴛ ɴᴏᴛ ғᴏᴜɴᴅ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴄᴏᴜɴᴛ!")
          return       
        if not username:
          await m.reply_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀɴ ᴜsᴇʀ ! 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀ɴʏ 𝐔sᴇʀ 𝐎ʀ 𝐆ɪᴠᴇ 𝐈ᴅ/𝐔sᴇʀɴᴀᴍᴇ")
          return
        try:
           user = await app.get_users(Romeo[1])
        except:
           await m.reply_text("**𝐋ᴇʟᴇ 𝐋ᴀᴜᴅᴀ 𝐄ʀʀᴏʀ 𝐀ᴀɢʏᴀ:** ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ᴏʀ ᴍᴀʏ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ!")
           return
      elif m.reply_to_message:
        counts = int(Romeo[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("ᴜsᴀɢᴇ: .ᴅᴍʟʀᴀɪᴅ ᴄᴏᴜɴᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ")
        return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("𝐒ᴏʀʀʏ 𝐀ᴘ 𝐀ᴘɴᴇ 𝐁ᴀᴀᴘ 𝐏ᴀʀ 𝐑ᴀɪᴅ 𝐍ʜɪ 𝐊ᴀʀ 𝐒ᴀᴋᴛᴇ")
         return
      if int(user.id) in SUDO_USER:
         await m.reply_text("ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀs.")
         return
      mention = user.mention
      await m.reply_text("ᴅᴍ ʟᴏᴠᴇ ʀᴀɪᴅ sᴛᴀʀᴛᴇᴅ..")
      for _ in range(counts): 
         r = f"{choice(LOVE)}"
         await app.send_message(user.id, r)
         await asyncio.sleep(0.3)
