import unittest
from fractalFactory import makeFractal

class TestFractalFactory(unittest.TestCase):
    incorrectFractalType = {
        "type": "mmmandels",
        "centerx": -1.643577002,
        "centery": -0.000058690069,
        "axislength": 0.000851248888,
        "pixels": 512,
        "iterations": 111
    }
    incorrectFractalType1 = {
        "type": 123,
        "centerx": -1.643577002,
        "centery": -0.000058690069,
        "axislength": 0.000851248888,
        "pixels": 512,
        "iterations": 111
    }
    incorrectFractalType2 = {
        "type": "",
        "centerx": -1.643577002,
        "centery": -0.000058690069,
        "axislength": 0.000851248888,
        "pixels": 512,
        "iterations": 111
    }

    missingFractalType = {
        "centerx": -1.643577002,
        "centery": -0.000058690069,
        "axislength": 0.000851248888,
        "pixels": 512,
        "iterations": 111
    }

    def test_incorrectType(self):
        with self.assertRaises(RuntimeError):
            makeFractal(self.incorrectFractalType)
            makeFractal(self.incorrectFractalType1)
            makeFractal(self.incorrectFractalType2)

    def test_missingType(self):
        with self.assertRaises(RuntimeError):
            makeFractal(self.missingFractalType)

if __name__ == '__main__':
    unittest.main()