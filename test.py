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

    def test_is_prime(self):
        """Testing is_prime method
        """
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(12), False)
        self.assertEqual(is_prime(8), False)





if __name__ == '__main__':
    unittest.main()