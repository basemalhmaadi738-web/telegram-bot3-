from telegram.ext import CommandHandler

from loader import app
from database import Database

from handlers.start import start

# إنشاء قاعدة البيانات
db = Database()
db.create_tables()

# تسجيل الأوامر
app.add_handler(CommandHandler("start", start))

print("✅ Telegram Manager Bot Started")

# تشغيل البوت
app.run_polling()