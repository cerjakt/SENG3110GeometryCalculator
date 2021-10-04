import unittest
import cuboid

class cubeTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(cuboid.volume(10, 32, 32) == 10240)

    def test_volume2(self):
        assert(cuboid.volume(10, 100, 100) == 100000)

    #failing test
    def test_volume3(self):
        assert(cuboid.volume(10, 1000, 1000) == 0)


if __name__ == '__main__':
    unittest.main()