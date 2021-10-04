import unittest
import triangle

class triangleTest(unittest.TestCase):

    #passing tests
    def test_area1(self):
        assert(triangle.area(10, 32) == 160.0)

    def test_area2(self):
        assert(triangle.area(10, 100) == 500.0)

    #failing test
    def test_area3(self):
        assert(triangle.area(10, 1000) == 0)

if __name__ == '__main__':
    unittest.main()