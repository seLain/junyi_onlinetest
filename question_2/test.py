import unittest
from solution import exclude

class TestSolutionMethods(unittest.TestCase):

    def test_reverse_string(self):
        # question tests
        n = 15
        expected = 9
        computed = exclude(n)
        self.assertEqual(expected, computed)

if __name__ == '__main__':
    unittest.main()