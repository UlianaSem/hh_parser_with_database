from abc import ABC, abstractmethod

import requests


class HeadHunterAPI:
    """
    Класс для работы с API сайта HeadHunter
    """

    def __init__(self, employer_id: str):
        """
        Инициализирует экземпляр класса HeadHunter
        :param employer_id: идентификатор работодателя
        """
        self.employer_url = 'https://api.hh.ru/employers/' + employer_id.strip()

        employer_row_data = self.__get_employer_info()

        self.vacancies_url = employer_row_data['vacancies_url']
        self.__employer_info = self.formate_employer_data(employer_row_data)

        vacancies_row_data = self.__get_vacancies()

        self.__vacancies_data = self.formate_vacancies_data(vacancies_row_data)

    def __get_employer_info(self):
        """
        Получает и возвращает словарь с данными о вакансиях
        :return: словарь с данными о вакансиях
        """
        employer_data = requests.get(self.employer_url).json()

        return employer_data

    def __get_vacancies(self):
        """
        Получает и возвращает словарь с данными о вакансиях
        :return: словарь с данными о вакансиях
        """
        vacancies_data = requests.get(self.vacancies_url).json()

        return vacancies_data['items']

    @property
    def employer_info(self):
        return self.__employer_info

    @property
    def vacancies_data(self):
        return self.__vacancies_data

    @staticmethod
    def formate_vacancies_data(vacancies: list):
        """
        Возвращает данные о вакансиях в требуемом формате
        :return: список словарей с данными о вакансиях
        """
        vacancies_for_return = []

        validator = HeadHunterDataValidator()

        for vacancy in vacancies:
            profession = vacancy['name']
            address = validator.validate_address(vacancy['address'])
            salary_from, salary_to, currency = validator.validate_salary(vacancy['salary'])
            requirement = validator.validate_vacancy_requirement(vacancy['snippet'])
            url = vacancy['alternate_url']

            vacancies_for_return.append({'vacancy_name': profession,
                                         'salary_from': salary_from,
                                         'salary_to': salary_to,
                                         'currency': currency,
                                         'vacancy_url': url,
                                         'address': address,
                                         'requirements': requirement
                                         })

        return vacancies_for_return

    @staticmethod
    def formate_employer_data(employer: dict):
        """
        Возвращает данные о работодателе в требуемом формате
        :return: словарей с данными о работодателе
        """
        name = employer['name']
        hh_id = employer['id']
        region = employer['area']['name']
        hh_url = employer['alternate_url']
        company_url = employer['site_url']

        return {'employer_name': name,
                'employer_url': company_url,
                'region': region,
                'hh_id': hh_id,
                'hh_url': hh_url}


class DataValidator(ABC):
    """
    Абстрактный класс для проверки данных добавляемых в класс Vacancy
    """

    @staticmethod
    @abstractmethod
    def validate_salary(salary, currency):
        """
        Абстрактный метод для проверки правильности формата зарплаты
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_address(address):
        """
        Абстрактный метод для проверки правильности формата адреса
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_vacancy_requirement(vacancy_requirement):
        """
        Абстрактный метод для проверки правильности формата требований к вакансии
        """
        pass


class HeadHunterDataValidator(DataValidator):
    """
    Класс для проверки данных добавляемых в класс Vacancy с платформы HeadHunter
    """

    @staticmethod
    def validate_salary(salary, currency=None):
        """
        Проверяет правильность формата зарплаты и возвращает в нужном формате
        :param salary: данные о зарплате
        :param currency: валюта
        :return: данные о зарплате
        """
        if salary is None:
            return None, None

        salary_from = salary['from']
        salary_to = salary['to']

        if salary_from is not None:
            salary_from = int(salary_from)

        if salary_to is not None:
            salary_to = int(salary_to)

        if salary.get('currency') is not None:
            currency = salary['currency']

        return salary_from, salary_to, currency

    @staticmethod
    def validate_address(address):
        """
        Проверяет правильность формата адреса и возвращает в нужном формате
        :param address: данные об адресе
        :return: данные об адресе в str
        """
        if address is None:
            return None

        if address['raw'] is not None:
            return address['raw']

        city, street, building = address['city'], address['street'], address['building']
        address_list = []

        if address['city'] is not None:
            address_list.append(city)

        if address['street'] is not None:
            address_list.append(street)

        if address['building'] is not None:
            address_list.append(building)

        return ', '.join(address_list)

    @staticmethod
    def validate_vacancy_requirement(vacancy_requirement):
        """
        Проверяет правильность формата требований и возвращает в нужном формате
        :param vacancy_requirement: данные об адресе
        :return: данные об адресе в str
        """
        if vacancy_requirement is None:
            return None

        requirement = vacancy_requirement['requirement']
        responsibility = vacancy_requirement['responsibility']
        requirements_list = []

        if requirement is not None:
            requirements_list.append(requirement)

        if responsibility is not None:
            requirements_list.append(responsibility)

        return '\n'.join(requirements_list)
