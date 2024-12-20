import unittest
import square

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(2), 4)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(2), 8)

