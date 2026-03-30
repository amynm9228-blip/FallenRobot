import os

class Config(object):
    LOGGER = True

    # Telegram API credentials - from my.telegram.org/apps
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")

    # Bot token - from @BotFather
    TOKEN = os.environ.get("TOKEN", "")

    # Database
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")

    # Owner
    OWNER_ID = int(os.environ.get("OWNER_ID", 1356469075))

    # Optional API keys
    CASH_API_KEY = os.environ.get("CASH_API_KEY", "")
    TIME_API_KEY = os.environ.get("TIME_API_KEY", "")

    # Bot settings
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg")
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "DevilsHeavenMF")
    EVENT_LOGS = os.environ.get("EVENT_LOGS", "")

    # Optional user lists
    BL_CHATS = []
    DRAGONS = []
    DEV_USERS = []
    DEMONS = []
    TIGERS = []
    WOLVES = []

    # Feature flags
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    STRICT_GBAN = True

    LOAD = []
    NO_LOAD = []
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
