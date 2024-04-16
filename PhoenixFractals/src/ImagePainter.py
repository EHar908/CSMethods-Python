import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop

def paint(fractal, palette, window, img):
    coordsX = ((fractal.centerx + (fractal.axislength / 2.0)),
           (fractal.centerx - (fractal.axislength / 2.0)))
    coordY = (fractal.centery - (fractal.axislength / 2.0))
    canvas = Canvas(window, width=fractal.pixels, height=fractal.pixels, bg='#000000')
    canvas.pack()
    canvas.create_image((int(fractal.pixels / 2), int(fractal.pixels / 2)), image=img, state="normal") #Do these need to be cast to int to prevent a possible float?
    pixelSize = abs(coordsX[0] - coordsX[1]) / fractal.pixels
    for row in range(fractal.pixels, 0, -1):
        colorCodes = []
        for column in range(fractal.pixels):
            x = coordsX[1] + column * pixelSize
            y = coordY + row * pixelSize
            returnedColor = fractal.count(complex(x, y))
            colorCodes.append(palette.getColor(returnedColor))
        img.put('{' + ' '.join(colorCodes) + '}', to=(0, fractal.pixels - row))
        window.update()
        print(pixelStatus(row, fractal), end='\r', file=sys.stderr)

def pixelStatus(row, fractal):
    portion = (fractal.pixels - row) / fractal.pixels
    statusPercent = '{:>4.0%}'.format(portion)
    statusBar = '=' * int(34 * portion) #Why is it 34 here? Does it matter if this is changed?
    return ''.join(list(['[', statusPercent, ' ', '{:<33}'.format(statusBar), ']']))

def main(fileName, fractal, palette):
    print("Rendering {} fractal".format(fractal), file=sys.stderr)
    startTime = time.time()
    window = Tk()
    img = PhotoImage(width=fractal.pixels, height=fractal.pixels)
    paint(fractal, palette, window, img)
    endTime = time.time()
    print(f"\nDone in {endTime - startTime:.3f} seconds!", file=sys.stderr)
    img.write(f"{fileName}.png")
    print(f"Wrote picture {fileName}.png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()
