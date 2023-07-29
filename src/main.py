import src.api
import utils
from src.config import config
from src.db_manager import DBManager

EMPLOYERS_IDS = ['41862', '3672566', '65068', '1723062', '67611', '1022259', '3542906', '3529', '1740', '78638',
                 '42600']
DATABASE_NAME = 'hh_vacancies'
TABLES = [
    {'table_name': 'employers', 'table_description': 'employer_id SERIAL,\nemployer_name VARCHAR(150) NOT NULL,\n'
                                                     'employer_url VARCHAR(150) NOT NULL,\nregion VARCHAR(90) NOT NULL,'
                                                     '\nhh_id VARCHAR(15) NOT NULL,\nhh_url VARCHAR(150) NOT NULL,\n'
                                                     'CONSTRAINT pk_employers_employer_id PRIMARY KEY (employer_id)'},
    {'table_name': 'currencies', 'table_description': 'currency_id SERIAL,\ncurrency_name VARCHAR(10) NOT NULL,\n'
                                                      'CONSTRAINT pk_currencies_currency_id PRIMARY KEY '
                                                      '(currency_id)'},
    {'table_name': 'vacancies', 'table_description': 'vacancy_id SERIAL,\nemployer_id INT,\n'
                                                     'vacancy_name VARCHAR(200) NOT NULL,\nsalary_from INT,\n'
                                                     'salary_to INT,\ncurrency_id INT,\nvacancy_url VARCHAR(150) '
                                                     'NOT NULL,\naddress VARCHAR(250),\nrequirements TEXT,\n'
                                                     'CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id),\n'
                                                     'CONSTRAINT fk_vacancies_employers FOREIGN KEY (employer_id) '
                                                     'REFERENCES employers(employer_id) ON DELETE CASCADE,\n'
                                                     'CONSTRAINT fk_vacancies_currencies FOREIGN KEY (currency_id) '
                                                     'REFERENCES currencies(currency_id) ON DELETE SET NULL'}
]
CURRENCIES = [{'currency_name': 'AZN'}, {'currency_name': 'BYR'}, {'currency_name': 'EUR'}, {'currency_name': 'GEL'},
              {'currency_name': 'KGS'}, {'currency_name': 'KZT'}, {'currency_name': 'RUR'}, {'currency_name': 'UAH'},
              {'currency_name': 'USD'}, {'currency_name': 'UZS'}]


def main():
    """
    Задает алгоритм работы программы
    """
    # создаем список для хранения экземпляров класса HeadHunterAPI
    employers = []

    # получаем данные по API и кладем в список
    for employer_id in EMPLOYERS_IDS:
        employers.append(src.api.HeadHunterAPI(employer_id))

    # получаем параметры для подключения к БД из файла
    params = config()

    # создаем базу данных
    utils.create_database(params, DATABASE_NAME)

    # добавляем название БД к параметрам подключения
    params.update({'dbname': DATABASE_NAME})

    # создаем таблицы БД
    for table in TABLES:
        utils.create_table(params, table['table_name'], table['table_description'])

    # заполняем таблицу currencies
    for currency in CURRENCIES:
        utils.add_data_to_table(params, TABLES[1]['table_name'], currency)

    # заполняем таблицы employers и vacancies
    for employer in employers:
        employer_id = utils.add_data_to_table(params, TABLES[0]['table_name'], employer.employer_info,
                                              'employer_id')

        for vacancy in employer.vacancies_data:
            vacancy['currency_id'] = utils.get_currency_id(params, vacancy.pop('currency'))
            vacancy['employer_id'] = employer_id

            utils.add_data_to_table(params, TABLES[2]['table_name'], vacancy)

    # создаем экземпляр класса для управления данными в БД
    manager = DBManager(params)

    while True:
        user_request = input("""Вы можете получить следующую информацию из БД:
1. список всех компаний и количество вакансий у каждой компании
2. список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
3. среднюю зарплату по вакансиям
4. список всех вакансий, у которых зарплата выше средней по всем вакансиям
5. список всех вакансий, в названии которых содержатся переданные в метод слова, например 'python'
        
Введите цифру интересующего вас запроса, для выхода введите 'exit'\n""").strip().lower()

        if user_request == '1':
            data = manager.get_companies_and_vacancies_count()

        elif user_request == '2':
            data = manager.get_all_vacancies()

        elif user_request == '3':
            data = int(manager.get_avg_salary())

        elif user_request == '4':
            data = manager.get_vacancies_with_higher_salary()

        elif user_request == '5':
            keyword = input('Введите слово для поиска\n').lower().strip()
            data = manager.get_vacancies_with_keyword(keyword)

        elif user_request == 'exit':
            return

        else:
            input('Вы ввели неверный запрос\n')
            break

        utils.build_answer(data)


if __name__ == '__main__':
    main()
