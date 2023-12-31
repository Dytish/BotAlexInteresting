
from internal.dispatcher import bd
from datetime import datetime


comand_check_quest = """SELECT * FROM questionnaires WHERE user_tg_id = %s"""
comand_check_vip = """SELECT id FROM questionnaires WHERE vip = %s"""
comand_add_quest = """INSERT INTO questionnaires (user_tg_id, images, title, 
                                        previe, info, info_mob, 
                                        info_social, vip, sub, 
                                        updated_at, deleted_at, created_at) 
                                        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

comand_change_status_user = """Update questionnaires set status = %s, updated_at = %s
                                                where id_telegram = %s"""


def add_new( quest:tuple) -> None:
    """Добавляет пользователя в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_add_quest, quest)
    conn.commit()

def check( id_telegram:int) ->int:
    """Проверяет есть ли анкета в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_check_quest, (id_telegram, ), )
    # curs.execute(
    #     """SELECT * FROM users WHERE id_telegram = %s""",
    #     (int(id_telegram)),
    # )
    conn.commit()
    res = curs.fetchall()
    # print(len(res))
    return len(res)


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