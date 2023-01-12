from django.test import TestCase
from nbp.helpers.statistical_measures import median, dominant, standard_deviation, coefficient_of_variation

# INPUT IS ASSUMED TO BE CORRECT – NO STRINGS AND DIFFERENT TYPES, JUST AN ARRAY OF DECIMAL OR INT NUMBERS 
class StatisticalMeasuresTestCase(TestCase):
    datasets = [
        [],
        [5.55],
        [5.55, 1.11],
        [181, 187, 196, 196, 198, 203, 207, 211, 215, 123, 199],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [3, 7, 14.5, 34.76, 12.256, 4.1, 1.5, 1.5, 1.5, 4.1],
        [-15.4, -12.5, 12.5, 4.2, -77.11, 4.2],
        [1.11, 1.05, 1.09, 1.005, 1.10, 1.08, 1.06, 1.07, 1.4, 1.04, 1.4, 1.03, 1.02, 1.01],
        [1.1150335, 1.05123, 1.08111, 1.0921111, 1.00545666, 1.101131, 1.08111, 1.06131323, 1.07, 1.412313],
        [0, 0, 0]
    ]

    def test_median(self):
        self.assertEquals(median(self.datasets[0]), None)
        self.assertEquals(median(self.datasets[1]), 5.55)
        self.assertEquals(median(self.datasets[2]), 3.33)
        self.assertEquals(median(self.datasets[3]), 198)
        self.assertEquals(median(self.datasets[4]), 5.5)
        self.assertEquals(median(self.datasets[5]), 6)
        self.assertEquals(median(self.datasets[6]), 4.1)
        self.assertEquals(median(self.datasets[7]), -4.15)
        self.assertEquals(median(self.datasets[8]), 1.065)
        self.assertEquals(median(self.datasets[9]), 1.08111)
        self.assertEquals(median(self.datasets[10]), 0)

    def test_dominant(self):
        self.assertEquals(dominant(self.datasets[0]), None)
        self.assertEquals(dominant(self.datasets[1]), 5.55)
        self.assertEquals(dominant(self.datasets[2]), [5.55, 1.11])
        self.assertEquals(dominant(self.datasets[3]), 196)
        self.assertEquals(dominant(self.datasets[4]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEquals(dominant(self.datasets[5]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        self.assertEquals(dominant(self.datasets[6]), 1.5)
        self.assertEquals(dominant(self.datasets[7]), 4.2)
        self.assertEquals(dominant(self.datasets[8]), 1.4)
        self.assertEquals(dominant(self.datasets[9]), 1.08111)
        self.assertEquals(dominant(self.datasets[10]), 0)

    def test_standard_deviation(self):
        self.assertEquals(standard_deviation(self.datasets[0]), None)
        self.assertEquals(standard_deviation(self.datasets[1]), 0)
        self.assertEquals(standard_deviation(self.datasets[2]), 2.2)
        self.assertEquals(standard_deviation(self.datasets[3]), 23.853)
        self.assertEquals(standard_deviation(self.datasets[4]), 2.872)
        self.assertEquals(standard_deviation(self.datasets[5]), 3.162)
        self.assertEquals(standard_deviation(self.datasets[6]), 9.787)
        self.assertEquals(standard_deviation(self.datasets[7]), 29.866)
        self.assertEquals(standard_deviation(self.datasets[8]), 0.125)
        self.assertEquals(standard_deviation(self.datasets[9]), 0.106)
        self.assertEquals(standard_deviation(self.datasets[10]), 0)

    #Temporarily disabled bad test
    # def test_bad_test_that_should_work(self):
    #     self.assertEqual(self.number2, self.number3)
