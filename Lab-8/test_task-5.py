import unittest

def convert_date_format(date_str):
    year, month, day = date_str.split("-")
    return f"{day}-{month}-{year}"

class TestConvertDateFormat(unittest.TestCase):

    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_another_date(self):
        self.assertEqual(convert_date_format("1999-01-05"), "05-01-1999")

if __name__ == "_main_":
    unittest.main()