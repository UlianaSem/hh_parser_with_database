import pytest

import src.api


@pytest.fixture
def get_head_hunter_api_object():
    return src.api.HeadHunterAPI('3672566')


@pytest.fixture
def get_head_hunter_validator_object():
    return src.api.HeadHunterDataValidator()


def test_head_hunter_api(get_head_hunter_api_object):
    """
    Проверяет правильность url
    :param get_head_hunter_api_object: объект класса Head Hunter
    """
    assert get_head_hunter_api_object.employer_url == 'https://api.hh.ru/employers/3672566'
    assert get_head_hunter_api_object.vacancies_url == 'https://api.hh.ru/vacancies?employer_id=3672566'
    assert get_head_hunter_api_object.employer_info == {'employer_name': 'BRANDPOL',
                                                        'employer_url': 'http://brandpolgroup.com',
                                                        'region': 'Москва',
                                                        'hh_id': '3672566',
                                                        'hh_url': 'https://hh.ru/employer/3672566'}


# def test_get_employer_info(get_head_hunter_api_object):
#     """
#     Проверяет правильность получения данных о компании
#     :param get_head_hunter_api_object: объект класса Head Hunter
#     """
#     assert get_head_hunter_api_object.__get_employer_info()['id'] == '3672566'


# def test_get_vacancies(get_head_hunter_api_object):
#     """
#     Проверяет правильность получения данных о вакансиях
#     :param get_head_hunter_api_object: объект класса Head Hunter
#     """
#     assert get_head_hunter_api_object.get_vacancies('https://api.hh.ru/vacancies?employer_id=3672566'
#                                                     )[0]['employer']['id'] == '3672566'


