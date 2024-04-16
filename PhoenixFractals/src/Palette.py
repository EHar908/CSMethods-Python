from colour import Color

cri = Color('crimson')
lime = Color('lime')
pur = Color('purple')
blk = Color('black')
mag = Color('magenta')
pin = Color('pink')
ora = Color('orange')
yel = Color('yellow')


class Palette:
    def __init__(self, iterationN):
        if type(self) is Palette:
            raise NotImplementedError("A Palette is abstract, and cannot be created.")
        else:
            self.iterationN = iterationN
    def getColor(self, iterationN):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")
    def getIteration(self):
        return self.iterationN

class PaletteOne(Palette):
    def __init__(self, iterationN):
        super().__init__(iterationN)
        while(iterationN % 12 != 0):
            iterationN += 1
        iterationN = iterationN // 12
        self.dynamic = [c.hex_l for c in cri.range_to(blk, iterationN)]
        self.dynamic += [c.hex_l for c in blk.range_to(cri, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in cri.range_to(lime, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in lime.range_to(yel, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in yel.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(lime, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in lime.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(pur, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in pur.range_to(mag, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in mag.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(pur, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in pur.range_to(cri, iterationN + 1)][1:]

    def getColor(self, iterationN):
        return self.dynamic[iterationN]

class PaletteTwo(Palette):
    def __init__(self, iterationN):
        super().__init__(iterationN)
        while(iterationN % 13 != 0):
            iterationN += 1
        iterationN = iterationN // 13
        self.dynamic = [c.hex_l for c in pin.range_to(blk, iterationN)]
        self.dynamic += [c.hex_l for c in blk.range_to(ora, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in ora.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(lime, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in lime.range_to(pin, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in pin.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(ora, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in ora.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(lime, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in lime.range_to(pin, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in pin.range_to(blk, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in blk.range_to(ora, iterationN + 1)][1:]
        self.dynamic += [c.hex_l for c in ora.range_to(cri, iterationN + 1)][1:]


    def getColor(self, iterationN):
        return self.dynamic[iterationN]



