class Fractal:
    def __init__(self, pixels, centerx, centery, axislength, iterations):
        if type(self) == Fractal:
            raise NotImplementedError("A Fractal is abstract, and cannot be created.")
        else:
            self.pixels = pixels
            self.centerx = centerx
            self.centery = centery
            self.axislength = axislength
            self.iterations = iterations
    def count(self, comXY):
        raise NotImplementedError("Concrete subclass of Fractal must implement Count parameter method.")

class Phoenix(Fractal):
    def __init__(self, pixels, centerx, centery, axislength, iterations, preal, pimag, creal, cimag):
        super().__init__(pixels, centerx, centery, axislength, iterations)
        self.preal = preal
        self.pimag = pimag
        self.creal = creal
        self.cimag = cimag

    def count(self, comXY):
        julConst = complex(self.creal, self.cimag)
        phConst = complex(self.preal, self.pimag)
        xyFlipped = complex(comXY.imag, comXY.real)
        xyPrev = 0 + 0j
        currentXY = xyFlipped
        for i in range(self.iterations + 1):
            xySave = currentXY
            currentXY = (currentXY * currentXY) + julConst + (phConst * xyPrev)
            xyPrev = xySave
            if abs(currentXY) > 2:
                return i
        return self.iterations



class Mandelbrot(Fractal):
    def __init__(self, pixels, centerx, centery, axislength, iterations):
        super().__init__(pixels, centerx, centery, axislength, iterations)
    def count(self, comXY):
        complexNum = complex(0, 0)
        for i in range(self.iterations + 1):
            complexNum = complexNum * complexNum + comXY
            if abs(complexNum) > 2:
                return i
        return self.iterations

class Spider(Fractal):
    def __init__(self, pixels, centerx, centery, axislength, iterations):
        super().__init__(pixels, centerx, centery, axislength, iterations)

    def count(self, comXY):
        complexNum = complex(0, 0)
        for i in range(self.iterations + 1):
            complexNum = complexNum * complexNum + comXY
            comXY = (comXY * 0.5) + complexNum
            if abs(complexNum) > 2:
                return i
        return self.iterations

class FourMandelbrot(Fractal):
    def __init__(self, pixels, centerx, centery, axislength, iterations):
        super().__init__(pixels, centerx, centery, axislength, iterations)

    def count(self, comXY):
        complexNum = complex(0, 0)
        for i in range(self.iterations + 1):
            complexNum = complexNum * complexNum * complexNum * complexNum + comXY
            if abs(complexNum) > 2:
                return i
        return self.iterations
