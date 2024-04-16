import unittest
import ImagePainter
from fractalFactory import makeFractal

class TestImagePainter(unittest.TestCase):
    testFractal = {
        "type": "mandelbrot",
        "centerx": -1.643577002,
        "centery": -0.000058690069,
        "axislength": 0.000851248888,
        "pixels": 512,
        "iterations": 111
    }
    testFractal = makeFractal(testFractal)

    def test_pixelStatus(self):
        self.assertEqual(ImagePainter.pixelStatus(1, self.testFractal), '[100% =================================]')
        self.assertEqual(ImagePainter.pixelStatus(7, self.testFractal), '[ 99% =================================]')
        self.assertEqual(ImagePainter.pixelStatus(257, self.testFractal), '[ 50% ================                 ]')
        self.assertEqual(ImagePainter.pixelStatus(256, self.testFractal), '[ 50% =================                ]')
        self.assertEqual(ImagePainter.pixelStatus(100, self.testFractal), '[ 80% ===========================      ]')
        self.assertEqual(ImagePainter.pixelStatus(640, self.testFractal), '[-25%                                  ]')
        self.assertEqual(ImagePainter.pixelStatus(137, self.testFractal), '[ 73% ========================         ]')
        self.assertEqual(ImagePainter.pixelStatus(512, self.testFractal), '[  0%                                  ]')

if __name__ == '__main__':
    unittest.main()
