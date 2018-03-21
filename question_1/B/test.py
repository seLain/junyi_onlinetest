import unittest
from solution import reverse_string_by_order

class TestSolutionMethods(unittest.TestCase):

    def test_reverse_string(self):
        # question tests
        s = 'flipped class room is important'
        expected = 'deppilf ssalc moor si tnatropmi'
        computed = reverse_string_by_order(s)
        self.assertEqual(expected, computed)

if __name__ == '__main__':
    unittest.main()