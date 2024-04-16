# Code Smells Report - 5.0

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Copy the offensive code between `` ``` ``
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!

Smell at file [lines xx-yy or general location]

* [Brief description of smell]
* [Code Snippet between triple-backquotes ```]
* [How to resolve]    

### These are some of the code smells you may find in the starter code:

0.  **Magic** numbers
    *   Numeric literals in critical places without any context or meaning
    *   "Does `256` over here have anything to do with the `256` over there?"
1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
2.  **Poorly-named** variables
    *   Short variable names are okay in some contexts:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share **too much information**
    *   When almost every line of code is has an explanatory comment, it is likely true that variable and function names were poorly chosen
    *   Write code that speaks for itself
4.  Comments that **lie**
    *   An out-of-date remark that longer accurately describes the code
    *   Bad advice left by a developer without a clue
5.  Too many arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but left unused
    *   Instead, accumulate parameters into a collection such as a dict
6.  Function/Method that is too long
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"
7.  Complex decision trees
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Has every branch been tested?
8.  Spaghetti code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of 
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   A repeated statement which doesn't have an effect the second time
    *   ```
        i = 7
        print(i)
        i = 7
        ```
    *   Ask yourself whether it makes any difference to be run more than once.
10. Dead code
    *   A piece of code that is not used (usually because it is obsolete)
    *   Blocks of commented-out code that serve no purpose and clutter up the file

If you see something that is not covered on this list, please add it to this report.


### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 32, 34]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first.
    *   ```python
        import mbrot_fractal  	    	       
        import phoenix_fractal as phoenix  	    	       
        import mbrot_fractal  	    	       
        ```
    *   This is easily resolved by deleting the second `import` statement.
    

## Code Smells

Smell at main.py [line 30-34]
* (10) Redundant and dead code: Duplicated "import mbrot_fractal" 
*```
import sys
import mbrot_fractal  	    	       
import phoenix_fractal as phoenix  	    	       
import mbrot_fractal ```
* Delete line 32 instance of "import mbrot_fractal"

Smell at main.py [line 46]
* (2) Poorly named variable: Misspelled and in all caps, also doesn't provide much info on what exactly it does
* ```PHOENX =[] ```
* Rewrite as ```phKeys = []```

Smell at main.py [lines 51-54]
* (3) Poor/Confusing/Redundant Comments
* ```
  MBROTS.extend( #extend the list with a tuple - I think this 	    	       
               # casts the last half of this list as read-only  	    	       
        ('spiral0','spiral1','starfish')  # its a good thing  	    	       
              ) # that I don't change this list afterward!  
  ```
* Remove "I think this casts the last half of this list as ready-only. its a good thing that I don't change this list 
afterward!"

Smell at main.py [lines 71-122]
* (6) The function/method is way too long. This overcomplicates verifying that the input option
is within the list of keys, and the code for it is very convoluted. 
* ```    
  print("ERROR:", sys.argv[1], "is not a valid fractal")    #  	    	       
    print("Please choose one of the following:")             ###  	    	       
    quit = False                                           #######  	    	       
    next = ''                                              #######  	    	       
    iter = 0                                                #####  	    	       
    while not quit:                             #     ## ########### ###  	    	       
        next = PHOENX[iter]                      ### #################### ## #  	    	       
        print("\t%s" % next)                      ###########################  	    	       
                                              # ############################  	    	       
        if PHOENX[iter] == 'shrimp-cocktail': ################################  	    	       
            break                            ####################################  	    	       
                            #    ## #       ###################################  	    	       
        else:               ##########     ######################################  	    	       
            iter += 1     ##############   ####################################  	    	       
                     ########################################################  	    	       
              ######################################## CODE IS ART #########  	    	       
                     ########################################################  	    	       
    exit = None          ############################## (c) 2022 #############  	    	       
    i = 0                 ##############   #####################################  	    	       
    i = 0                   ##########     ####################################  	    	       
    fractal = ''            #    ## #       ####################################  	    	       
                                             #################################  	    	       
    while not exit:                          ################################  	    	       
        print("\t" + MBROTS[i])               #  ############################  	    	       
        if PHOENX[iter] =='shrimp-cocktail':    ######################### ####  	    	       
            if MBROTS[i]  == 'starfish':       ### #  ## ##############   #  	    	       
                                              #             #####  	    	       
                i = i + 1                                  #######  	    	       
                exit = PHOENX[iter] =='shrimp-cocktail'    #######  	    	       
                i -= 1 #need to back off, else index error   ###  	    	       
                exit = exit and MBROTS[i]  == 'starfish'      #
  ```
* Re-write all of this with a simple if-else statement, checking to see if the entered argument exists within 
the fractal lists of Mandelbrot and Phoenix. If they don't, then return an error message and exit the program. 

