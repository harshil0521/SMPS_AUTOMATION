import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('harshil', 'solanki')
        self.assertEqual(formatted_name, 'Harshil Solanki')

