import unittest

from wrapped import foo

class FooTest(unittest.TestCase):
    def test_default_return_value(self):
        self.assertEqual(foo.run(), 'my name is happy foo')

    def test_parameterized_return_value(self):
        self.assertEqual(foo.run('friendly', 'Rupert'), 'my name is friendly Rupert')

if __name__ == '__main__':
    unittest.main()
