import sqlite3

def init_db():
    conn = sqlite3.connect("zara_memory.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS chat_history (
                        user_id INTEGER,
                        message TEXT
                    )""")
    conn.commit()
    conn.close()

def store_message(user_id, message):
    conn = sqlite3.connect("zara_memory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (user_id, message) VALUES (?, ?)", (user_id, message))
    conn.commit()
    conn.close()

def get_history(user_id, limit=10):
    conn = sqlite3.connect("zara_memory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM chat_history WHERE user_id = ? ORDER BY ROWID DESC LIMIT ?", (user_id, limit))
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in reversed(rows)]

def clear_history(user_id):
    conn = sqlite3.connect("zara_memory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_history WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
