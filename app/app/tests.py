"""
Sample tests.
"""
from django.test import SimpleTestCase
from app import calc


class calcTests(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Test adding numbers together."""
        # res = calc.add(5, 6)
        R = calc.add(5, 6)
        self.assertEqual(R, 11)

    def test_sub(self):
        S =calc.sub(6, 4)
        self.assertEqual(S, 2)
