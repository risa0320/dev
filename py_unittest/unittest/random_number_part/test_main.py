
import unittest


class TestOikujiCase(unittest.TestCase):

    def test_generate_random_number(self):
        from random_number_part import main

        omikuji = main.Omikuji()
        random_number = omikuji.generate_random_number()
        self.assertGreater(random_number, 0)
        self.assertLess(random_number, 1)
