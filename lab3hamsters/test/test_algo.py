import unittest
from hamster_algo import max_number_of_hamsters


class Test(unittest.TestCase):
    def test_function_1_scenario(self):
        self.assertEqual(max_number_of_hamsters("test_input_1.txt"), 3)

    def test_function_2_scenario(self):
        self.assertEqual(max_number_of_hamsters("test_input_2.txt"), 1)

    def test_function_3_scenario(self):
        self.assertEqual(max_number_of_hamsters("test_input_3.txt"), 3)

    def test_function_4_scenario(self):
        self.assertEqual(max_number_of_hamsters("test_input_4.txt"), 5)
