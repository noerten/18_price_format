import unittest

from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_float(self):
        self.assertEqual(format_price(77775.666666), '77 775.67')

    def test_float_to_int(self):
        self.assertEqual(format_price(77775.00000), '77 775')

    def test_int(self):
        self.assertEqual(format_price(77775), '77 775')

    def test_invalid_value(self):
        self.assertIsNone(format_price('seven'))

    def test_negative_value(self):
        self.assertIsNone(format_price(-9))


if __name__ == '__main__':
    unittest.main()
