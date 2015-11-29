# -*- coding: utf-8 -*-
import unittest
from functions import replace

class TestReplace(unittest.TestCase):

    def test_replace(self):
        self.assertEqual(replace(''), 0)
        self.assertEqual(replace('abc'), 0)
        self.assertEqual(replace('123,45'), 123.45)
        self.assertEqual(replace('123.45'), 123.45)
        self.assertEqual(replace('123 456,78'), 123456.78)
        self.assertEqual(replace('+12'), 12)
        self.assertEqual(replace('+ 12'), 12)
        self.assertEqual(replace('-12'), -12)
        self.assertEqual(replace('- 12'), -12)
        self.assertEqual(replace(' 100 '), 100)
        self.assertEqual(replace('123zł'), 123)
        self.assertEqual(replace('123 zł'), 123)
        self.assertEqual(replace('123.456,78'), 123456.78)
        self.assertEqual(replace('123.456,78 zł'), 123456.78)

if __name__ == '__main__':
    unittest.main()
