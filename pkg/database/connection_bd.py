
import psycopg2 as psql

import logging
from pkg.config.config import CONFIG_BD

class BD_conn():
    def __init__(self, cnf: CONFIG_BD):
        try:
            with psql.connect(
                user=cnf["user"],  
                password=cnf["password"],
                database=cnf["database"], 
                host=cnf["host"], 
                port=cnf["port"] 
                )as conn:

                self.conn = conn
        except Exception as ex:
            print("Connection refused...")
            print(ex)
        
