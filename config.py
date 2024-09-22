from os import getenv

API_ID = int(getenv("API_ID", "21237427"))
API_HASH = getenv("API_HASH", "9fddf284152a3792475388ce0bb61435)
BOT_TOKEN = getenv("BOT_TOKEN", "7895092224:AAHAAtpFYH02h-MXAQDnYzA2oMVLLA6R8V8")
OWNER_ID = int(getenv("OWNER_ID", "5008302137"))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6812888267").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/9db83cb6ae0b870c34e49.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/Team-CF-Bots/Lily-Userbot")
BRANCH = getenv("BRANCH", "main")
