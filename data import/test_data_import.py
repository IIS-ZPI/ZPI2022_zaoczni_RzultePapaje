from datetime import date, timedelta

import data_import
import unittest


class TestUtils(unittest.TestCase):

	def setUp(self):
		self.url_date_start = date(2002, 1, 2)
		self.url_date_end = self.url_date_start + timedelta(days=93)
		self.data_table = data_import.get_data('A', self.url_date_start, self.url_date_end)

	def test_url_response(self):
		result_a = 'http://api.nbp.pl/api/exchangerates/tables/A/2002-01-02/2002-04-05'
		result_b = 'http://api.nbp.pl/api/exchangerates/tables/B/2002-01-02/2002-04-05'
		result_c = 'http://api.nbp.pl/api/exchangerates/tables/C/2002-01-02/2002-04-05'
		self.assertEqual(data_import.create_url('A', self.url_date_start, self.url_date_end), result_a)
		self.assertEqual(data_import.create_url('B', self.url_date_start, self.url_date_end), result_b)
		self.assertEqual(data_import.create_url('C', self.url_date_start, self.url_date_end), result_c)

	def test_insert_creation(self):
		result = "INSERT INTO tabela_a values(default,'1/A/NBP/2002','2002-01-02','AUD',2.0227);"
		self.assertEqual(data_import.create_inserts(self.data_table, 'A')[0][0], result)


if __name__ == '__main__':
	unittest.main()
