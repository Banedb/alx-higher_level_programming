#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


types = [2, -2, '2', (2,), {'2': 2}, True, [2]]
attr = ['width', 'height', 'x', 'y']


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(4, 5, 1, 2, 25)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 25)

    def test_width(self):
        rect = Rectangle(4, 5)
        rect.width = 10
        self.assertEqual(rect.width, 10)

    def test_height(self):
        rect = Rectangle(4, 5)
        rect.height = 10
        self.assertEqual(rect.height, 10)

    def test_x(self):
        rect = Rectangle(4, 5, 1, 2)
        rect.x = 3
        self.assertEqual(rect.x, 3)

    def test_y(self):
        rect = Rectangle(4, 5, 1, 2)
        rect.y = 4
        self.assertEqual(rect.y, 4)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(2, 2)
        output = '##\n##\n'
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), output)

    def test_str(self):
        r = Rectangle(5, 5, 1, 1, 3)
        output = '[Rectangle] (3) 1/1 - 5/5\n'
        text = StringIO()
        sys.stdout = text
        print(r)
        sys.stdout = sys.__stdout__
        self.assertEqual(text.getvalue(), output)

    def test_update(self):
        pass

    def test_property_check(self):
        rect = Rectangle(10, 5, 2, 3)
        with self.assertRaises(ValueError):
            rect.width = 0
        with self.assertRaises(ValueError):
            rect.height = 0
        with self.assertRaises(ValueError):
            rect.x = -1
        with self.assertRaises(ValueError):
            rect.y = -10
        with self.assertRaises(TypeError):
            rect.width = "10"
        with self.assertRaises(TypeError):
            rect.height = "5"
        with self.assertRaises(TypeError):
            rect.x = '4'
        with self.assertRaises(TypeError):
            rect.y = '5'

    def test_types(self):
        r = Rectangle(5, 4, 3, 2)
        for attribute in attr:
            for data in types:
                if not isinstance(data, int):
                    with self.assertRaises(TypeError):
                        setattr(r, attribute, data)


if __name__ == '__main__':
    unittest.main()
