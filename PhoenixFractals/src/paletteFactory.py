from Palette import PaletteOne, PaletteTwo

def paletteFactory(colorChoice, iteration):
    if colorChoice != "":
        if colorChoice == "PaletteOne":
            return PaletteOne(iteration)
        elif colorChoice == "PaletteTwo":
            return PaletteTwo(iteration)
        else:
            raise NotImplementedError("Invalid palette requested.")
    else:
        return PaletteOne(iteration)
