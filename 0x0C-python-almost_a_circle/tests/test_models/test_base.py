#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id(self):
        t = Base(5)
        self.assertEqual(t.id, 5)

    def test_noid(self):
        t = Base()
        self.assertEqual(t.id, 1)


if __name__ == '__main__':
    unittest.main()
