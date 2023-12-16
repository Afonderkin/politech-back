from sqlite3 import connect

DB_PATH = "TEST.db"

def get_channels_db():
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM channel""")
    channels_info = cursor.fetchall()
    connection.close()
    channels_info = [{'id': el[0], 'ChannelName': el[1], 'ICOPath': el[2], 'LiveURL': el[3]} for el in channels_info]
    return channels_info
