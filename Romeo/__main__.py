import asyncio
import importlib
from pyrogram import Client, idle
from nobita import client, app

async def start_bot():
    await app.start()
    print("ʟᴏɢ.. ꜰᴏᴜɴᴅᴇᴅ ʙᴏᴛ ᴛᴏᴋᴇɴ ʙᴏᴏᴛɪɴɢ..")
    print("ɴᴏʙɪᴛᴀ ᴜꜱᴇʀʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ")
    await client.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
