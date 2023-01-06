import datetime

import requests
from datetime import timedelta, date


def data_import():
	print(create_url('A'))
	resp = requests.get(url=create_url('A'))
	for x in resp.json():
		print(x)


def create_url(url_type):
	#start_date = date(2002, 1, 2)
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


if __name__ == '__main__':
	data_import()
