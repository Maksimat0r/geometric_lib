import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):
    def test_calc_circle_area(self):
        result = calc('circle', 'area', [1])
        self.assertAlmostEqual(result, 3.141592653589793)

    def test_calc_square_area(self):
        result = calc('square', 'area', [2])
        self.assertEqual(result, 4)

    def test_calc_triangle_area(self):
        result = calc('triangle', 'area', [3, 4, 5])
        self.assertEqual(result, 6)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('hexagon', 'area', [3])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [1])

    def test_invalid_size_for_circle(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', [1, 2])

    def test_invalid_size_for_triangle(self):
        with self.assertRaises(TypeError):
            calc('triangle', 'area', [3, 4])
