import sqlite3
from config import DATABASE_NAME


class Database:

    def __init__(self):
        self.db = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.db.cursor()

    def create_tables(self):

        # ==========================
        # المستخدمون
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # ==========================
        # المجموعات
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS groups(
            chat_id INTEGER PRIMARY KEY,
            title TEXT,
            language TEXT DEFAULT 'ar',
            welcome INTEGER DEFAULT 1,
            protection INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # ==========================
        # المطورون
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS developers(
            user_id INTEGER PRIMARY KEY
        )
        """)

        # ==========================
        # ملاك المجموعات
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS owners(
            chat_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY(chat_id,user_id)
        )
        """)

        # ==========================
        # المدراء
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins(
            chat_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY(chat_id,user_id)
        )
        """)

        # ==========================
        # المحظورون
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bans(
            chat_id INTEGER,
            user_id INTEGER,
            reason TEXT,
            PRIMARY KEY(chat_id,user_id)
        )
        """)

        # ==========================
        # المكتومون
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS mutes(
            chat_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY(chat_id,user_id)
        )
        """)
        # ==========================
        # التحذيرات
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS warnings(
            chat_id INTEGER,
            user_id INTEGER,
            warns INTEGER DEFAULT 0,
            PRIMARY KEY(chat_id,user_id)
        )
        """)

        # ==========================
        # تغيير الأوامر
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands(
            command TEXT PRIMARY KEY,
            new_command TEXT
        )
        """)

        # ==========================
        # إعدادات الحماية
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(
            chat_id INTEGER PRIMARY KEY,
            anti_spam INTEGER DEFAULT 1,
            anti_links INTEGER DEFAULT 1,
            anti_bots INTEGER DEFAULT 1,
            anti_flood INTEGER DEFAULT 1
        )
        """)

        # ==========================
        # الهمسات
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS whispers(
            whisper_id TEXT PRIMARY KEY,
            sender INTEGER,
            receiver INTEGER,
            message TEXT
        )
        """)

        self.db.commit()
            def add_user(self, user_id, first_name, username):
        self.cursor.execute("""
        INSERT OR IGNORE INTO users(user_id, first_name, username)
        VALUES (?, ?, ?)
        """, (user_id, first_name, username))
        self.db.commit()


    def add_group(self, chat_id, title):
        self.cursor.execute("""
        INSERT OR IGNORE INTO groups(chat_id, title)
        VALUES (?, ?)
        """, (chat_id, title))
        self.db.commit()


    def add_admin(self, chat_id, user_id):
        self.cursor.execute("""
        INSERT OR IGNORE INTO admins(chat_id, user_id)
        VALUES (?, ?)
        """, (chat_id, user_id))
        self.db.commit()


    def remove_admin(self, chat_id, user_id):
        self.cursor.execute("""
        DELETE FROM admins
        WHERE chat_id=? AND user_id=?
        """, (chat_id, user_id))
        self.db.commit()


    def is_admin(self, chat_id, user_id):
        self.cursor.execute("""
        SELECT * FROM admins
        WHERE chat_id=? AND user_id=?
        """, (chat_id, user_id))

        return self.cursor.fetchone() is not None


    def close(self):
        self.db.close()