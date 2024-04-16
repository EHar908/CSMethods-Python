# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
This project is a continuation of the Fractal program that was trimmed and reorganized into
clean code. In this sprint, the fundamental design of the program will be significantly altered
in order to become way more flexible. The original program was fairly rigid in that it only worked with
a series of hard-coded fractals and palettes. This redesign should allow the utilization of new fractals 
and palettes that can be easily introduced to the program without the need to change code. 

This will be done through a combination of inheritance and polymorphism. A good solution overall is a 
combination of the two, allowing for the creation of a program that can accept any new subclass of Fractal
and palette and generate the image without the need to change or alter the core code. 


## Phase 1: System Analysis *(10%)*

This program will consist of six classes total: Fractal, FractalParser, FractalFactory, Palette, PaletteFactory, 
and ImagePainter. 

The format of the command-line interface is as follows
`python src/main.py [FRACTAL_FILE] [PALETTE_NAME]]`

The first significant part of this system is the creation of an abstract Fractal class with
at least four concreate subclasses. These subclasses -- i.e. the different types of fractals -- 
should be polymorphic to the overall structure of the Fractal class. In other words, 
the program will use classes derived from Fractal.py through inheritance. The main 
method of Fractal.py that will be used by these subclasses is count(). 

count() takes one complex number as an input and returns an integer that is the 
number of iterations tried before the absolute value of the fractal formula grew 
larger than 2.0; otherwise the maximum number of iterations is returned. Any 
other data necessary is supplied through a self reference. 

For the purposes of this program, there should be four types of fractals total that 
will inherit the structure of the Fractal class. Phoenix and Mandelbrot used in the 
original program will be utilized here, but I will need to figure out how to deduce 
a new fractal image via an equation and the necessary lengths/axis. 

Finally, the Fractals created here should have no direct association with the Palette or
Color modules used. 

For the FractalFactory class, it accepts a framework of a fractal provided by the user. 
This'll be provided via the command-line interface, where it will direct a file to the program to 
open, collect the information from, and then prepare it for the program to use. The given 
information is inserted into a Fractal object that the program can then use. 

If no file is specified when the program is run, FractalFactory should have inside of it 
a hard-coded fractal to send to the rest of the program to use. 

FractalFactory will also error-check the fractal object.

For the FractalParser class, it will verify that the format of the .frac file is correct
and that the given information is viable for FractalFactory to use in order to create 
its Fractal object and for PaletteFactory. 

For the Palette class, it exists to provide a structure for the palette subclasses, 
similar to Fractal and its subclasses. It should include a getColor() method which is 
solely used to raise an exception error
"Concrete subclass of Palette must implement getColor() method". 

The subclasses of Palette inherit their structure from Palette and must provide 
their own instance of getColor(). getColor(n) takes an integer as input and 
returns a string which represents a color in this format: "#RRGGBB"
Generalize color palette creation so that a user-defined number of iterations 
may be specified instead of using a hard-coded array of colors.

Palette should have no knowledge of the Fractal object. 

The PaletteFactory returns a Palette object depending on the Palette file 
provided by the user. If no such file is provided, a default palette will be used,
hard-coded into this file. When a non-existent palette is raised, return an error. 
The palette object shouldn't use any direct Fractal info. 

The ImagePainter class is where the canvas and fractal image is constructed and 
displayed. It's also where Tkinter is imported. It takes the info from FractalFactory,
PaletteFactory, and FractalParser as input; it purely takes their products/objects. It
doesn't take anything from the command-line or the .frac files. 

In summary, this program utilizes polymorphism in order to seamlessly take both 
fractal and palette information and generate an image. So the data used will primarily 
be provided via external .frac files, with the exception of default info if nothing 
is provided by the user. 

The main challenge I anticipate with this is understanding inheritence and polymorphism, as 
those are concepts I'm still not quite familiar with. 


## Phase 2: Design *(30%)*
-- main.py -- 
Import FractalParser, FractalFactory, PaletteFactory, ImagePainter

Check to see if they provided a file and a palette name. 
Store the filename in fracFileName
Refer the file to the FractalParser and receive back the dictionary fractalInfo
Refer the palette name to the Palette Factory and receive back a Palette object. 
Plug the Palette and Fractal objects into ImagePainter. 

