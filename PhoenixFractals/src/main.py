import sys
import fractalParser
import paletteFactory
from ImagePainter import main

userInput = sys.argv[1:] #Everything after "python main.py"
if len(userInput) > 0:
    fileName = userInput[0]
    #fileName.replace(".frac", "")
    fractal = fractalParser.parseFile(userInput[0])
else:
    fileName = "Default Fractal"
    fractal = fractalParser.parseFile("")

if len(userInput) > 1:
    palette = paletteFactory.paletteFactory(userInput[1], fractal.iterations)
else:
    palette = paletteFactory.paletteFactory("", fractal.iterations)

main(fileName, fractal, palette)
