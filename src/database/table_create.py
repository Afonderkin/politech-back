from sqlite3 import connect

DB_PATH = "TEST.db"

#connection = connect(DB_PATH)
#cursor = connection.cursor()


def create_channeldb():
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS channel(
    IDchannel INTEGER PRIMARY KEY,
    ChannelName TEXT,
    ICOPath TEXT,
    LiveURL TEXT
    )""")
    connection.commit()
    connection.close()

def create_programmdb():
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS programm(
    IDprogramm INTEGER PRIMARY KEY,
    ProgrammName TEXT,
    ChannelID INTEGER,
    Description TEXT,
    FOREIGN KEY (ChannelID) REFERENCES channel (IDchannel)
    )""")
    connection.commit()
    connection.close()

def create_schedule():
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedule(
    IDchannel INTEGER,
    IDprogramm INTEGER,
    Date TEXT NOT NULL,
    StartTime TEXT NOT NULL,
    EndTime TEXT NOT NULL,
    FOREIGN KEY (IDchannel) REFERENCES channel (IDchannel),
    FOREIGN KEY (IDprogramm) REFERENCES programm (IDprogramm)
    )""")
    connection.commit()
    connection.close()

def create_genredb():

    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS genre(
    IDprogramm INTEGER,
    Genre TEXT,
    FOREIGN KEY (IDprogramm) REFERENCES programm (IDprogramm)
    )""")

    connection.commit()
    connection.close()


