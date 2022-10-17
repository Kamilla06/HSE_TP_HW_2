import unittest
import time
from main import _max

class TimeTestCase(unittest.TestCase):
    def test_time(self):
        #откроем файл с 10^6 элементами
        with open('time_test.txt', 'r', encoding='utf-8') as file:
            array = list(map(int, file.readline().split()))

        #3 раза замерим время и возьмем среднее значение
        start_time_1 = time.time()
        tmp_1 = _max(array)
        end_time_1 = time.time()
        start_time_2 = time.time()
        tmp_2 = _max(array)
        end_time_2 = time.time()
        start_time_3 = time.time()
        tmp_3 = _max(array)
        end_time_3 = time.time()
        average_time = (end_time_1 + end_time_2 + end_time_3 - start_time_1 - start_time_2 - start_time_3)/3

        self.assertLess(average_time, 0.075)

if __name__ == '__main__':
    unittest.main()
