import unittest
import equilateral_triangle

class equilateral_triangleTest(unittest.TestCase):

    #passing tests
    def test_area1(self):
        assert(equilateral_triangle.area(32) == 443.40500673763256)

    def test_area2(self):
        assert(equilateral_triangle.area(100) == 4330.127018922193)

    #failing test
    def test_area3(self):
        assert(equilateral_triangle.area(1000) == 0)


if __name__ == '__main__':
    unittest.main()