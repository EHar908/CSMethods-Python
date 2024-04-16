import sys
from Fractal import Mandelbrot, FourMandelbrot, Phoenix, Spider

def makeFractal(fractalInfo):
    f = fractalInfo
    if "type" in f:
        if f["type"] == "phoenix":
            return Phoenix(f["pixels"], f["centerx"], f["centery"], f["axislength"], f["iterations"],
                           f["preal"], f["pimag"], f["creal"], f["cimag"])
        elif f["type"] == "spider":
            return Spider(f["pixels"], f["centerx"], f["centery"], f["axislength"], f["iterations"])
        elif f["type"] == "mandelbrot":
            return Mandelbrot(f["pixels"], f["centerx"], f["centery"], f["axislength"], f["iterations"])
        elif f["type"] == "mandelbrot4":
            return FourMandelbrot(f["pixels"], f["centerx"], f["centery"], f["axislength"], f["iterations"])
        else:
            raise RuntimeError("Please provide a valid fractal type.")
    else:
        raise RuntimeError("Please provide a 'type' in your Fractal file.")

