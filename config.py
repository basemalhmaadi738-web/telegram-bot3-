import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# معلومات البوت
# =========================

BOT_NAME = os.getenv("BOT_NAME", "Telegram Manager Bot")

BOT_VERSION = "1.0.0"

# =========================
# التوكن
# =========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# المطور الأساسي
# =========================

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# =========================
# قاعدة البيانات
# =========================

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "data/database.db"
)

# =========================
# الحماية
# =========================

SPAM_LIMIT = 5
SPAM_SECONDS = 10
MAX_WARNINGS = 3

# =========================
# اللغة
# =========================

LANGUAGE = "ar"

# =========================
# السجلات
# =========================

ENABLE_LOGS = True