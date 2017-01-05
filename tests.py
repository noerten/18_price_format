import unittest

from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    def test_float(self):
        self.assertEqual(format_price(77775.00), '77 775')


    def test_invalid_value(self):
        self.assertIsNone(format_price('seven'))


if __name__ == '__main__':
    unittest.main()