Smell at mbrot_fractal.py [lines 154-205]
* (8) Spaghetti Code. This code is riddled with too many if/elif statements and unnecessary variables.
* ```
  def colorOfThePixel(c, palette):  	    	       
    """Return the color of the current pixel within the Mandelbrot set"""  	    	       
    global z  	    	       
    z = complex(0, 0)  # z0  	    	       

    global MAX_ITERATIONS  	    	       
    global iter  	    	       

    len = MAX_ITERATIONS  	    	       
    for iter in range(len):  	    	       
        z = z * z + c  # Get z1, z2, ...  	    	       
        global TWO  	    	       
        if abs(z) > TWO:  	    	       
            z = float(TWO)  	    	       
            # XXX: the program used to crash with the error  	    	       
            #   TypeError: 'int' object is not callable  	    	       
            #  	    	       
            # maybe it had something to do with 'len' being an integer variable  	    	       
            # instead of a function variable.  	    	       
            # Somebody from StackOverflow suggested I do it this way  	    	       
            # IDK why, but it stopped crashing, and taht's all that matters!  	    	       
            import builtins  	    	       
            len = builtins.len  	    	       
            if iter >= len(palette):  	    	       
                iter = len(palette) - 1  	    	       
            return palette[iter]  	    	       
        elif abs(z) < TWO:  	    	       
            continue  	    	       
        elif abs(z) > seven:  	    	       
            print("You should never see this message in production", file=sys.stderr)  	    	       
            continue  	    	       
            break  	    	       
        elif abs(z) < 0:  	    	       
            print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	    	       
            sys.exit(1)  	    	       
        else:  	    	       
            pass  	    	       

    # Code borrowed from StackOverflow, comment copied from above  	    	       
    #  	    	       
    # XXX: the program used to crash with the error  	    	       
    #   TypeError: 'int' object is not callable  	    	       
    #  	    	       
    # maybe it had something to do with 'len' being an integer variable  	    	       
    # instead of a function variable.  	    	       
    # Somebody from StackOverflow suggested I do it this way  	    	       
    # IDK why, but it stopped crashing, and taht's all that matters!  	    	       
    import builtins  	    	       
    len = builtins.len  	    	       
    if iter >= len(palette):  	    	       
        iter = len(palette) - 1  	    	       
    return palette[iter]  # The sequence is unbounded ```
* Replace with the following code, which only needs to accept the appropriate complex numbers from the calculated
x/y coordinates associated with the called upon fractal image: 
```
def pickColor(comXY):
    complexNum = complex(0, 0)
    for i in range(111):
        complexNum = complexNum * complexNum + comXY
        if abs(complexNum) > 2:
            return i
    return 110
   ```

Smell at mbrot_fractal.py [lines 298-302 and 310-314]
* (9) Repeated/Redundant Code
* ```       'spiral1': {  	    	       
            'centerX': -0.747,  	    	       
            'centerY': 0.1075,  	    	       
            'axisLen': 0.002,  	    	       
            }, ```

  ```'spiral1': {  	    	       
            'centerX': -0.747,  	    	       
            'centerY': 0.1075,  	    	       
            'axisLen': 0.002,  	    	       
            }, ```
* Remove the second instance of this repeated code. 

Smell at phoenix_fractal.py [lines 118-122]
* (7) Complex decision tree. For only needing to check if the key is in the dictionary, this is way too complex.
* ```
      for key in dictionary:  	    	       
        if key in dictionary:  	    	       
            if key == name:  	    	       
                value = dictionary[key]  	    	       
                return key  	    	
  ```
* Replace with something like this:
```
if argument in dictionary: 
    use the key in ImagePainter 
```

Smell at phoenix_fractal.py [lines 128]
* (5) Too many parameters: A lot of which are unused/pointless 
* ```def makePictureOfFractal(f, i, e, w, g, p, W, s): ```
* Rewrite as ```def paint(fractalList, fractal, image)```

Smell at mbrot_fractal.py [line 74]
* (4) Comments that Lie: The comment lies about the total number of colors in the list "palette"
* ```# This color palette contains 100 color steps.```
* The true total is 111, so simply rewrite 100 as 111. 

Smell at mbrot_fractal.py [lines 50, 114, and 159]
* (0) Magic Number: Numeric literal "MAX_ITERATIONS" redeclared with different integer values. The first of these values
  (-1) is not given any explanation and has no relevance to the rest of the program. 
* ```MAX_ITERATIONS = -1 ``` ```MAX_ITERATIONS = 115``` ```global MAX_ITERATIONS ```
* On line 163, just run the for loop a number of times such that (115, 0, -1). Delete MAX_ITERATIONS.

Smell at mbrot_fractal.py [lines 156-157]
* (1) Global Variable: The variable z in colorOfThePixel is made a global variable. Firstly, if it were really necessary
to this function, it would've been imported in at the very least. But instead, the variable z is immediately changed
to equal complex(0, 0), making the creation of the Global Variable completely redundant!
* ```    
  global z  	    	       
  z = complex(0, 0)  # z0
  ```
* Remove the global variable z. 

