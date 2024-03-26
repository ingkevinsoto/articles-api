import sqlite3

conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, image_url TEXT, autor TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, phone TEXT, message TEXT)''')

conn.commit()
conn.close()


