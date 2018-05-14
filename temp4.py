import sqlite3
conn = sqlite3.connect("E:\\sqlite\\和合本.db")
cursor = conn.cursor()



cursor.close()
conn.close()
