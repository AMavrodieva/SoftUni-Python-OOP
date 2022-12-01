# zero test
import unittest

class ReverseIterTests(unittest.TestCase):
    def test_zero(self):
        res = ""
        reversed_list = reverse_iter([1, 2, 3, 4])
        for item in reversed_list:
            res += str(item) + "\n"
        self.assertEqual(res, "4\n3\n2\n1\n")

if __name__ == '__main__':
    unittest.main()