from datetime import timedelta, date
import requests


def data_import():
	tables = ['A', 'B', 'C']
	insert_table = []
	for table in tables:
		resp = requests.get(url=create_url(table))
		for x in resp.json():
			insert_table.append(x)


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

def create_inserts(insert_table):
	pass

if __name__ == '__main__':
	data_import()
