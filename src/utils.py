import psycopg2


def create_database(params, database_name: str):
    """
    Создает базу данных
    :param params: параметры для подключения к базе данных
    :param database_name: название базы данных
    """
    connection = psycopg2.connect(database='postgres', **params)
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(f'DROP DATABASE {database_name}')
        cursor.execute(f'CREATE DATABASE {database_name}')

    connection.close()


def create_table(params, table_name, table_description: str):
    """
    Создает таблицу в БД
    :param params: параметры для подключения к базе данных
    :param table_name: название таблицы
    :param table_description: описание таблицы
    """
    with psycopg2.connect(**params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_description})')


def add_data_to_table(params, table_name, data: dict, for_return=''):
    """
    Заполняет таблицу
    :param for_return: название колонки для возвращения
    :param params: параметры для подключения к базе данных
    :param table_name: название таблицы
    :param data: данные для заполнения
    """
    column_number = len(data)
    s_string = ', '.join(['%s'] * column_number)
    column_string = ', '.join([x for x in data.keys()])

    if for_return == '':
        returning = ''
    else:
        returning = f'\nRETURNING {for_return}'

    request_string = 'INSERT INTO ' + table_name + '(' + column_string + ') VALUES (' + s_string + ')' + returning

    with psycopg2.connect(**params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(request_string, tuple(data.values()))

            if returning != '':
                id_ = cursor.fetchone()[0]

                return id_


def get_currency_id(params, currency: str):
    """
    Возвращает currency_id из таблицы currencies
    :param params: параметры для подключения к базе данных
    :param currency: название валюты
    :return: currency_id валюты
    """
    if currency is None:
        return None

    with psycopg2.connect(**params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT currency_id FROM currencies WHERE currency_name = '{currency}'")

            currency_id = cursor.fetchone()[0]

    return currency_id


def build_answer(data):
    """
    Строит ответ для пользователя
    :param data: запрашиваемые данные
    """
    if isinstance(data, int):
        print('Средняя зарплата по вакансиям:', data)

    else:
        for line in data:
            for key, value in line.items():
                print(f"{key}: {value}", end=' | ')

            print('')