-- Fractal.py -- 
Create class Fractal: 
    Declare data fields: pixels, centerx, centery, axislength, iterations, complexCoord
    define an initializer with parameters(self, pixels, centerx, centery, axislength, iterations): 
        if the type(self) equals Fractal: 
            raise a NotImplementedError("Concrete subclass of Fractal must implement parameter method.")
            Verifies that the subclass overriding here is a Fractal object type.
    define function Count(accepts a complex coordinate value):
        raise a NotImplementedError("Concrete subclass of Fractal must implement Count parameter method.")

Create subclass Mandelbrot: 
    Declare data fields: pixels, centerx, centery, axislength, iterations, complexCoord
    define an initializer with parameters(self, pixels, centerx, centery, axislength, iterations): 
        Initialize self.(for each of the data fields above)
    define a function called Count(accepts a complex coordinate value): 
        Execute the same methods utilized in part one of this project. 
        Calculate and return an iteration number (an integer value) based upon the given data fields for this instance

Create subclass Phoenix: 
    Declare data fields: preal, pimag, creal, cimag, pixels, centerx, centery, axislength, iterations, complexCoord
    define an initializer with parameters(self, pixels, centerx, centery, axislength, iterations): 
        Initialize self.(for each of the data fields above) 
    define a function called Count(accepts a complex coordinate value):
        Execute the same method utilize in part one of this object 
        Calculate and return an iteration number (an integer value) based upon the given data fields for this instance
        
Create subclass HigherMandelbrot: 
    Declare data fields: pixels, centerx, centery, axislength, iterations, complexCoord
    define an initializer with parameters(self, pixels, centerx, centery, axislength, iterations): 
        Initialize self.(for each of the data fields above)
    define a function called Count(accepts a complex coordinate value):
        Calculate and return an iteration number (an integer value) based upon the given data fields for this instance

Create subclass Spider: 
    Declare data fields: pixels, centerx, centery, axislength, iterations
    define an initializer with parameters(self, pixels, centerx, centery, axislength, iterations): 
        Initialize self.(for each of the data fields above)
    define a function called Count(accepts complexCoordinate):
        Calculate and return an iteration number (an integer value) based upon the given data fields for this instance

-- FractalFactory.py -- 
import the fractal subclasses Mandelbrot, Phoenix, HigherMandelbrot, and Spider

define makeFractal function (parameter: self, dictionary)
    Use an if/else tree to determine the type of fractal specified in the fractalInfo dictionary. 
    For whichever fractal is specified, create a new Fractal object and plug in the dictionary. 
    After that, return the newly made Fractal object. 

-- FractalParser.py -- 
import FractalFactory

