import psycopg2
from pony.orm import *



db = Database()

class Exhibitions(db.Entity):
    """Класс, определяющий таблицу exhibitions, атрибуты класса соответствуют атрибутам таблицы"""

    exhibition_id = PrimaryKey(int, auto=True)
    name = Required(str)
    duration = Optional(str)
    age_limit = Optional(int)

class Sessions(db.Entity):
    """Класс, определяющий таблицу sessions, атрибуты класса соответствуют атрибутам таблицы"""

    session_id = PrimaryKey(int, auto=True)
    date_of_session = Required(date)
    time_of_session = Required(time)
    exhibition = Optional(Exhibitions)

db.bind(provider='postgres', user='postgres', password='000', host='127.0.0.1', port=5432, database='basatest')
db.generate_mapping(create_tables=True)


@db_session
def exhibitions_show():
    """Функция запроса для вывода данных из таблицы exhibitions"""

    print("\nТаблица exhibitions:\n")
    exhibitions_show = select(e for e in Exhibitions)[:]
    for exhibition in exhibitions_show:
        print(exhibition.to_dict())
    print("\n")


@db_session
def sessions_show():
    """Функция запроса для вывода данных из таблицы sessions"""

    print("\nТаблица sessions:\n")
    sessions_show = select(s for s in Sessions)[:]
    for session in sessions_show:
        print(session.to_dict())
    print("\n")


@db_session
def main():
    # Пример запроса на заполнение таблицы exhibitions
    exhibitions_data = [
        {'name': 'Art Exhibition', 'duration': '2:00', 'age_limit': 18},
        {'name': 'Historical Display', 'duration': '1:30', 'age_limit': 12},
        {'name': 'Science Expo', 'duration': '1:45', 'age_limit': 16},
        {'name': 'Nature Showcase', 'duration': '1:15', 'age_limit': 0}
    ]
    Exhibitions(**exhibitions_data)

    print("Значения добавлены в таблицу exhibitions")
    exhibitions_show()

    # Пример запроса на обновление таблицы exhibitions
    Exhibitions.get(name='Science Expo').age_limit = 14
    commit()

    print("Таблица exhibitions обновлена")
    exhibitions_show()

    # Пример запроса на удаление данных
    Exhibitions.get(name='Art Exhibition').delete()
    commit()

    print("Значения удалены из таблицы exhibitions")
    exhibitions_show()

    # Пример запроса на заполнение таблицы sessions
    sessions_data = [
        {'date_of_session': date(2023, 3, 23), 'time_of_session': time(18, 0), 'exhibition': 4},
        {'date_of_session': date(2023, 4, 1), 'time_of_session': time(21, 30), 'exhibition': 4},
        {'date_of_session': date(2023, 4, 8), 'time_of_session': time(19, 0), 'exhibition': 3},
        {'date_of_session': date(2023, 4, 11), 'time_of_session': time(18, 0), 'exhibition': 2},
        {'date_of_session': date(2023, 6, 6), 'time_of_session': time(13, 0), 'exhibition': 4},
        {'date_of_session': date(2023, 3, 29), 'time_of_session': time(13, 30), 'exhibition': 4}
    ]
    Sessions(**sessions_data)

    print("Значения добавлены в таблицу sessions")
    sessions_show()

    # Пример запроса на объединение таблиц
    join_q = select((e.name, s.date_of_session, s.time_of_session)
                    for e in Exhibitions
                    for s in e.sessions
                    if e.name == 'Nature Showcase')[:]
    print("\nРезультат объединения двух таблиц\n")
    for tuple in join_q:
        print(tuple)

    # Удаление таблиц
    db.drop_all_tables(with_all_data=True)


if __name__ == '__main__':
    main()
