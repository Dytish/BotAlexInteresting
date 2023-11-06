
from internal.dispatcher import bd
from datetime import datetime


comand_check_quest = """SELECT * FROM questionnaires WHERE user_tg_id = %s"""
comand_check_vip = """SELECT id FROM questionnaires WHERE vip = %s"""
comand_add_quest = """INSERT INTO questionnaires ( {} ) 
                                        VALUES ( {} ) RETURNING id"""
comand_add_images = """INSERT INTO images ( name, url, quest_id )
                                        VALUES ( %s, %s, %s ) """

# user_tg_id = %s, title = %s, 
#                                         previe = %s, info = %s, info_mob = %s, 
#                                         info_social = %s, vip = %s, sub = %s, 
#                                         updated_at = %s, deleted_at = %s, created_at = %s

comand_change_quest = """Update questionnaires set {} 
                                                WHERE id = {}"""

def add_new_images( images:list ) -> None:
    """Добавляет медиа в бд"""
    conn = bd.conn
    curs = conn.cursor()
    # images = [("sada", "sadsad", 1), ("sad111a", "sa21dsad", 1)]
    curs.executemany(comand_add_images, images)
    conn.commit()

def add_new( quest: dict) -> int:
    """Добавляет анкету в бд"""
    conn = bd.conn
    curs = conn.cursor()
    qurst_values = tuple(quest.values())
    qurst_keys = ', '.join(quest.keys()) 
    count_values = "%s, "*len(qurst_values)
    comand_add_quest = comand_add_quest.format(qurst_keys, str[:-2])
    curs.execute(comand_add_quest, qurst_values)
    conn.commit()
    insertId = curs.fetchone()
    # print(insertId)
    return insertId

def check( id_telegram:int) ->int:
    """Проверяет есть ли анкета в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_check_quest, (id_telegram, ), )
    conn.commit()
    res = curs.fetchall()
    # print(len(res))
    return len(res)

def find_quest(id_telegram:int ) -> list:
    """Находит анкету в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_check_quest, (id_telegram, ), )
    conn.commit()
    res = curs.fetchall()
    # print(len(res))
    return len(res)

def edit_quest(quest:dict, id:int) -> None:
    """Изменение анкеты"""
    conn = bd.conn
    curs = conn.cursor()
    qurst_values = tuple(quest.values())
    qurst_keys = quest.keys() 

    # print(type(quest))
    # print(quest)
    str_key = ""
    for key in qurst_keys:
        str_key += f"{key}= %s, "
        # print(f"{key}= %s,")
    print(str_key[:-2])
    comand_change_quest1 = comand_change_quest.format(str_key[:-2], id)
    print("ssa", comand_change_quest1)
    curs.execute(comand_change_quest1, qurst_values)
    conn.commit()

def check_vip(vip: int):
    """Проверяет есть пользователь 
        с таким приоритетом в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_check_vip, (vip, ), )
    conn.commit()
    res = curs.fetchall()
    # print(len(res))
    return len(res)