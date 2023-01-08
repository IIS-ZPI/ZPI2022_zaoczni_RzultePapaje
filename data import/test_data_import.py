import data_import
import unittest


class TestUtils(unittest.TestCase):

	def setUp(self):
		self.data_table = data_import.get_data('A').json()
	def test_url_response(self):
		self.assertEqual(data_import.create_url('A'), 'http://api.nbp.pl/api/exchangerates/tables/A/2002-01-02/2002-04-05')
		self.assertEqual(data_import.create_url('B'), 'http://api.nbp.pl/api/exchangerates/tables/B/2002-01-02/2002-04-05')
		self.assertEqual(data_import.create_url('C'), 'http://api.nbp.pl/api/exchangerates/tables/C/2002-01-02/2002-04-05')

	def test_insert_creation(self):
		self.assertEqual(data_import.create_inserts(self.data_table)[0][0], "INSERT INTO tabela_a values(default,'1/A/NBP/2002','2002-01-02','AUD',2.0227);")


if __name__ == '__main__':
	unittest.main()
