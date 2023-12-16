from sqlite3 import connect

DB_PATH = "TEST.db"

def get_channels_db():
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM channel""")
    channels_info = cursor.fetchall()
    connection.close()
    return channels_info

