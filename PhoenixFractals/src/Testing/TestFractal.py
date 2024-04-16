import unittest
import Fractal
from fractalFactory import makeFractal

class TestFractal(unittest.TestCase):
    correctFractalInfoM = Fractal.Mandelbrot(512, -1.643577002, -0.000058690069, 0.000851248888, 111)
    correctFractalInfoM4 = Fractal.FourMandelbrot(640, 0.0, 0.0, 4.0, 100)
    correctFractalInfoP = Fractal.Phoenix(512, 0, 0, 3.25, 101, -0.5, 0.0, 0.5667, 0.0)
    correctFractalInfoS = Fractal.Spider(640, -1.0, 0.0, 4.0, 100)


    def test_countReturnsInt(self):
        self.assertEqual(type(self.correctFractalInfoM.count(complex(0, 0))), int)
        self.assertEqual(type(self.correctFractalInfoM4.count(complex(0, 0))), int)
        self.assertEqual(type(self.correctFractalInfoP.count(complex(0, 0))), int)
        self.assertEqual(type(self.correctFractalInfoS.count(complex(0, 0))), int)

    def test_cannotCreateFractalObject(self):
        with self.assertRaises(NotImplementedError):
            Fractal.Fractal(512, -1.523, -1.523, 1.32, 112)

if __name__ == '__main__':
    unittest.main()