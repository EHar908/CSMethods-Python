# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

A customer has requested that the code of the provided, finished program be rewritten and cleaned up, along with 
writing a UML diagram and two User Manuals for programmers and users, respectively. The program is simply named 
"Refactoring" and prints out PNGs of certain complex shapes. There is a specified list of these 
shapes given. 

A good solution to this program is simple: clean up and reorganize the code without altering its functions. 
The best way to go about this without ruining its functionality is to create a folder of its PNG images prior to editing 
any code, then to constantly compare the output of the updated code to its original output. 
If any change is detected, then something has been altered and needs to be reversed. 
The code that will be most often used for this will be ```cmp (image).png backup/(image).png```
while located within the /src directory. 

The primary challenge of this clean-up will be understanding how the program works. I am personally not familiar 
with complex numbers nor the method used here to create complex shapes from them; studying the code and perhaps
doing some online research on those topics will be useful. 
Identifying code smells will be the optimal method of determining what code to change or edit. 


## Phase 1: System Analysis *(10%)*

There is no unique data that must be provided to the program. The user input only determines which type of 
PNG image the program will construct and print out. 

The flow of this program begins in main.py, which imports functions from mbrot_fractal.py and phoenix_fractal.py. 
The output involves three things: a new .png file that is saved to the user's computer, a png display of their 
image being created, and a display informing them how long it took to create the image. 

The first of the algorithms used include imports of tkinter modules, sys, and time. Tkinter is used to create the 
images via their canvas, photo images, mainloop, and tk. Sys is used to provide various additional functions not 
privy to the default methods of Python. Time is used to keep track of how long the program takes to create the images. 
Meanwhile, the program uses a combination of dictionaries with pre-determined, hard-coded information (primarily for 
colors with their hexcode values and the complex values associated with the unique shapes) in order to draw its unique 
shapes. 

Based on all of that, I believe the bulk of the program's function is determining where to print out colors 
based upon the complex numbers/values of its listed shapes. The complexity of that has resulted in the program
being produced with confusing formats, comments, and variables (half unused and others entirely unnecessary). 
Fortunately for the programmer, the functionality of the program is correct -- the overarching design of their
algorithms and functions are correct. However, it is altogether too messy; any modifications or upgrades to this 
program are practically impossible as it stands, and I'd be hard-pressed to believe the original programmer 
could do it themselves. 

## Phase 2: Design *(30%)*
* Main.py
import sys
import FractionalInformation
import ImagePainter
import Phoenix
import Mandelbrot

Verify that the length of the command-line isn't less than two.
    If it is less than two, print "Please provide the name of a fractal as an argument." 
    Print allKeys, thus giving the options they can run for the program. 
    Quit the program here.

Verify that the command given for the program fractal is a valid option
    Do this by seeing if it is inside allKeys list. 
    If it isn't, then print "That is not a valid option," 
        print the list allKeys as the options available to them,
        and quit the program. 

If they've activated the program and given a valid option,
    Check if the command is within mbKeys from FractalInformation.py
        Run ImagePainter with the given command 
    Check if it is within phKeys from FractalInformation.py
        Run ImagePainter with the given command 


* FractalInformation.py
Create dictionary "phKeys" filled with the keys and numbers for the Phoenix images.
Create dictionary "mbKeys" filled with the keys and numbers for the Mandelbrot images.

  
* ImagePainter.py
from tkinter import Tk, Canvas, PhotoImage, mainloop
import FractalInformation
import Phoenix
import Mandelbrot
import Palette 

Create function paint(fractList, fractal, window)
    Create two tuples, one for coordsY and one for coordsX
        coordsX calculated is fractals['centerX'] - (fractals['axisLen'] / 2.0) AND fractals['centerX'] + (fractals['axisLen'] / 2.0)  
        coordsY calculated is fractals['centerY'] + (fractals['axisLen'] / 2.0)  
    Display the image on the screen via canvas (width/height 512 pixels, bg = "000000")
    Pack the canvas
    Create image (256, 256, image=img)
    Create float variable pixelSize and equate it to the absolute value of the max X coordinate minus the min X coordinate divided by 512.
    Create a for loop going through each row in a range(512, 0, -1)
        Create an empty list colorCodes 
        Create another for loop going through each column in range(512)
            A coordinate x = minX + column * pixelSize
            A coordinate y = maxY + row * pixelSize
            Based upon the type of the fractals given, call upon the pickColor() from either Phoenix.py or Mandelbrot.py 
                Based upon the complex values for x and y given to pickColor() in either class, the iteration value is returned
                which is then plugged into palatte to determine what color code we want.
            Append the discovered color code to the empty list colorCode.
        Call the img object from ImagePainter and put the gathered color codes from colorCode into it. 
        Update the window object from ImagePainter
        Print/Call the pixelStatus(row) 

