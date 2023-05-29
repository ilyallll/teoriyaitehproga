import psycopg2


def create_database():
    """Функция для создания базы данных"""

    print("Введите название для новой базы данных")
    name = input()
    create_database_q = f"CREATE DATABASE {name};"
    cursor.execute(create_database_q)
    print(f"База данных {name} создана")
    return name


def drop_database(name):
    """Функция для удаления базы данных с заданным именем"""

    drop_database_q = f"DROP DATABASE {name};"
    cursor.execute(drop_database_q)
    print(f"База данных {name} удалена")

def show_databases():
    """Функция для отображения существующих баз данных"""

    show_databases_q = "SELECT datname FROM pg_database;"
    cursor.execute(show_databases_q)
    print(f"Существующие базы данных: {cursor.fetchall()}")

def show_table(name):
    """Функция для отображения данных из таблицы с заданным именем"""

    print(f"\nТаблица {name}")
    show_table_q = f"SELECT * FROM {name};"
    cursor.execute(show_table_q)
    for tuple in cursor.fetchall():
        print(tuple)
    print("\n")

def show_columns(name):
    """Функция для отображения столбцов таблицы с заданным именем"""

    show_columns_q = f"select column_name from information_schema.columns where table_name = '{name}' ;"
    cursor.execute(show_columns_q)
    print(f"Столбцы таблицы {name}:", cursor.fetchall())

def drop_table(name):
    drop_table_q = f"DROP TABLE {name};"
    cursor.execute(drop_table_q)
    print(f"Таблица {name} удалена")


# Подключение к существующей базе данных
try:
    connection = psycopg2.connect(
        user="postgres",
        password="000",
        host="127.0.0.1",
        port="5432",
        database="proga_test"
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        # Пример запроса на создание базы данных
        name_of_database = create_database()
        show_databases()
        # Пример запроса на создание таблицы
        create_table_exhibitions_q = "CREATE TABLE exhibitions (exhibition_id SERIAL PRIMARY KEY," \
                                   "name VARCHAR(50) NOT NULL, " \
                                   "duration TIME," \
                                   " age_limit SMALLINT CHECK (age_limit>=0));"
        cursor.execute(create_table_exhibitions_q)
        print("Таблица exhibitions создана")
        # Пример запроса на заполнение таблицы
        insert_exhibitions_q = "INSERT INTO exhibitions(name, duration, age_limit) " \
                             "VALUES ('The Pushkin', '1:50', 16), ('Our_predecessors', '2:30', 12), " \
                             "('The wonders of science', '1:10', 16), ('The World of animals', '1:30', 0);"
        cursor.execute(insert_exhibitions_q)
        print("Значения добавлены в таблицу exhibitions")
        # Показать результат заполнения
        show_table('exhibitions')
        # Пример запроса на обновление таблицы
        update_age_limit_exhibitions_q = "UPDATE exhibitions " \
                                       "SET age_limit = 14 " \
                                       "WHERE age_limit = 16;"
        cursor.execute(update_age_limit_exhibitions_q)
        print("Таблица exhibitions обновлена")
        # Показать результат обновления
        show_table('exhibitions')
        # Пример запроса на удаление данных
        delete_pushkin_q = "DELETE FROM exhibitions WHERE name = 'The Pushkin';"
        cursor.execute(delete_pushkin_q)
        print("Значения удалены из таблицы exhibitions")
        # Показать результат удаления
        show_table('exhibitions')
        # Создать новую таблицу
        create_table_sessions_q = "CREATE TABLE sessions" \
                                  "(session_id SERIAL PRIMARY KEY," \
                                  "date_of_session DATE NOT NULL," \
                                  "exhibition_id INT," \
                                  "FOREIGN KEY (exhibition_id) REFERENCES exhibitions (exhibition_id)" \
                                  "ON DELETE SET NULL);"
        cursor.execute(create_table_sessions_q)
        print("Таблица sessions создана")
        show_columns('sessions')
        alter_sessions_q = "ALTER TABLE sessions ADD COLUMN time_of_session TIME NOT NULL;"
        cursor.execute(alter_sessions_q)
        print("Таблица sessions изменена")
        # Показать результат изменения
        show_columns('sessions')
        # Заполнить sessions
        insert_sessions_q = "INSERT INTO sessions(date_of_session, time_of_session, exhibition_id) " \
                             "VALUES ('2023-03-23', '18:00', 4), ('2023-04-01', '21:30', 4), " \
                             "('2023-04-08', '19:00', 3), ('2023-04-11', '18:00', 2), " \
                          "('2023-06-06', '13:00', 4), ('2023-03-29', '13:30', 4);"
        cursor.execute(insert_sessions_q)
        print("Значения добавлены в таблицу sessions")
        # Показать результат заполнения
        show_table('sessions')
        # Пример запроса на объединение таблиц
        join_q = "SELECT ex.name, s.date_of_session, s.time_of_session " \
               "FROM exhibitions AS ex " \
               "JOIN sessions AS s " \
               "ON ex.exhibition_id = s.exhibition_id " \
               "WHERE ex.name = 'The World of animals'; "
        cursor.execute(join_q)
        print("Результат объединения двух таблиц")
        for tuple in cursor.fetchall():
            print(tuple)
        # Пример запроса на удаление таблицы
        drop_table('sessions')
        drop_table('exhibitions')
        # Пример запроса на удаление базы данных
        drop_database(name_of_database)
        show_databases()


except Exception as _ex:
    print("Ошибка при работе с PostgreSQL: ", _ex)
finally:
    if connection:
        connection.close()
        print("Соединение с PostgreSQL закрыто")
