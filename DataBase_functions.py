from sqlite3 import connect

DB_PATH = "TVDataBase.db"

def get_channels_db():
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM channel""")
    channels_info = cursor.fetchall()
    connection.close()
    return channels_info

def get_programm_db(idprgramm):
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT programm.programmname, programm.description, genre.genre, programm.channelid
    FROM programm, genre
    WHERE programm.idprogramm = {idprgramm} AND genre.idprogramm = programm.idprogramm
    """)
    programm_info_db = cursor.fetchall()
    programm_info = []
    programm_info.append(programm_info_db[0][0])
    programm_info.append(programm_info_db[0][1])
    programm_info.append(programm_info_db[0][3])
    programm_info.append([])
    for i in range(len(programm_info_db)):
        programm_info[3].append(programm_info_db[i][2])
    connection.close()
    return programm_info