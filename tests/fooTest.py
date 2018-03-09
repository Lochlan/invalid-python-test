import unittest

from wrapped import foo

class FooTest(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(foo.run(), 'my name is foo')

if __name__ == '__main__':
    unittest.main()
