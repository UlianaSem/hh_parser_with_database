import psycopg2


class DBManager:
    """
    Класс для работы с базой данных
    """
    def __init__(self, params):
        """
        Инициализирует экземпляр класса DBManager
        :param params: параметры для подключения к базе данных
        """
        self.connection = psycopg2.connect(**params)
        self.cursor = self.connection.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        :return: список словарей с компаниями
        """
        with self.connection:
            self.cursor.execute(f'''SELECT employer_name, COUNT(*) FROM employers
            LEFT JOIN vacancies USING (employer_id)
            GROUP BY vacancies.employer_id, employer_name
            ORDER BY employer_name''')

            data = self.cursor.fetchall()
            data_for_return = [{'employer_name': line[0], 'vacancies_number': line[1]} for line in data]

            return data_for_return

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        :return: список словарей с вакансиями
        """
        with self.connection:
            self.cursor.execute(f'''
            SELECT employer_name, vacancy_name, salary_from, salary_to, vacancy_url FROM employers
            JOIN vacancies USING (employer_id)
            ORDER BY employer_name, vacancy_name''')

            data = self.cursor.fetchall()
            data_for_return = [{'employer_name': line[0], 'vacancy_name': line[1], 'salary_from': line[2],
                                'salary_to': line[3], 'vacancy_url': line[4]} for line in data]

            return data_for_return

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        :return: средняя зарплата
        """
        with self.connection:
            self.cursor.execute(f'''SELECT ROUND(AVG(salary_to)) FROM vacancies''')

            avg_salary = self.cursor.fetchone()[0]

            return avg_salary

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        :return: список словарей с вакансиями
        """
        with self.connection:
            self.cursor.execute(f'''SELECT employer_name, vacancy_name, salary_from, vacancy_url FROM employers
            JOIN vacancies USING (employer_id)
            WHERE salary_from >= (
            SELECT ROUND(AVG(salary_to))
            FROM vacancies
            )
            ORDER BY employer_name, vacancy_name''')

            data = self.cursor.fetchall()
            data_for_return = [{'employer_name': line[0], 'vacancy_name': line[1], 'salary_from': line[2],
                                'vacancy_url': line[3]} for line in data]

            return data_for_return

    def get_vacancies_with_keyword(self, keyword: str):
        """
        Получает список всех вакансий, в названии которых содержатся ключевое слово
        :param keyword: ключевое слово
        :return: список словарей с вакансиями
        """
        keyword = keyword.strip().lower()

        with self.connection:
            self.cursor.execute(f'''SELECT employer_name, vacancy_name, salary_from, vacancy_url FROM employers
            JOIN vacancies USING (employer_id)
            WHERE LOWER(vacancy_name) LIKE '%{keyword}%'
            ORDER BY employer_name, vacancy_name''')

            data = self.cursor.fetchall()
            data_for_return = [{'employer_name': line[0], 'vacancy_name': line[1], 'salary_from': line[2],
                                'vacancy_url': line[3]} for line in data]

            return data_for_return
