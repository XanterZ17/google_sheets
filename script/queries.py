from contextlib import closing

import psycopg2

from settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOSTNAME


def CreateTable():
    """Если таблицы не существует, создает ее"""   
    with closing(psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOSTNAME
        )) as connection:
        with connection.cursor() as cursor:
            query = '''
                    CREATE TABLE IF NOT EXISTS test(
                        id SERIAL PRIMARY KEY,
                        order_id VARCHAR(7) NOT NULL,
                        cost_usd INT NOT NULL,
                        date VARCHAR(10) NOT NULL,
                        cost_rub FLOAT NOT NULL
                    );
                    '''
            cursor.execute(query)
            connection.commit()

def GetTable() -> list:
    """Возвращает таблицу test из бд"""
    with closing(psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOSTNAME
        )) as connection:
        with connection.cursor() as cursor:
            query = '''
                SELECT * FROM test;
            '''
            cursor.execute(query)
            result = cursor.fetchall()
    return result


def UpdateTable(update_list: list):
    """Добавляет(или обвновляет) строки из update_list в бд"""
    with closing(psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOSTNAME
        )) as connection:
        with connection.cursor() as cursor:
            for row in update_list:
                id, order_id, cost_usd, date, cost_rub = row
                query = '''
                    INSERT INTO test (id, order_id, cost_usd, date, cost_rub)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (id)
                    DO UPDATE SET (id, order_id, cost_usd, date, cost_rub) = (%s, %s, %s, %s, %s);
                '''
                cursor.execute(query, (id, order_id, cost_usd, date, cost_rub, id, order_id, cost_usd, date, cost_rub))
        connection.commit()



def DeleteFromTable(delete_list: list):
    """Удаляет строки из delete_list из бд"""
    with closing(psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOSTNAME
        )) as connection:
        with connection.cursor() as cursor:
            query = '''
                DELETE FROM test
                WHERE id = %s;
            '''
            for row in delete_list:
                cursor.execute(query, (row[0],))
        connection.commit()