Create function pixelStatus(rows)
    Create a float variable named "portion" and equate it to (512 - rows) / 512
    Create a "status_percent" variable and format portion onto it. 
    Create a variable status_bar and equate it to '=' times the int value of 34 (width of the bar) times portion variable
    Redeclare status_bar as itself formatted onto {:<33}
    return a list of the status_bar's joined together

Create function main()
    Create a variable named "startTime" and equate it to time.time()
    Create a variable named "window" and equate it to Tk() 
    Create variable "img" and equate it to a PhotoImage object with dimensions 512 x 512 pixels. 
    Call the function paint and run it with the parameters (1, 2, window)
    Create a variable named "endTime" and equate it to time.time()
    Using startTime and endTime, print out how long it took to create the image
    Using img.write, create a png file with the newly created image. 
    Print a statement informing of the creation and to close the image window to exit the program. 
    Run mainloop() here 

* Mandelbrot.py
Create function pickColor(parameter comXY = complex of (x,y))
    Create a variable complexNum and equate it to complex(0, 0)
        Create a for loop i in range(101)
            Equate complexNum to complexNum^2 plus comXY
            If the absolute value of complexNum is greater than 2, 
                complexNum equals float(2) 
                If this iteration is >= length of palette (int 115)
                    iteration = length minus 1
                return iteration value
            If the iteration is greater than or equal to the length of palette
                the iteration equals the length of the palette minus one
            return iteration

