from os import getenv

API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6242589578").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://envs.sh/I09.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/vishalpandeynkp1/Nobitauserbot")
BRANCH = getenv("BRANCH", "main")
