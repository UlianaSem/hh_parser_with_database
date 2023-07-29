-- создаем базу данных
CREATE DATABASE hh_vacancies;

-- создаем таблицу employers
CREATE TABLE employers
(
	employer_id SERIAL,
	employer_name VARCHAR(50) NOT NULL,
	employer_url VARCHAR(30) NOT NULL,
	region VARCHAR(30) NOT NULL,
	hh_id VARCHAR(15) NOT NULL,
	hh_url VARCHAR(30) NOT NULL,

	CONSTRAINT pk_employers_employer_id PRIMARY KEY (employer_id)
);

-- создаем таблицу currencies
CREATE TABLE currencies
(
	currency_id SERIAL,
	currency_name VARCHAR(10) NOT NULL,

	CONSTRAINT pk_currencies_currency_id PRIMARY KEY (currency_id)
);

-- заполняем таблицу currencies
INSERT INTO currencies(currency_name) VALUES
('AZN'),
('BYR'),
('EUR'),
('GEL'),
('KGS'),
('KZT'),
('RUR'),
('UAH'),
('USD'),
('UZS')

-- создаем таблицу vacancies
CREATE TABLE vacancies
(
	vacancy_id SERIAL,
	employer_id INT,
	vacancy_name VARCHAR(60) NOT NULL,
	salary_from INT,
	salary_to INT,
	currency_id INT,
	vacancy_url VARCHAR(30) NOT NULL,
	address VARCHAR(70),
	requirements TEXT,

	CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id),
	CONSTRAINT fk_vacancies_employers FOREIGN KEY (employer_id) REFERENCES employers(employer_id) ON DELETE CASCADE,
	CONSTRAINT fk_vacancies_currencies FOREIGN KEY (currency_id) REFERENCES currencies(currency_id) ON DELETE SET NULL
);

-- заполняем таблицу employers, (...) - данные, полученные по API
INSERT INTO employers(employer_name, employer_url, region, hh_id, hh_url) VALUES
(...)

-- заполняем таблицу vacancies, (...) - данные, полученные по API
INSERT INTO vacancies(vacancy_name, employer_id, salary_from, salary_to, currency_id, vacancy_url, address, requirements) VALUES
(...)
