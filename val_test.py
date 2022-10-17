import unittest
from main import _min, _max, _sum, _mult

class MyValTestCase(unittest.TestCase):
    def test_min(self):
        with open('test.txt', 'r', encoding='utf-8') as file:
            array = list(map(int, file.readline().split()))
            self.assertEqual(_min(array), 1)

    def test_max(self):
        with open('test.txt', 'r', encoding='utf-8') as file:
            array = list(map(int, file.readline().split()))
            self.assertEqual(_max(array), 18748717481)

    def test_sum(self):
        with open('test.txt', 'r', encoding='utf-8') as file:
            array = list(map(int, file.readline().split()))
            self.assertEqual(_sum(array), 20000518976)

    def test_mult(self):
        with open('test.txt', 'r', encoding='utf-8') as file:
            array = list(map(int, file.readline().split()))
            self.assertEqual(_mult(array), 24307127499153558476614976597099838218285503379562948432094099496505401071310708232591159853615205926092072960)

if __name__ == '__main__':
    unittest.main()
