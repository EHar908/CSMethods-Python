# Fractal Visualizer User Manual

Welcome! In this program, you can construct your very own unique fractal images by submitting a file! Additionally,
you can see these shapes in different colors by selecting one of our optional palettes! 

To run the program, verify that you are within the project file (you can do this by looking at your current location 
in the directory). Once you are inside, you can activate the program by typing the following in the terminal: 

``` python src/main.py ```

When you do this, the program will create its default fractal image using its default palette and end. If you 
would like to submit your own valid file, enter the following command:

``` python src/main.py [insert your file name here [choose a palette]]```

If you misspell or provide an invalid file or palette, the program will raise an error, indicate such and
display the options for the palettes before ending. If you do not provide a palette option, the default 
palette will be used with your fractal image. You cannot change the palette used on the default option. 

Be aware that your file must contain at least one of the following:

```
type: [a valid string of either phoenix, mandelbrot, fourmandelbrot, or spider]
pixels: [a valid integer value which determines the size of the image]
centerX: [a valid float value used to determine coloration/plotting]
centerY: [a valid float value used to determine coloration/plotting]
axislength: [a valid float value used to determine coloration/plotting]
iterations: [a valid integer value which will impact the variety of colors used]
```

If you wish to create a phoenix image, your file will also need to contain the following: 

```
preal: [a valid float value]
pimag: [a valid float value]
creal: [a valid float value]
cimag: [a valid float value]
```

If there is a typo in any of these written categories or the value provided isn't of the appropriate type,
then an error will indicate such and the program will end. 

During the creation of your fractal image, a window will appear on your screen and the program will create your 
image in real time, along with a percentage meter keeping track of its progress. 

Once it's complete, the program will automatically save a png version of the image into your computer. 
To exit the program, simply click on the "x" button on the png in the top right corner. 
