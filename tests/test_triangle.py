import unittest
import triangle

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(3, 4, 5), 6)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

