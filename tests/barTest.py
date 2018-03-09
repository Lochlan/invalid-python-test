import unittest

from wrapped import bar

class BarTest(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(bar.run(), 'python is cool!')

if __name__ == '__main__':
    unittest.main()