* Phoenix.py
Create a function pickColor(parameter comXY)
    Create variable julConst equal to complex(0.5667, 0.0)
    Create variable phConst equal to complex(-0.5, 0.0)
    Create variable xyFlipped equal to complex(comXY.imag, comXY.real) (???, since we're doing max of Y)
    Create variable xyPrev = 0+0j
    Equate variable currentXY to xyFlipped
    for loop i in range(102):
        xySave = currentXY
        currentXY equals (currentXY)^2 + julConst + (phConst * xyPrevious)
        xyPrevious equals xySave
        if the absolute value of currentXY is greater than 2: 
            return the value i 
        return integer 101

* Palette.py
Create a list mbPalette filled with hex code for the colors in Mbrot (the images dictionary in the initial project). 
Create a list phPalette filled with hex code for the colors in Phoenix (the f dictionary in the initial project). 

When called upon in ImagePainter, create a function that handles such, taking the current iteration count they're on AND what type of image they're creating.
    Knowing the iteration count and the type of image they're on, first verify that the iteration count is not greater than or equal to the length of the lists.
    Then go into the respective list and use the iteration count to choose which color code. 




* Unit Testing (first draft) 
** TestMandelbrot.py and TestPhoenix.py
Ensure that the palette lists only contain strings 
    if all(isinstance(item, str) for item in mbPalette)
        return True
    if all(isinstance(item, str) for item in phPalette)
        return True
Ensure that the dictionary of fractal configuration information contains the expected number of fractals
    assertEquals(len(mbKeys), 8)
    assertEquals(len(phKeys), 4)
Ensure that each fractal configuration dictionary contains the expected keys, and that the corresponding values are all of the expected types
    Create set containing all of the known strings of ph and mb keys. 
    If a string is within that set, 
        assertEquals that the set of values associated with that key is equal to the expected set of values
        associated with that key. 


## Phase 3: Implementation *(15%)*

The amount of time I spent on the design phase made this phase really straight-forward. 
I did make the following changes: 
* In main.py, the printed list of options were created from a list in FractalInformation named "allKeys".
* In Mandelbrot.py, I realized that I had copied over some redundant if statements that the original programmer
had made because they had their range of the for loop too high. So after fixing the range of the for loop to 111,
there was no need for the 5-8 extra lines of code, and now Mandelbrot in total is only 7 lines. 

During the next spring, I should make sure to make most if not all of the functions private in order to prevent 
the user from tampering with the code prior/while running it. 

## Phase 4: Testing & Debugging *(30%)*

General Debugging: 
* Command: python main.py starfish (along with various print statements in ImagePainter's Paint function and the Mandelbrot and 
Phoenix modules; primarily seeing if the program was gathering the expected lists of Fractal information, then seeing if the 
for loops were properly going through the rows, columns, and finally iterations)
* Bug Found: The image wouldn't print, instead it would only print the first color from the respective palettes. After adding a few print() statements throughout the code, I deduced that 
the for loops created in Mandelbrot and Phoenix were only returning 0 over and over again. 
* Bug Fixed: I realized that the final return of "i", the iteration, was incorrect, and instead should've been the 
end of the palette lists, 101 for phoenix and 110 for MandelBrot. 

* Command: python runTests.py 
* Bug Found: The length of the phPalette wasn't the correct length. Upon further investigation, the last 11 strings of 
color weren't being used at all since in Phoenix.py the range of iterations it goes through makes it impossible to even 
get to those last couple rows of color codes. 
* Bug Fixed: I readjusted the expected length from the phoenix Palette and just removed the unused strings. 

* Command: python runTests.py 
* Bug Found: So with "test_colorOfThePixelPhoenix" and with Mandelbrot, I originally had 
manually found what the returned iteration from pickColor should give and be equal to a specific 
index from the Palette lists. However, there came a point where I thought "There's gotta be an easier 
way.." and thought to use the .index() method in order to have the program find the index for me. 
However, I realized this may cause issues in the future since there are repeated color codes in the palettes. 
* Big Fixed: Just find the specific index since there are copies of color codes across
different ones. 


Unit Tests: 
def testpickColorReturnInt
    Verify that ImagePainter's pickColor() function returns an int value; this allows for the color codes
    from the palettes to be retrieved properly. 

def test_colorOfThePixelPhoenix: (colorOfThePixelMandelbrot acts the same way)
    This test verifies that the function pickColor from Phoenix and Mandelbrot respectively is returning 
    a correct iteration number that matches the index of the desired color from the Phoenix and Mandelbrot 
    palettes. 
    This ensures both the functions of the Phoenix/Mandelbrot modules and the locations of the 
    desired colors in each palette. 

def test_phoenixPaletteLength: (mandelbrotPaletteLength acts the same way)
    This test verifies that the list of colors is at the appropriate/expected length. 
    If it weren't at the appropriate length, this could cause drastic changes to the appearance of 
    the images created, since it would be taking different colors than intended. 

def test_onlyStringsPhoenixPalette: (onlyStringsMandelbrotPalette acts the same way)
    This test verifies that the palettes for each image type only contain strings. 
    This prevents any erroneous data types from popping up and potentially crashing the programming.

def test_numberPhoenixFractalsListLength: (numberMandelbrotFractalsListLength acts the same way)
    This test verifies that the dictionaries for the fractals are of the expected lengths. 

def test_pixelStatus: 
    This verifies that the status bar printed at the same time as the image is created 
    does so correctly and according to the current row on the graph/image the program is on. 

def testfractalOptions: 
    This test verifies that there are no erroneous strings/data types within the FractalInformation
    dictionaries. 

def testFractalKeysAndTypes
    This verifies that all the keys are as expected along with their contents' datatypes. 
    So first create a for loop going through the allKeys list from FractalInformation and compare them to both
    phKeys and mbKeys, verifying that all of them have the correct keys. 
    Then go into each key and verify that the first 3 keys return float datatypes and the 4th key
    returns a string. 


## Phase 6: Maintenance

* Reflecting on this process, I think I've refined the design of the original program pretty well. However, 
there is a part of me anticipating that the methods for calculating the complex values and where they go onto the 
graph could be done a little better -- not sure as of now if there's anything to that. In that same vein, I do 
still feel a bit perplexed by how the complex numbers work, but otherwise I'm pretty familiar with how the program works 
now. I believe I could resolve any bugs that might poke up with how I've simplified/modulated this program. 
* I believe the documentation for this program, I've actually been a bit more specific/clear than with previous projects. 
Especially, I was pretty precise with how many code smells that I found. I think if I were to come back to this program 
in six months, it wouldn't take too long to refamiliarize myself with it. 
* With all of that said, I do think it would be fairly difficult to add additional features IF they're involved
with the images and how they're printed. Otherwise, there are quality of life adaptations that can be put onto this
program, like making the menu more advanced/easier to provide input without having to restart the program every time. 
* The program should work regardless of the operating System and hardware, although it would most likely work faster 
if the technology was better. Again it's hard to say if it would work with the next version of Python; especially 
since this program uses a couple complex algorithms, like with ImagePainter, Canvas, etc. 
