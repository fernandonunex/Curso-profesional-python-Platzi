"""Testing methods"""

import unittest
from unittest import TestCase
from palindrome_static_typing import is_palindrome
from prime_static_typing import is_prime

class TestingFunctions(TestCase):
    """ Tests to know if the methods works well
    """

    def test_is_palindrome(self):
        """Testing is_palindrome method
        """
        self.assertEqual(is_palindrome('Ligar es ser agil'), True)
        self.assertEqual(is_palindrome('Arepera'), True)
        self.assertEqual(is_palindrome('Cualquier cosa'), False)
        self.assertEqual(is_palindrome('Ana'), True)


if __name__ == '__main__':
    unittest.main()