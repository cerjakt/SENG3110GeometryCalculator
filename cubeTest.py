import unittest
import cube

class cubeTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(cube.volume(32, 1024) == 32768)

    def test_volume2(self):
        assert(cube.volume(100, 10000) == 1000000)

    #failing test
    def test_volume3(self):
        assert(cube.volume(10, 1000) == 0)


if __name__ == '__main__':
    unittest.main()