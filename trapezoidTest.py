import unittest
import trapezoid

class trapezoidTest(unittest.TestCase):

    #passing tests
    def test_area1(self):
        assert(trapezoid.area(21, 32) == 672.0)

    def test_area2(self):
        assert(trapezoid.area(55, 100) == 5500.0)

    #failing test
    def test_area3(self):
        assert(trapezoid.area(505, 1000) == 0)

if __name__ == '__main__':
    unittest.main()