def test_formate_vacancies_data(get_head_hunter_api_object):
    """
    Проверяет правильность форматирования данных о вакансиях
    :param get_head_hunter_api_object: объект класса Head Hunter
    """
    assert get_head_hunter_api_object.formate_vacancies_data(
        [{'id': '82524858', 'premium': False, 'name': 'Программист Python Junior (BigData)', 'department': None,
          'has_test': False, 'response_letter_required': False,
          'area': {'id': '3', 'name': 'Екатеринбург', 'url': 'https://api.hh.ru/areas/3'},
          'salary': {'from': 45000, 'to': 100000, 'currency': 'RUR', 'gross': True},
          'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
          'sort_point_distance': None,
          'published_at': '2023-07-21T11:27:38+0300', 'created_at': '2023-07-21T11:27:38+0300', 'archived': False,
          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=82524858',
          'insider_interview': None,
          'url': 'https://api.hh.ru/vacancies/82524858?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/82524858',
          'relations': [],
          'employer': {'id': '3672566', 'name': 'BRANDPOL', 'url': 'https://api.hh.ru/employers/3672566',
                       'alternate_url': 'https://hh.ru/employer/3672566',
                       'logo_urls': {'original': 'https://hhcdn.ru/employer-logo-original/1022054.png',
                                     '240': 'https://hhcdn.ru/employer-logo/5708985.png',
                                     '90': 'https://hhcdn.ru/employer-logo/5708984.png'},
                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3672566',
                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                'requirement': 'Уверенное использование Python. Знание базовых структур данных и алгоритмов, способно'
                               'сть оценивать скорость работы алгоритмов. Умение вникать в большие объемы кода. ',
                'responsibility': 'Обеспечивать работоспособность и доступность бизнес-систем компании. Управлять конф'
                                  'игурациями и микросервисами. Находить не тривиальные решения. Быть "белыми хакерам'
                                  'и" всегда решать...'},
          'contacts': None, 'schedule': None, 'working_days': [], 'working_time_intervals': [],
          'working_time_modes': [],
          'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
          'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False},
         {'id': '83644453', 'premium': False, 'name': 'Аналитик данных', 'department': None, 'has_test': False,
          'response_letter_required': False,
          'area': {'id': '3', 'name': 'Екатеринбург', 'url': 'https://api.hh.ru/areas/3'},
          'salary': {'from': 40000, 'to': 80000, 'currency': 'RUR', 'gross': True},
          'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
          'sort_point_distance': None,
          'published_at': '2023-07-21T17:41:15+0300', 'created_at': '2023-07-21T17:41:15+0300', 'archived': False,
          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=83644453',
          'insider_interview': None,
          'url': 'https://api.hh.ru/vacancies/83644453?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/83644453',
          'relations': [],
          'employer': {'id': '3672566', 'name': 'BRANDPOL', 'url': 'https://api.hh.ru/employers/3672566',
                       'alternate_url': 'https://hh.ru/employer/3672566',
                       'logo_urls': {'original': 'https://hhcdn.ru/employer-logo-original/1022054.png',
                                     '240': 'https://hhcdn.ru/employer-logo/5708985.png',
                                     '90': 'https://hhcdn.ru/employer-logo/5708984.png'},
                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3672566',
                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
             'requirement': 'Знание Excel. Знание и понимание из чего состоит веб-страница (HTML, CSS, JS). Умение по'
                            'нять какую задачу, каким инструментом решить...',
             'responsibility': 'Исследование рынка, поиск фактов незаконного использования товарных знаков и других н'
                               'арушений. Поиск, сбор и анализ информации на веб-ресурсах (мониторинг...'},
          'contacts': None, 'schedule': None, 'working_days': [], 'working_time_intervals': [],
          'working_time_modes': [],
          'accept_temporary': False, 'professional_roles': [{'id': '10', 'name': 'Аналитик'}],
          'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False},
         {'id': '83644681', 'premium': False, 'name': 'Оператор ПК', 'department': None, 'has_test': False,
          'response_letter_required': False,
          'area': {'id': '3', 'name': 'Екатеринбург', 'url': 'https://api.hh.ru/areas/3'},
          'salary': {'from': 30000, 'to': 50000, 'currency': 'RUR', 'gross': False},
          'type': {'id': 'open', 'name': 'Открытая'},
          'address': {'city': 'Екатеринбург', 'street': 'улица Энгельса', 'building': '36', 'lat': 56.834038,
                      'lng': 60.621792, 'description': None, 'raw': 'Екатеринбург, улица Энгельса, 36',
                      'metro': {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
                                'line_id': '48', 'lat': 56.837982, 'lng': 60.59734}, 'metro_stations': [
                  {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
                   'line_id': '48',
                   'lat': 56.837982, 'lng': 60.59734}], 'id': '6154316'}, 'response_url': None,
          'sort_point_distance': None,
          'published_at': '2023-07-21T17:47:41+0300', 'created_at': '2023-07-21T17:47:41+0300', 'archived': False,
          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=83644681',
          'insider_interview': None,
          'url': 'https://api.hh.ru/vacancies/83644681?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/83644681',
          'relations': [],
          'employer': {'id': '3672566', 'name': 'BRANDPOL', 'url': 'https://api.hh.ru/employers/3672566',
                       'alternate_url': 'https://hh.ru/employer/3672566',
                       'logo_urls': {'original': 'https://hhcdn.ru/employer-logo-original/1022054.png',
                                     '240': 'https://hhcdn.ru/employer-logo/5708985.png',
                                     '90': 'https://hhcdn.ru/employer-logo/5708984.png'},
                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3672566',
                       'accredited_it_employer': False, 'trusted': True},
          'snippet': {'requirement': 'Знание Excel. Усидчивость. Внимательность.',
                      'responsibility': 'Поиск, сбор и анализ информации на веб-ресурсах (мониторинг Интернета). Выпо'
                                        'лнение задач старших аналитиков по сбору и проверке уже собранных...'},
          'contacts': None, 'schedule': None, 'working_days': [], 'working_time_intervals': [],
          'working_time_modes': [],
          'accept_temporary': False, 'professional_roles': [{'id': '84', 'name': 'Оператор ПК, оператор базы данных'}],
          'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'probation', 'name': 'Стажировка'}, 'adv_response_url': None, 'is_adv_vacancy': False},
         {'id': '83531022', 'premium': False, 'name': 'Менеджер по развитию бизнеса B2B (Европейский рынок)',
          'department': None, 'has_test': False, 'response_letter_required': False,
          'area': {'id': '3', 'name': 'Екатеринбург', 'url': 'https://api.hh.ru/areas/3'},
          'salary': {'from': 60000, 'to': 200000, 'currency': 'RUR', 'gross': False},
          'type': {'id': 'open', 'name': 'Открытая'},
          'address': {'city': 'Екатеринбург', 'street': 'улица Энгельса', 'building': '36', 'lat': 56.834038,
                      'lng': 60.621792, 'description': None, 'raw': 'Екатеринбург, улица Энгельса, 36',
                      'metro': {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
                                'line_id': '48', 'lat': 56.837982, 'lng': 60.59734}, 'metro_stations': [
                  {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
                   'line_id': '48',
                   'lat': 56.837982, 'lng': 60.59734}], 'id': '6154316'}, 'response_url': None,
          'sort_point_distance': None,
          'published_at': '2023-07-20T10:35:16+0300', 'created_at': '2023-07-20T10:35:16+0300', 'archived': False,
          'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=83531022',
          'insider_interview': None,
          'url': 'https://api.hh.ru/vacancies/83531022?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/83531022',
          'relations': [],
          'employer': {'id': '3672566', 'name': 'BRANDPOL', 'url': 'https://api.hh.ru/employers/3672566',
                       'alternate_url': 'https://hh.ru/employer/3672566',
                       'logo_urls': {'original': 'https://hhcdn.ru/employer-logo-original/1022054.png',
                                     '240': 'https://hhcdn.ru/employer-logo/5708985.png',
                                     '90': 'https://hhcdn.ru/employer-logo/5708984.png'},
                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3672566',
                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
             'requirement': 'Наличие успешного опыта личных продаж/назначения встреч/ведения переговоров/сопровождени'
                            'я клиентов до сделки. - Опыт работы от 1 года. - ',
             'responsibility': 'Работа с существующей клиентской базой, работа на входящем потоке. - Поиск и привлечен'
                               'ие новых клиентов в странах Европейского союза. - '},
          'contacts': None, 'schedule': None, 'working_days': [], 'working_time_intervals': [],
          'working_time_modes': [],
          'accept_temporary': False,
          'professional_roles': [{'id': '70', 'name': 'Менеджер по продажам, менеджер по работе с клиентами'}],
          'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
          'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False}])


def test_formate_employer_data(get_head_hunter_api_object):
    """
    Проверяет правильность форматирования данных о работодателе
    :param get_head_hunter_api_object: объект класса Head Hunter
    """
    assert get_head_hunter_api_object.formate_employer_data(
        {'id': '3672566', 'trusted': True, 'accredited_it_employer': False, 'name': 'BRANDPOL', 'type': 'company',
         'description': '<p><em><strong>Мы – международная аккредитованная IT компания, которая работает на рынке 20'
                        ' лет, ежедневно создаем уникальный продукт , призванный защищать потребителей и производител'
                        'ей товаров и услуг по всему миру на всех языках и на всех интернет-площадках. Мы создаем совер'
                        'шенно новый цифровой поход для обеспечения экономических интересов производителей и потреби'
                        'телей по всему миру, на базе собственной разработки онлайн-платформы BRANDPOL.</strong></em><'
                        '/p> <p><em><strong>Сайт проекта: brandpolgroup.com</strong></em></p> <p><em><strong>Основные'
                        ' клиенты - корпоративные компании- производители, а также крупные дистрибьютеры.</strong></em'
                        '></p> <p><em><strong>Ключевые продукты: защита интеллектуальной собственности в интернете, мо'
                        'ниторинг цен, управление репутацией в интернете.</strong></em></p> <p><em><strong>Наши сильны'
                        'е стороны: офисы в России и Болгарии. Наша платформа для проведения анализа рынка. Стабильная'
                        ' команда. Оцифрованные процессы продажи и ведения проектов в Битрикс24.</strong></em></p>',
         'site_url': 'http://brandpolgroup.com', 'alternate_url': 'https://hh.ru/employer/3672566',
         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3672566',
         'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/5708985.png',
                       'original': 'https://hhcdn.ru/employer-logo-original/1022054.png',
                       '90': 'https://hhcdn.ru/employer-logo/5708984.png'}, 'relations': [],
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'industries': [{'id': '7.541',
                                                                                                    'name': 'Интернет-'
                                                                                                            'компания '
                                                                                                            '(поискови'
                                                                                                            'ки, плате'
                                                                                                            'жные сист'
                                                                                                            'емы, соц.'
                                                                                                            'сети, инфо'
                                                                                                            'рмационно-'
                                                                                                            'познавател'
                                                                                                            'ьные и раз'
                                                                                                            'влекатель'
                                                                                                            'ные ресурс'
                                                                                                            'ы, продвиж'
                                                                                                            'ение сайто'
                                                                                                            'в и проче'
                                                                                                            'е)'},
                                                                                                   {'id': '7.540',
                                                                                                    'name': 'Разработка'
                                                                                                            ' программ'
                                                                                                            'ного обесп'
                                                                                                            'ечения'},
                                                                                                   {'id': '7.539',
                                                                                                    'name': 'Системная'
                                                                                                            ' интеграц'
                                                                                                            'ия,  авто'
                                                                                                            'матизации'
                                                                                                            ' технологи'
                                                                                                            'ческих и б'
                                                                                                            'изнес-про'
                                                                                                            'цессов пре'
                                                                                                            'дприятия, '
                                                                                                            'ИТ-консалт'
                                                                                                            'инг'}],
         'branded_description': None, 'branding': None, 'insider_interviews': [], 'open_vacancies': 4})


def test_validate_salary(get_head_hunter_validator_object):
    """
    Проверяет правильность проверки данных о зарплате
    :param get_head_hunter_validator_object: объект класса HeadHunterDataValidator
    """
    assert get_head_hunter_validator_object.validate_salary({'from': 60000, 'to': 200000, 'currency': 'RUR',
                                                             'gross': False}) == (60000, 200000, 'RUR')
    assert get_head_hunter_validator_object.validate_salary({'from': None, 'to': None, 'currency': 'RUR',
                                                             'gross': False}) == (None, None, 'RUR')
    assert get_head_hunter_validator_object.validate_salary({'from': 60000, 'to': 200000, 'currency': None,
                                                             'gross': False}) == (60000, 200000, None)
    assert get_head_hunter_validator_object.validate_salary({'from': None, 'to': 200000,
                                                             'gross': False}) == (None, 200000, None)


def test_validate_vacancy_requirement(get_head_hunter_validator_object):
    """
    Проверяет правильность проверки данных об описании вакансии
    :param get_head_hunter_validator_object: объект класса HeadHunterDataValidator
    """
    assert get_head_hunter_validator_object.validate_vacancy_requirement({
        'requirement': 'Знание Excel. Знание и понимание из чего состоит веб-страница (HTML, CSS, JS). Умение по'
                       'нять какую задачу, каким инструментом решить...',
        'responsibility': 'Исследование рынка, поиск фактов незаконного использования товарных знаков и других н'
                          'арушений. Поиск, сбор и анализ информации на веб-ресурсах (мониторинг...'}) == 'Знание Exc' \
                                                                                                          'el. Знание' \
                                                                                                          ' и пониман' \
                                                                                                          'ие из чего' \
                                                                                                          ' состоит в' \
                                                                                                          'еб-страниц' \
                                                                                                          'а (HTML, C' \
                                                                                                          'SS, JS). У' \
                                                                                                          'мение пон' \
                                                                                                          'ять какую ' \
                                                                                                          'задачу, ка' \
                                                                                                          'ким инстру' \
                                                                                                          'ментом реш' \
                                                                                                          'ить...\nИс' \
                                                                                                          'следование' \
                                                                                                          ' рынка, по' \
                                                                                                          'иск фактов' \
                                                                                                          ' незаконно' \
                                                                                                          'го использ' \
                                                                                                          'ования тов' \
                                                                                                          'арных знак' \
                                                                                                          'ов и други' \
                                                                                                          'х нарушени' \
                                                                                                          'й. Поиск,' \
                                                                                                          ' сбор и ан' \
                                                                                                          'ализ инфор' \
                                                                                                          'мации на в' \
                                                                                                          'еб-ресурса' \
                                                                                                          'х (монитор' \
                                                                                                          'инг...'
    assert get_head_hunter_validator_object.validate_vacancy_requirement({'requirement': 'Знание Excel. Знание и поним'
                                                                                         'ание из чего состоит веб-стр'
                                                                                         'аница (HTML, CSS, JS). Уме'
                                                                                         'ние понять какую задачу, как'
                                                                                         'им инструментом решить...',
                                                                          'responsibility': None}) == 'Знание Excel. ' \
                                                                                                      'Знание и поним' \
                                                                                                      'ание из чего с' \
                                                                                                      'остоит веб-стр' \
                                                                                                      'аница (HTML, C' \
                                                                                                      'SS, JS). Умени' \
                                                                                                      'е понять какую' \
                                                                                                      ' задачу, каким' \
                                                                                                      ' инструментом ' \
                                                                                                      'решить...'
    assert get_head_hunter_validator_object.validate_vacancy_requirement({'requirement': None,
                                                                          'responsibility': 'Исследование рынка, поиск '
                                                                                            'фактов незаконного исполь'
                                                                                            'зования товарных знаков и'
                                                                                            ' других нарушений. Поиск, '
                                                                                            'сбор и анализ информации'
                                                                                            ' на веб-ресурсах (монитори'
                                                                                            'нг...'}) == 'Исследован' \
                                                                                                         'ие рынка, п' \
                                                                                                         'оиск фактов' \
                                                                                                         ' незаконно' \
                                                                                                         'го использо' \
                                                                                                         'вания товар' \
                                                                                                         'ных знаков ' \
                                                                                                         'и других на' \
                                                                                                         'рушений. По' \
                                                                                                         'иск, сбор и' \
                                                                                                         ' анализ инф' \
                                                                                                         'ормации на ' \
                                                                                                         'веб-ресурс' \
                                                                                                         'ах (монитор' \
                                                                                                         'инг...'


def test_validate_address(get_head_hunter_validator_object):
    """
    Проверяет правильность проверки данных об адресе
    :param get_head_hunter_validator_object: объект класса HeadHunterDataValidator
    """
    assert get_head_hunter_validator_object.validate_address({'city': 'Екатеринбург', 'street': 'улица Энгельса',
                                                              'building': '36', 'lat': 56.834038,
                                                              'lng': 60.621792, 'description': None,
                                                              'raw': 'Екатеринбург, улица Энгельса, 36',
                                                              'metro': {'station_name': 'Площадь 1905 года',
                                                                        'line_name': 'Север-Юг', 'station_id': '48.266',
                                                                        'line_id': '48', 'lat': 56.837982,
                                                                        'lng': 60.59734}, 'metro_stations': [
            {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
             'line_id': '48',
             'lat': 56.837982, 'lng': 60.59734}], 'id': '6154316'}) == 'Екатеринбург, улица Энгельса, 36'
    assert get_head_hunter_validator_object.validate_address({'city': 'Екатеринбург', 'street': 'улица Энгельса',
                                                              'building': '36', 'lat': 56.834038,
                                                              'lng': 60.621792, 'description': None,
                                                              'raw': None,
                                                              'metro': {'station_name': 'Площадь 1905 года',
                                                                        'line_name': 'Север-Юг', 'station_id': '48.266',
                                                                        'line_id': '48', 'lat': 56.837982,
                                                                        'lng': 60.59734}, 'metro_stations': [
            {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
             'line_id': '48',
             'lat': 56.837982, 'lng': 60.59734}], 'id': '6154316'}) == 'Екатеринбург, улица Энгельса, 36'
    assert get_head_hunter_validator_object.validate_address({'city': 'Екатеринбург', 'street': None,
                                                              'building': None, 'lat': 56.834038,
                                                              'lng': 60.621792, 'description': None,
                                                              'raw': None,
                                                              'metro': {'station_name': 'Площадь 1905 года',
                                                                        'line_name': 'Север-Юг', 'station_id': '48.266',
                                                                        'line_id': '48', 'lat': 56.837982,
                                                                        'lng': 60.59734}, 'metro_stations': [
            {'station_name': 'Площадь 1905 года', 'line_name': 'Север-Юг', 'station_id': '48.266',
             'line_id': '48',
             'lat': 56.837982, 'lng': 60.59734}], 'id': '6154316'}) == 'Екатеринбург'
