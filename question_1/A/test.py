import unittest
from solution import reverse_string

class TestSolutionMethods(unittest.TestCase):

    def test_reverse_string(self):
        # question tests
        s = 'junyiacademy'
        expected = 'ymedacaiynuj'
        computed = reverse_string(s)
        self.assertEqual(expected, computed)

if __name__ == '__main__':
    unittest.main()