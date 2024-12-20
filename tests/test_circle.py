import unittest
import circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(1), 3.141592653589793)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(1), 6.283185307179586)
