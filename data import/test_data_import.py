import data_import
import unittest


class TestUtils(unittest.TestCase):
	def test_url_response(self):
		self.assertEqual(data_import.create_url('A'), 'http://api.nbp.pl/api/exchangerates/tables/A/2002-01-02/2002-04-05')
		self.assertEqual(data_import.create_url('B'), 'http://api.nbp.pl/api/exchangerates/tables/B/2002-01-02/2002-04-05')
		self.assertEqual(data_import.create_url('C'), 'http://api.nbp.pl/api/exchangerates/tables/C/2002-01-02/2002-04-05')


if __name__ == '__main__':
	unittest.main()
