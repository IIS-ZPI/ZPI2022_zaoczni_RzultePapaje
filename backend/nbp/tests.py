from django.test import SimpleTestCase


# Create your tests here.
class ExampleTestCase(SimpleTestCase):
    def setUp(self):
        self.number1 = 5
        self.number2 = 5
        self.number3 = 4

    def test_example_fn(self):
        self.assertEqual(self.number1, self.number2)

    def test_example_next_fn(self):
        self.assertNotEqual(self.number1, self.number3)

    #Temporarily disabled bad test
    # def test_bad_test_that_should_work(self):
    #     self.assertEqual(self.number2, self.number3)

