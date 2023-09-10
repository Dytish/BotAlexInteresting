
from internal.dispatcher import bd
from datetime import datetime


comand_check_user = """SELECT * FROM users WHERE id_telegram = %s"""
comand_add_user = """INSERT INTO users (id_telegram, username, first_name, last_name, 
                                        bio, language_code, utm, status, is_premium, 
                                        updated_at, deleted_at, created_at, type_user_id) 
                                        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
comand_take_user = """SELECT id_telegram, username, first_name, last_name, 
                                bio, language_code, utm, status, is_premium, 
                                updated_at, type_user_id 
                                FROM users WHERE id_telegram = %s"""

comand_take_type_user = """SELECT type_user_id
                                FROM users WHERE id_telegram = %s"""

comand_change_status_user = """Update users set status = %s, updated_at = %s
                                                where id_telegram = %s"""
def add_new( user:tuple ) -> None:
    """Добавляет пользователя в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute( comand_add_user ,user)
    conn.commit()

def change_status(user:tuple) -> None:
    """Изменяет статус у пользователя (бан/не бан)"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_change_status_user, user )
    conn.commit()

def take_type_user(id_telegram: int) -> int:
    """Достает status пользователя из бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_take_type_user, (id_telegram, ), )
    res = curs.fetchone()
    conn.commit()
    return res[0]
      

def take( id_telegram: int ) -> list:
    """Достает пользователя из бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_take_user, (id_telegram, ), )
    conn.commit()
    res = curs.fetchone()
    print("aaa", res)
    return res


def check( id_telegram):
    """Проверяет есть ли пользователь в бд"""
    conn = bd.conn
    curs = conn.cursor()
    curs.execute(comand_check_user, (id_telegram, ), )
    # curs.execute(
    #     """SELECT * FROM users WHERE id_telegram = %s""",
    #     (int(id_telegram)),
    # )
    conn.commit()
    res = curs.fetchall()
    # print(len(res))
    return len(res)
