"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from csv_api.doink import *
import os

class TestDoink(TestCase):

    def setUp(self):
        pass

    def test_sample(self):
        self.assertEqual(1+1, 2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    main()

