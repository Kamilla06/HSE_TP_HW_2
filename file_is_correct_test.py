import unittest
from main import main

class MyTestCase(unittest.TestCase):
    def test_correction(self):
        self.assertEqual(main('incorrect_test.txt'), f'ERROR\nFile is incoect')

if __name__ == '__main__':
    unittest.main()
