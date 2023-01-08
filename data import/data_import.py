from datetime import timedelta, date
import psycopg2
import requests


def data_import():
	# tables = ['A', 'B', 'C']
	tables = ['A']
	data_table = []
	insert_table = []
	for table in tables:
		resp = get_data(table)
		for x in resp:
			data_table.append(x)
		insert_table = create_inserts(data_table)
	conn = connect_to_db()
	execute_inserts(conn, insert_table)
	conn.close()


def create_url(url_type):
	# start_date = date(2002, 1, 2)
	url_table_a = 'http://api.nbp.pl/api/exchangerates/tables/A/'
	url_table_b = 'http://api.nbp.pl/api/exchangerates/tables/B/'
	url_table_c = 'http://api.nbp.pl/api/exchangerates/tables/C/'
	url_date_start = date(2002, 1, 2)
	url_date_end = url_date_start + timedelta(days=93)
	if url_type == 'A':
		return url_table_a + str(url_date_start) + '/' + str(url_date_end)
	if url_type == 'B':
		return url_table_b + str(url_date_start) + '/' + str(url_date_end)
	if url_type == 'C':
		return url_table_c + str(url_date_start) + '/' + str(url_date_end)


def create_inserts(data_table):
	insert_start = "INSERT INTO tabela_a values(default,'"
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


def get_data(url_type):
	return requests.get(url=create_url(url_type)).json()


def connect_to_db():
	return psycopg2.connect(host='localhost', database='test_app_nbp', user='postgres', password='postgres')


def execute_inserts(conn, insert_table):
	cur = conn.cursor()
	for inserts in insert_table:
		for insert in inserts:
			cur.execute(insert)
	conn.commit()


if __name__ == '__main__':
	data_import()
