import os
import sqlite3


DB = 'memsource.db'


def get_db_name(instance_path):
    return os.path.join(instance_path, DB)


def init_db(instance_path):
    with sqlite3.connect(get_db_name(instance_path)) as conn:
        try:
            cur = conn.cursor()
            cur.execute('DROP TABLE IF EXISTS memchess;')
            cur.execute('''
                CREATE TABLE memchess (
                    id TEXT PRIMARY KEY,
                    result TEXT
                );'''
            )
            conn.commit()
            print('DB initialized!')
        except:
            conn.rollback()


def insert_into_db(instance_path: str, id: str, value: str) -> None:
    with sqlite3.connect(get_db_name(instance_path)) as conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO memchess (id, result) VALUES (?, ?)", (id, value))
            conn.commit()
            print('Value inserted')
        except Exception as e:
            conn.rollback()
            print(e)


def update_db(instance_path: str, id: str, value: str) -> None:
    with sqlite3.connect(get_db_name(instance_path)) as conn:
        try:
            cur = conn.cursor()
            cur.execute("UPDATE memchess SET result=? WHERE id=?", (value, id))
            conn.commit()
            print('Value updated')
        except Exception as e:
            conn.rollback()
            print(e)


def get_result(instance_path: str, id: str) -> str:
    with sqlite3.connect(get_db_name(instance_path)) as conn:
        try:
            cur = conn.cursor()
            query = "SELECT result FROM memchess WHERE id=?"
            cur.execute(query, (id,))
            rows = cur.fetchall()
            print(rows)
            return rows[0][0]
        except Exception as e:
            conn.rollback()
            print(e)
