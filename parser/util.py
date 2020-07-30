import config
import pymysql


def connection(func):

    def wrapper(*args, **kwargs):
        connect = pymysql.Connect(**config.connect)
        cursor = connect.cursor()
        func(cursor, connect, *args, **kwargs)
        connect.close()

    return wrapper


@connection
def insert_in_db(cursor, connect, date, title, data):
    cursor.execute('SELECT `title_of_new` '
                   'FROM backend_news '
                   f'WHERE `title_of_new` = "{title}"')
    if not cursor.fetchall():
        cursor.execute('INSERT INTO backend_news (`title_of_new`, `description_of_new`, `date_of_new`) '
                       f'VALUES ("{title}", "{data}", "{date}")')
        connect.commit()

