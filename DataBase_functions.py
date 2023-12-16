<<<<<<< HEAD
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
    #return {"name_programm": programm_info[0], "Desc": programm_info[1], "channel_id": programm_info[2], "Tags": programm_info[3]}

def get_channel_info(id_channel, on_day):
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT channelname, icopath, liveurl
    FROM channel
    WHERE idchannel = {id_channel}
    """)
    channel_info = cursor.fetchall()
    cursor.execute(f"""SELECT programm.programmname, schedule.starttime, schedule.endtime
    FROM programm, schedule
    WHERE schedule.idchannel = {id_channel} AND schedule.idprogramm = programm.idprogramm AND schedule.date = '{on_day}'""")
    schedule_info = cursor.fetchall()
    connection.close()
    return [channel_info, schedule_info]

def find_somethink(string, on_day, client_time):
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM channel""")
    channel_list = cursor.fetchall()
    i = 0
    while i < len(channel_list):
        if string.lower() not in channel_list[i][1].lower():
            channel_list.pop(i)
        else:
            i+=1
    cursor.execute(f"""SELECT schedule.idchannel, programm.programmname FROM schedule, programm WHERE (schedule.date = '{on_day}') AND ('{client_time}' BETWEEN schedule.starttime AND schedule.endtime) AND (schedule.idprogramm = programm.idprogramm)""")
    programm_list = cursor.fetchall()
    i = 0
    while i < len(programm_list):
        if string.lower() not in programm_list[i][1].lower():
            programm_list.pop(i)
        else:
            i+=1
    new_programm_list = []
    for i in range(len(programm_list)):
        cursor.execute(f"""SELECT programm.programmname, genre.genre, programm.channelid
        FROM programm, genre
        WHERE programm.programmname = '{programm_list[i][1]}' AND genre.idprogramm = programm.idprogramm
        """)
        from_db = cursor.fetchall()
        old_to_new = []
        old_to_new.append(from_db[0][0])
        old_to_new.append(from_db[0][2])
        old_to_new.append([])
        for i in range(len(from_db)):
            old_to_new[2].append(from_db[i][1])
        new_programm_list.append(old_to_new)



    connection.close()
    return [channel_list, new_programm_list]
=======
from sqlite3 import connect
import pprint

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
    #return {"name_programm": programm_info[0], "Desc": programm_info[1], "channel_id": programm_info[2], "Tags": programm_info[3]}

def get_channel_info(id_channel, on_day):
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT channelname, icopath, liveurl
    FROM channel
    WHERE idchannel = {id_channel}
    """)
    channel_info = cursor.fetchall()
    cursor.execute(f"""SELECT programm.programmname, schedule.starttime, schedule.endtime
    FROM programm, schedule
    WHERE schedule.idchannel = {id_channel} AND schedule.idprogramm = programm.idprogramm AND schedule.date = '{on_day}'""")
    schedule_info = cursor.fetchall()
    connection.close()
    return [channel_info, schedule_info]

def find_somethink(string, on_day, client_time):
    connection = connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(f"""SELECT * FROM channel""")
    channel_list = cursor.fetchall()
    i = 0
    while i < len(channel_list):
        if string.lower() not in channel_list[i][1].lower():
            channel_list.pop(i)
        else:
            i+=1
    cursor.execute(f"""SELECT schedule.idchannel, programm.programmname FROM schedule, programm WHERE (schedule.date = '{on_day}') AND ('{client_time}' BETWEEN schedule.starttime AND schedule.endtime) AND (schedule.idprogramm = programm.idprogramm)""")
    programm_list = cursor.fetchall()
    i = 0
    while i < len(programm_list):
        if string.lower() not in programm_list[i][1].lower():
            programm_list.pop(i)
        else:
            i+=1
    new_programm_list = []
    for i in range(len(programm_list)):
        cursor.execute(f"""SELECT programm.programmname, genre.genre, programm.channelid
        FROM programm, genre
        WHERE programm.programmname = '{programm_list[i][1]}' AND genre.idprogramm = programm.idprogramm
        """)
        from_db = cursor.fetchall()
        old_to_new = []
        old_to_new.append(from_db[0][0])
        old_to_new.append(from_db[0][2])
        old_to_new.append([])
        for i in range(len(from_db)):
            old_to_new[2].append(from_db[i][1])
        new_programm_list.append(old_to_new)



    connection.close()
    return [channel_list, new_programm_list]

#print(find_somethink('с', '2023-12-18', '05:37'))
>>>>>>> eb842327159027ae13a6d93bd4469f9a73c7a774
