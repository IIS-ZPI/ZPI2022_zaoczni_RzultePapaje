from datetime import timedelta, date
import psycopg2
import requests
import configparser


def data_import():
	tables = ['A', 'B']
	data_table = []

	conn = connect_to_db()
	for table_type in tables:
		url_date_start = date(2023, 1, 2)
		url_date_end = url_date_start + timedelta(days=93)
		print("Tabela", table_type)
		while True:
			if url_date_end > date.today():
				url_date_end = date.today()
			if url_date_start == date.today():
				break
			resp = get_data(table_type, url_date_start, url_date_end)
			for x in resp:
				data_table.append(x)
			insert_table = create_inserts(data_table, table_type)
			execute_inserts(conn, insert_table)
			data_table.clear()
			url_date_start = url_date_end
			url_date_end = url_date_start + timedelta(days=93)

	conn.close()


def create_url(url_type, url_date_start, url_date_end):
	url_table_a = 'http://api.nbp.pl/api/exchangerates/tables/A/'
	url_table_b = 'http://api.nbp.pl/api/exchangerates/tables/B/'
	url_table_c = 'http://api.nbp.pl/api/exchangerates/tables/C/'

	if url_type == 'A':
		return url_table_a + str(url_date_start) + '/' + str(url_date_end)
	if url_type == 'B':
		return url_table_b + str(url_date_start) + '/' + str(url_date_end)
	if url_type == 'C':
		return url_table_c + str(url_date_start) + '/' + str(url_date_end)


def create_inserts(data_table, table_type):
	insert_start = "INSERT INTO tabela_" + table_type.lower() + " values(default,'"
	insert_table = []
	tmp = []
	no = 'no'
	effective_date = 'effectiveDate'
	for line in data_table:
		insert_command = insert_start + line[no] + "','" + line[effective_date] + "'"
		for x in line['rates']:
			insert_multiple_values = insert_command + ",'" + x['code'] + "'," + str(x['mid']) + ");"
			tmp.append(insert_multiple_values)
		insert_table.append(tmp)
		tmp = []
	return insert_table


def get_data(url_type, url_date_start, url_date_end):
	return requests.get(create_url(url_type, url_date_start, url_date_end)).json()


def connect_to_db():
	config = parse_config()
	return psycopg2.connect(
		host=config['DATABASE']['Host'],
		dbname=config['DATABASE']['Name'],
		user=config['DATABASE']['Username'],
		password=config['DATABASE']['Password'])


def execute_inserts(conn, insert_table):
	cur = conn.cursor()
	for inserts in insert_table:
		for insert in inserts:
			cur.execute(insert)
		conn.commit()
	cur.close()


def parse_config():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config


if __name__ == '__main__':
	data_import()
