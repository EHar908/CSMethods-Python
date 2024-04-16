import unittest
from paletteFactory import paletteFactory

class TestPaletteFactory(unittest.TestCase):
    def test_incorrectPalette(self):
        with self.assertRaises(RuntimeError):
            paletteFactory("incorrectPaletteName", 111)
            paletteFactory(123, 111)
            paletteFactory(1.231, 111)


if __name__ == '__main__':
    unittest.main()