Check to see if the command-line argument given has a frac file at index 1.
    Copy down the name of the file given for when the image is created. 
    Create an empty dictionary named fractalInfo. Store first in this dictionary filename: the name of the file
    If there is a file, proceed with verification below: 
        First open the file. 
        Strip all white space from the line and skip blank lines 
        Convert all text to lowercase before reading through 
        Create a for loop to read through each line.
            Skip the following lines: 
                Begin with a hashtag (#)
                Empty lines
                Empty before or after the colon
            For each line, store the text before the colon as a "key" into fractalInfo and store the text after 
                the colon as its contents. 
        Once the file has been read and converted into the fractalInfo dictionary, run a for loop that goes through each key and its names. 
        Verify that there is at least one key of the following with the appropriate data type with it. 
                type : string
                centerX : float
                centerY : float
                axisLength : float 
                pixels : integer
                iterations : integer 
        If any of these are missing OR their contents aren't of the appropriate type, raise an error and end the program there. 
        Quickly check if the type equals "phoenix". If it does, verify then that the dictionary has each of the following: 
                preal : float
                pimag : float
                creal : float
                cimag : float 
        Now equate fractal to FractalFactory.makeFractal(fractalInfo), using the function contained in that module
        Then return the fractal to main.py 
If there isn't a file, implement a default fractal dictionary to be sent over 
to the FractalFactory. 
    Define a dictionary fractalDefault. 
    Now equate fractal to FractalFactory.makeFractal(fractalDefault), using the function contained in that module
        Then return the fractal to main.py 

-- Palette.py -- 
from colour import Color 
from HTML_Palette import stylesheet, html_palette 

Create a palette of colors ranging through the RGB color cube. 
    Be sure to convert these strings to Color, like Color('red')
    Mauve, Maroon, Sapphire, Black, Magenta, Pink, Orange 

Create class Palette: 
    define the data field iterationN. 
    define the function getColor(): 
        raise a NotImplementedError("Concrete subclass of Palette must implement getColor() method")
        This verifies that each subclass of Palette provides a getColor() method which then will override 
        the main Palette's empty getColor() method. 

Create subclass PaletteOne: 
    define the data field int iterationN. 
    define the function getColor(int iterationN):
        Create the list dynamic and equate it to the colors in range from one color to a different color. This depends on the 
        number of iterations specified by the user. 
            Ex: Range of red to black in x iterations. 
            Ex code: dynamic = [ c.hex_l for c in red.range_to(black, x)]
        Alternate between normal colors and black (to prevent everything from blending together) 

Create subclass PaletteTwo: 
    define the data field iterationN. 
    define the function getColor(int iterationN): 
        Create the list dynamic and equate it to the colors in range from one color to a different color. This depends on the 
        number of iterations specified by the user. 
            Ex: Range of red to black in x iterations. 
        Alternate between normal colors and black (to prevent everything from blending together)         

-- PaletteFactory.py -- 
from Palette import PaletteOne, PaletteTwo

Check to see if the command-line offered a palette name. 
    If they offered a valid palette name, create a new palette object of the chosen type and return it.
    If the offered palette name is invalid, raise an error and end the program. 
If the command-line is empty, provide a default palette. 
    PaletteOne is the default palette. 

-- ImagePainter.py -- 
from tkinter import Tk, Canvas, PhotoImage, mainloop

Create function paint(fractal, palette, window, img) 
    Create tuple coordsX and calculuate the max and min using fractal.centerX and fractal.axisLen
    Create tuple coordsY and calculate the min of Y using fractal.centerY and fractal.axisLen
    Display the image on the screen via canvas (width/height fractal.pixels, bg = "000000")
    Pack the canvas
    Create image (fractal.pixels / 2, fractal.pixels / 2, image=img)
    Calculate pixelSize with max and min of cordsX divided by fractal.pixels
    Create a for loop going through each row in a range(fractal.pixels, 0, -1)
        Create an empty list colorCodes 
        Create another for loop going through each column in range(fractal.pixels)
            Coordinate x = minX + column * pixelSize
            Coordinate y = maxY + row * pixelSize
            iterationCount = fractal.count(complex(x, y)) gives the iteration count to find the appropriate color code
            Use the Pallete.getColor(iterationCount) to get the appropriate color code and append it to colorCodes list
            Append the discovered color code to the empty list colorCode.
        Call the img object from ImagePainter and put the gathered color codes from colorCode into it. 
        Update the window object from ImagePainter
        Print/Call the pixelStatus(row) 

Create function pixelStatus(rows, fractal), same as before but this time using fracta.pixels to generate everything
    portion = (fractal.pixels - row) / fractal.pixels
    statusPercent = '{:>4.0%}'.format(portion)
    statusBar = '=' * int(34 * portion)
    Join the calculuated amount of equal signs to print to the console 

Create function main(fractalInfo)
    Create a variable named "startTime" and equate it to time.time()
    Create a variable named "window" and equate it to Tk() 
    Create variable "img" and equate it to a PhotoImage object with dimensions determined from the pixels key in fractalInfo 
    Call the function paint and run it with the parameters (1, 2, window)
    Create a variable named "endTime" and equate it to time.time()
    Using startTime and endTime, print out how long it took to create the image
    Using img.write, create a png file with the newly created image, extracting its name from the fileName key from the fractalInfo dictionary
    Print a statement informing of the creation and to close the image window to exit the program. 
    Run mainloop() here 


-- Unit Tests -- 

1. Verify that the count methods in the Fractal subclasses are returning integers. 
2. Verify that the lengths of each color palette is correct.
3. Verify that the function getColor from palettes are returning the type string when given an iteration value 
4. Verify that FractalFactory is identifying an incorrect type and raising an error 
5. Verify that FractalFactory is identifying a missing type and raising an error 
6. Verify that a Fractal object cannot be created and an error is raised
7. Verify that PaletteFactory detects an incorrect palette name and raises an error
8. Verify that ImagePainter is printing the correct pixel status bar. 



## Phase 3: Implementation *(15%)*

Changes During Implementation: 
* I realized that I had forgotten to make the constructors for each class private via my UML diagram. So those were 
promptly set back to private, along with xxx (verify). I also realized that the "complexCoord" variable was redundant
since the program ImagePainter would just plug in the complex coordinate after calculating it on its own. Initializing
an additional variable and equating it to the complex coordinate calculated by ImagePainter is redundant. 
* Renamed "HigherMandelbrot" to "FourMandelbrot" to more clearly designate the power by which Mandelbrot has been 
increased. 
* I realized with the initial design of the Palette subclasses that the size of the color palettes would be vastly 
greater than the specified number of iterations given by each file. For the time being, I've implemented
a while loop to verify that the iterations given are devisable by the number of range_to's I'm using. The purpose
of this is to then divide the iteration number given by how many range_to's I do, thus making 
a palette of the appropriate size! Then since the count of the palette is slightly larger
than the iterations specified by the user, that's not really a problem, it's okay to have
some leftover/unused color codes. 
* Besides other small syntax errors on my part, the implementation was overall good and the program
is now running smoothly. 


## Phase 4: Testing & Debugging *(30%)*

Command: [python main.py] 
Bug Found: There was something weird going on with the lengths of my palettes when
they were being called upon. I had set the iteration value to determine the length
of the palettes to be around 5. Originally I had it at 7 and was messing around with 
which colors I wanted to use and such. When I did this initially, however, the 
program blew up and stated the lengths were incorrect. 
Bug Fixed: Upon reviewing the code, there had been a missinput on my end with dividing
the iteration count before shooting them into each range_to line. 

Command: [python main.py]
Bug Found: When computing fractalFactory, I realized that I was incorrectly converting the types of each 
datatype taken from the file and put into fractalInfo; while they did work, there was a chance of it crashing. 
Bug Fixed: This was fixed by using the provided safe_conversation code by DuckieCrp. 

Command: [python main.py]
Bug Found: Initially I had set up a lot of my exceptions as just print("The error that's happening") and usually
a sys.exit(1). The problem with this was I forgot to input sys.exit(1) in various locations, so when I was going
through my debugging phase, there was some confusion because the program wasn't stopping and instead printing
various erroes. 
Bug Fixed: This was fixed by switching all of it to raise exceptions. 

-- Unit Tests -- 

1. Verify that the count methods in the Fractal subclasses are returning integers. This was done by creating Fractal 
objects within the UnitTest file TestFractal.py and detecting the type() of each and asserting that they were 
equal to Fractal.(the anticipated fractal type). Initially this was causing errors because I was trying to 
call the count() method as I was also makeFractal(a valid dictionary). So the program was getting confused; 
when I made the fractal objects before the unit test and fed it to the unit test, the error stopped. 
2. Verify that the lengths of each color palette is correct. This was set up with iteration values that would 
easily divide by the number of color ranges generated within each Palette initializer. This verifies that the lengths
of the palettes will be equal or greater than the iterations which the count function will cycle through. 
3. Verify that the function getColor from palettes are returning the type string when given an iteration value. 
Giving PaletteOne and Two's getColor functions a random iteration value and verifying that it is returning a 
string value. 
4. Verify that FractalFactory is identifying an incorrect type and raising an error. This was pretty straightforward,
simply provided a dictionary which contained an invalid value tied to the "type" key. 
5. Verify that FractalFactory is identifying a missing type and raising an error. This one was also pretty straightforward, 
had dictionaries that didn't have "type" as a key. 
6. Verify that a Fractal object cannot be created and an error is raised. Simply tried to input Fractal.Fractal() with 
the appropriate values, worked swimmingly. 
7. Verify that PaletteFactory detects an incorrect palette name and raises an error. Simply called getColor() with
a string name that didn't equal PaletteOne or PaletteTwo. 
8. Verify that ImagePainter is printing the correct pixel status bar. Since all I needed to see is if it was working,
I had it run using a Mandelbrot object.

In summation, the UnitTests all verified that the exceptions checked throughout the program are covered and reported
appropriate. 


## Phase 5: Deployment *(5%)*


## Phase 6: Maintenance

Reflecting on this project, the most sloppily written portion is likely the ImagePainter. Although I don't believe 
it is that sloppy -- the main part of it that could've been more concise was the calculation of the max and min of 
the x coordinate and the y coordinate. Beyond that, I believe everything else was pretty straight-forward. I do think
I understand nearly all of the program, although I'm still a little vague on the calculations behind the fractals. 
Elsewise, any bugs that may surface should be easy to work through. 

The documentation is fairly straightforward and should make sense to others and myself in the next six months. 

Because of the polymorphism and inheritance design, future new features and implementations should be pretty 
easy to add onto. The program should work despite of the hardware and the operating system. This should also work 
with new versions of Python, so long as the appropriate Color packages and such are downloaded. 
