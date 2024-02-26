import asyncio
import importlib
from pyrogram import Client, idle
from Romeo import client, app

async def start_bot():
    await app.start()
    print("𝐋ᴏɢ: 𝐅ᴏᴜɴᴅᴇᴅ 𝐁ᴏᴛ 𝐓ᴏᴋᴇɴ 𝐁ᴏᴏᴛɪɴɢ..")
    print("𝐋ɪʟʏ 𝐔sᴇʀʙᴏᴛ 𝐒ᴛᴀʀᴛᴇᴅ")
    await client.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
