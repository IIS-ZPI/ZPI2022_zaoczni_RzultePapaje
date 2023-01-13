import unittest
from datetime import date, timedelta

import data_import


class TestUtils(unittest.TestCase):

	def setUp(self):
		self.url_date_start = date(2002, 1, 2)
		self.url_date_end = self.url_date_start + timedelta(days=93)
		self.data_table = data_import.get_data('A', self.url_date_start, self.url_date_end)
		self.config = data_import.parse_config()
		self.result = "INSERT INTO tabela_a VALUES(default,'1/A/NBP/2002','2002-01-02','Australia','AUD',2.0227);"
		self.result_a = 'http://api.nbp.pl/api/exchangerates/tables/A/2002-01-02/2002-04-05'
		self.result_b = 'http://api.nbp.pl/api/exchangerates/tables/B/2002-01-02/2002-04-05'
		self.result_c = 'http://api.nbp.pl/api/exchangerates/tables/C/2002-01-02/2002-04-05'
		self.conn = data_import.connect_to_db()

	def test_url_response(self):
		self.assertEqual(data_import.create_url('A', self.url_date_start, self.url_date_end), self.result_a)
		self.assertEqual(data_import.create_url('B', self.url_date_start, self.url_date_end), self.result_b)
		self.assertEqual(data_import.create_url('C', self.url_date_start, self.url_date_end), self.result_c)

	def test_insert_creation(self):
		self.assertEqual(data_import.create_inserts(self.data_table, 'A')[0][0], self.result)

	def test_db_connection(self):
		self.assertEqual(data_import.connect_to_db().server_version, 150001)


if __name__ == '__main__':
	unittest.main()
