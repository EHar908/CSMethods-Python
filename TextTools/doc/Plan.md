# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
This project aims to provide programs that will provide basic text processing commands/tools for the user when editing 
their text in their files. Specifically, the programs will include linking text together (cat), linking text together in
reverse (tac), removing selected sections from lines of the file (cut), selecting and pasting lines of files together 
(paste), searching and outputting files/text of a matching pattern (grep), outputting the first part of a file (head), 
outputting the last part of a file (tail), sorting lines of text files (sort), and outputting the word count of a file 
(wc). Overall, the solutions of these programs are outputs which takes the text from the inputted file and creating an 
edited output; the actual files are not changed. A good solution would be these programs working with any if not all 
text files, again returning the edited text as the user desired. 

The parameters of the code necessary for these programs were already provided by a previous coder, so the majority of 
this project will involve the core code that takes the input and returns the correct output. Additionally, 
the program called "driver" (tt.py) will be used all across this project to unify multiple 
tools into a combined interface. This will collect the user's input and dispatch it to the appropriate tools/functions;
however, in the case that invalid input is given, either by too little or incorrect information, an error/info message 
has to be displayed to aid the user. Elsewise the majority of what I know in order to complete this object is rather 
basic -- I know how to open the files, have the programs read through them, etc etc. In that regard, I know that I 
specifically need to only open a file in the mode read-only ("r"), which includes open(). Additionally, the 
command-line interface should appear as 

"$ python3 src/tt.py TOOL [OPTIONS] FILENAME..."

where "Tool options" designates which function (in lowercase) the user wishes to use and "Filename" tells the program 
the pathway to their file (note: do not use input()). Additionally, the program should detect when too few arguments 
for the "tool options" are given and if the specified tool option exists or not.

The main challenge I anticipate involve figuring out the code needed to manipulate the inputted text/files. 
Specifically, which Python 3 functions would be most effective in doing so (since I am not intimiately familiar with 
Python). Thankfully examples have been provided, I'll just have to specify in phase 1 or 2 how specifically I decide 
to go about it. 



## Phase 1: System Analysis *(10%)*
The form of input that the program will receive will include the designated file and the type of 
function that the user wants operated over the file. The expected outputs will depend upon the file submitted and the 
type of "tool option" they decided upon; in any case, a proper output will be the desired edit the user wished to occur 
with the text in their file, copied over, editted, and then provided as an output, the original files never changed.
These outputs will include functions which were listed in requirements specifications, 
which will be listed once more below (skip if you've already read it):

Linking text together (cat), linking text together in reverse (tac), removing selected sections from lines of the 
file(cut), selecting and pasting lines of files together (paste), searching and outputing files/text of a matching 
pattern (grep), outputting the first part of a file (head), outputing the last part of a file (tail), sorting lines of 
text files (sort), and outputting the word count of a file (wc).

Some key functions for these programs will include opening and reading files, converting text to string for 
string-related functions, editing said converted strings through appropriate string functions, and returning the edited 
string as an output for the user to read. As well as integer values for the functions where a value is required. 



## Phase 2: Design *(30%)*
###TextTools function
```
The TextTools function ties in all the other text tool functions by taking in the input of the user and determining
what tool options they want, the files they want them used with, and ultimately the output given. In other words,
everything branches out from the TextTools function. 

User will call the program tt.py through the following command-line: 
"$ python src/tt.py TOOL [OPTIONS] FILENAME..."

It will be important throughout this program to remember the indexes of this input. Because the input is essentially
split up into different indexes that will help the program determine what tool options they want and what files they 
want the tool options to work on. Again, nothing is being changed/editted with the files; the tool options are 
only printing out the desired output that the tool options provide. 

Example: 
Input: python3 src/tt.py cat data/file1
sys.argv = ["tt.py", "cat", "file1"]
tt.py is in the 0th index. 
Cat is in the 1st index.
file1 is in the 2nd index. 
Thus the functions can be designed to detect for matching options in these indexes, being able to call upon
the appropriate tool option and then run the file pathway through to open, copy over, edit, and finally print 
its text. 


Pseudo-code: 
(Importing sys in order to call upon its sys.argv functions/code)
import sys 

(Importing each function from the other programs, tying them to the inputs given to this function) 	       
from Concatenate import cat, tac 
from CutPaste import cut, paste  	    	       
from Grep import grep  	    	       
from Partial import head, tail  	    	       
from Sorting import sort  	    	       
from WordCount import wc  	    	       
from Usage import usage  

if the length of the input given is less than three, there are too few arguments to run this program (need at least the
tool option and the file you want worked on) 
    usage(call upon error message in usage for "Too few arguments")
    exit the program 
elif the length of sys.argv is greater than 2: Make sure they're inputting tt.py and a tool option
    if sys.argv at index 1 == cat: (verify if the tool options designated by the user match with the imported functions)
        run cat(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)   
    elif sys.argv at index 1 == tac: 
        run tac(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)    
    elif sys.argv at index 1 == cut: 
        run cut(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)   
    elif sys.argv at index 1 == paste: 
        run paste(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags 
        and files)   
    elif sys.argv at index 1 == grep: 
        run grep(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)   
    elif sys.argv at index 1 == head: 
        run head(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)   
    elif sys.argv at index 1 == tail: 
        run tail(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)    
    elif sys.argv at index 1 == sort: 
        run sort(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)   
    elif sys.argv at index 1 == wc: 
        run wc(sys.argv at index 2 and onward, thus thus deleting the given tool and only holding the listed flags and
        files)  
else: 
    Detect via if/elif statements which tool option they were trying to call. 
        Call usage(with the matching tool option and thus its description/function here)  
    If/else the tool option they called does not match any of the tool options above, 
        return error message from usage() "You requested an incorrect tool option."
```

###Concatenate function
```
The cat function takes a list of filenames as input.
def cat(filenames):  
    The files are processed one at a time. 	
        Each file is opened in its turn. 
        Lines are read and printed one-by-one with no extra newlines/blanks between the lines. 
        Files are closed after being processed. 
    As soon as an invalid function is encountered the entire program may crash 
        (We will leave the error message to Python instead of writing one) 

The tac function takes a list of filenames as input. 
def tac(filenames):  	
    An empty list is created.    	
    The files are processed one at a time into a list. 
        Each file is opened in its turn. 
        Lines are read and added to the empty list created before the loop. 
        Files are closed after being processed. 
    The empty list now full of concatinated lines from the files are reversed. 
    The reversed list of lines are then printed one at a time through a loop. 

```

###CutPaste function
```
The cut function accepts one or more files as input. 
def cut(files, tool command -f to specify which field to extract):
    Each file is ran through a loop. 
        An empty string columnList is created. 
        Open the file. 
        If -f was NOT called:
            Add the 1st field to the columnList. Thus by default, the 1st field is printed if not specified. 
        elif -f WAS called:
            if multiple fields: 
                Add fields to columnList with "," between each one
                Verify that the lists are sorted in ascending order regardless
                of in what order they were called.  
            elif one field:
                Add specified field to columnList
        print columnList 
   
    
The paste function accepts two or more files as input
def paste(filenames, tool options):
    Each of the filenames are opened and stored as objects into a list. 
    if tool options indicates that the pasted data is going into a NEW FILE: 
        A for loop iterates over each list/file, and each word is sent into the new file. 
        print ""
    If the amount of filenames given is greater than 1: 
        A for loop iterates over each list/file, reading one line from each file and printing it
        with a comma instead of a newline.  
    elif there is only one file or there is only one file left in the list of files: 
        Print the lines from that file but only delete the new line at the end.   
    Outside of this for loop, a newline is printed. 
```

###Grep function
```
The grep function takes a list of filenames, the tool option, and a string input. 
def grep(filenames, string input, tool options): 
    The files are processed one of a time through a loop. 
        The file is opened. 
        Lines are read and split apart into individual words. 
        For each LINE, if a WORD in the LINE matches the string input:
            Print the LINE. (Note that the string input/matching word are case sensitive.)
            Elsewise print an empty string "" 
        If tool options equals "-v" 
            For each LINE, if a WORD in the LINE DOESN'T match the string input:
            Print the LINE.
        Close the file 
```

###Partial function
```
The head function takes a list of files as input. 
def head(filenames, number of lines): 
    The files are processed one at a time. 	
        If there is more than one file in the list: 
            print (filename) banner. Make sure no newlines 
        Each file is opened in its turn. 
        Lines are read and printed out. The function will not print out more than 10 lines 
        unless the user inputs the number of lines they want printed out. 
            Verify no new-lines are being printed out with each print. 
        Files are closed after being processed. 
        
The tail function takes a list of files as input and the number of lines the user wants printed. 
def tail(filenames, number of lines): 
    An emptyList is created. 
    The files are processed one at a time. 	
        If there is more than one file in the list: 
            print (filename) banner. Make sure no newlines 
        Each file is opened in its turn. 
        Lines are added to the emptyList list. 
            Verify no new-lines are being printed out with each print. 
        Files are closed after being processed. 
    Reverse the emptyList. 
    Through a loop, print out the lines of the emptyList up until 10 or less, unless the
    user inputs a custom number of lines they want printed. 
```

###Sorting function
```
The sort function takes one or more files as its input. 
def sort(filenames, tool options):
    The files are ran through a loop: 
        The file is opened.  
        Create the empty list wordList
        Split each line of the file up and run a for loop through each word, adding each
        to the empty list wordList
        Run .sort() on wordList. 
        Print wordList
        Close the file. 

```

###WordCount function
```
The wordcount function takes a list of filenames as input.
def wc(filenames, tool option):
    Create totalLines equal to 0
    Create totalWords equal to 0
    Create totalCharacters equal to 0
    The files are opened and their values printed one at a time.  
        Open the file.  
        Empty integer called lineCount equal to 0. 
        Empty integer called wordCount equal to 0.
        Empty integer called characterCount (bytes) equal to 0.  	
        Each line is ran through a loop:
            The empty list lineCount += 1 for every loop through, counting the lines via 
            each time the loop occurs.
            Add lineCount to totalLines. 
            Increase wordcount by the length of line split up by spaces into each word; thus counting each word. 
            Add wordcount to totalword. 
        Return the cursor to the top of the file. 
        Call a function to read through the entire file, counting its bytes, and add that to characterCount. Add 
        characterCount to totalCharacters. 
        Convert the integers lineCount, wordCount, and characterCount into String and print them in one
        line with the string conversion of the file that was just counted from. 
        Close the file. 
    If there is more than one filename given: 
        Print the string conversions of totalLine, totalCount, and totalCharacter with "totaL"
        at the end. 
     
```

###Usage function
```
The Usage function is already provided, however the way that it functions is that it can be imported and 
called upon as a function throughout the text tools, and they accept two arguments: "Error" and "Tool". 
The error input lets us the programmer write a string statement explaining the error that has occurred, 
and to help out the user, the tool option will be given a string of the current tool option in use, and so
the usage function will return a summary of how to use that text tool. 

So like usage("There are too few arguments here", "cat") would give

There are too few arguments here. 

tt.py cat|tac FILENAME...  	    	       
    Concatenate and print files in order or in reverse

```


## Phase 3: Implementation *(15%)*
The initial implementation of the codes from all across the functions had a few general hiccups: 

- There were various times where I tried to either extract or compare values from a list to another variable
in the program, but I had to remind myself that the text in a list have to be converted to the appropriate value type. 
So like if I were to take list[1] and compare it to an integer value 3, I'd often have to remind myself to then do
int(list[1]) to then maintain things. 
- I realized with the Word Counts function that you could indent code by doing format(string, ">#s"), # being the number
of spaces that I want to indent the printed strings. This was an unforseen tool that I could use to make it far 
more organized and neat. 
- I learned about the function .strip() specifically to prevent new line strings ("\n") from affecting the printed
strings in a list or for loop. Cause ordinarilly, the new line string is actually invisible, and there were a few times
during the debugging process where I couldn't figure out how to prevent that. So this was definately an unforseen
bit of code to use. 
- Another type of function/argument I wasn't aware of was the "if NOT x:" and "if x in y:". These helped out a ton
with 1) checking for any false statements to, especially when designing the error statements and 2) looking for
a value or variable in a list.
- After the design phase, I realized that it's not file.open, it's open(file). 

## Phase 4: Testing & Debugging *(30%)*

Preamble: Test Cases. 
````
All of the "Test Cases" listed for these various functions can be found in the "instructions" file beneath the 
"Code organization" section. Clicking on the .py files beneath the "Modules" list will show the instructions
for the desired outputs for each program. Thus. the testing/debugging for this function followed each of these
tested line of code. For the sake of keeping this file short and concise, go to the instructions file if you'd
like to see the proper outputs for each test case. 
````

###TextTools Function
````
Most of the debugging process for the Text Tools function was more-so understanding how it functioned alongside
the usage function. Initially I thought that I had to create a long list of statements to account for whether
or not the inputed text tool existed or not, like so: 

# else:
#     command = sys.argv[1]
#     if command == "cat":
#         usage("cat")
#     elif command == "tac":
#         usage("tac")

I realized quickly, however, that this was extremely redundant and that it would make far more sense to only ever
call the usage function if either 

1) In tt.py when sys.argv[1] did NOT match any of the elif'd tool options. 
2) If in one of the text tool programs (like cat, tac, etc) if there was too few arguments OR for the programs
that utilized flags if the user didn't correctly give the necessary information. 

So beyond those, the tt.py debugging was fairly minimal and was overall pretty straightforward. 

````

###Concatenate Function
````
Test Cases Used: 
--cat--
python src/tt.py cat data/let3 data/num2
python src/tt.py cat data/complexity
python src/tt.py cat data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8
 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
--tac--
python src/tt.py tac data/let3 data/num2
python src/tt.py tac data/complexity
python src/tt.py tac data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8
 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
--Errors--
python src/tt.py cat data/let3 DOES_NOT_EXIST data/debugging
python src/tt.py tac

````
```` 
- The cat function was fairly starightforward with no real hiccups. 
- The tac function required a bit of work. Initially I thought that I could simply pile everything into a list
and then reverse it, finally printing it outside of the for loop. When I did this, however, it gave an output like 
"['\n', 'c', '\n', 'b', '\n', 'a']['\n', '2', '\n', '1']," which was used from a simple data file called let3.
So rather than running through each independent line, it was compiling everything in the list (including some invisible 
text) and then printing it out as a list. 
-> The solution to this issue was simply taking the reversed list and then running it through its own for loop,
printing out each line. 
- It was then I realized I had missed a step with the instructions and the design -- they wanted the data input 
of each file to be reversed IN ORDER. So that meant I couldn't have the info of the last file added to be 
the first output (i.e. can't do an entire list and then just flip it. Gotta flip each file individually and print). 
This was fairly simple to solve, however, just moving the created empty list to the front of the for loop going through
each file in args and then having the lines printed from the reversed list at the end of that for loop. 
- After trying to run a file that contained sentences through tac, however, I realized then that reversing
the list didn't help because all of the characters in the collected were literally reversed. In other words, 
I want the LINES to be reversed, not the actual text. 
- So I tinkered around and it turned out that "reversedList += line" isn't right, instead doing 
reversedLine.append(line) helps tell the program to append the whole line versus adding it byte by byte (I believe).
````

###Cut and Paste Functions
````
Test Cases Used: 
--Cut--
python src/tt.py cut data/people.csv
python src/tt.py cut -f 2 data/people.csv
python src/tt.py cut -f 2,4 data/people.csv
python src/tt.py cut -f 4,2 data/people.csv
python src/tt.py cut -f 2 data/kids.csv data/people.csv
python src/tt.py cut -f 13 data/people.csv
python src/tt.py cut -f 3 data/kids.csv
--Paste--
python src/tt.py paste data/let3 data/num2
python src/tt.py paste data/num2 data/let3
python src/tt.py paste data/num2 data/let3 data/words5
python src/tt.py paste data/num2 data/words5 data/let3
python src/tt.py paste data/num10
python src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8
python src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8 > data/people.csv
python src/tt.py paste data/num10 data/names10 data/words5 > data/kids.csv
--Error--
python src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity
python src/tt.py cut
python src/tt.py cut -f
python src/tt.py cut -f 0,-1
````
````
CUT FUNCTION
This was definiately the hardest program to create. While there were definately a couple of tricks that I learned
later on that made it a lot easier, my main issue with this program was 1) misunderstanding some of its concepts and
2) over-complicating it with repetitive code. 

For instance, especially with the cut function, I thought that I had to create separate for loops to account for
whether or not they opted to use the flag -f to extract certain fields from the function. And even when I did that, 
I failed to program the functions in a way to where it could iterate through the various lines of the files and 
specifically extract and collect ones based upon their indexes (as specified through the -f flag or the default 
"1st" column). 

That said, when I managed to get everything condensed down and more orderly, there was a major issue with 
the way that I was collecting the lines. See when I would have the function run through a file, I would then
have it gather all of the lines (via readlines()) into an empty list. I would then use a for loop to iterate 
through that list of lines. With each line, I would then split them up and put them into ANOTHER list. I would then 
iterate through the lists after splitting them up by their commas, finally appending parts of the line based upon the 
value x which is extracted by the values given from the -f flag (in other words, I would get the words from a line
based upon the column number that the user wants. This would happen for every single line, thus gathering everything
of the same indexes and preparing to pring them out). However, when I would get to his point, I thought that I could 
immediately start printing out the "result" list as it was. That would only create an output where they were 
still of the same list only bunch up together, not in orderly columns as was required/desired. 

This was fixed through creating a variable and equating it to the length of the list taken from splitting up 
the field numbers that the user wanted. So like for example:

If the user wanted -f 3,4. 
3,4 was put into a list, and then split by their commas, giving
numF = ['3', '4']
Then once I had gathered all of the lines into the "result" list, I then created the integer variable columnLength
and equated it to the length of numF.
columnLength = len(numF) = 2
THEN I created two if statements that would see whether or not columnLength was still larger than 1 or qual to 1. 
For when it was larger than 1, the whole line was printed out and giving a comma at the end. 
For when it was equal to 1, a new line was given at the end. 
At the end of either statement, columnLength would be reduced by 1. Thus, for a single lint printed out, it would 
only end up as long as the number of columns wanted. And since the lists iterated in a way where they gathered 
back and forth between the two fields specified, doing it this way created the visual columns that were desired. 

PASTE FUNCTION
Meanwhile with Paste, the main debuging issue was making sure that the printed values continued to match up 
to the largest file. So like for example, if two files were pasted together and one had 200 bytes and the other 100 
bytes, the original output would only give 100 bytes of each cause that's the most the second file could go. So 
I had to design the program in a way to where the sizes of both files were recorded in a variable largestFile, 
and then so long as x remained in the range of largestFile, it could keep printing the lines of the file, 
even if it was an empty string. 
````

###Grep Function
````
Test Cases Used: 
--Grep--
python src/tt.py grep Blue data/colors8
python src/tt.py grep blue data/colors8
python src/tt.py grep Blue data/colors8
python src/tt.py grep a data/ages8 data/colors8 data/let3
python src/tt.py grep -v a data/ages8 data/colors8 data/let3
python src/tt.py grep rch data/verbs8
python src/tt.py grep -v rch data/verbs8
python src/tt.py grep oo data/words200
--Error--
python src/tt.py grep a data/let3 DOES_NOT_EXIST data/complexity
python src/tt.py grep
python src/tt.py grep pattern
````
````
The main debugging issues with the grep program came again with writing too much code and then not accounting
for changes in the variables given. For instance, I again felt that I had to create two complete copies of the
code for when there was the flag -v and when there wasn't. This was entirely redundent and resulted in 
a few bugs where it would run through and print out results for both conditions. Then with the variables, if I didn't 
adjust the list for when there was and wasn't the flag, the line of files would get messed up, some just forgotten 
about, etc. 

Meanwhile, the actual way that I tried going about scanning for matching words in the lists was 
way too complicated and involved splitting too many lines. Like the final check was:
 
if line.split() == args[0]:
    print(line)

Which was an immediate error. I was trying to go for a way to be able to scan through the entire line and compare it
to the given grep word.  Figuring out that I could use the "if x in y" was a godsend and made the entire function
work more concisely and simply. 

Besides those hiccups, the grep function was a generally straightforward program. 
````

###Partial Functions
````
Test Cases Used: 
--Head--
python src/tt.py head data/let3
python src/tt.py head data/names10
python src/tt.py head data/words200
python src/tt.py head -n 13 data/words200
python src/tt.py head -n 3 data/complexity
python src/tt.py head -n 3 data/ages8 data/names8 data/words200
python src/tt.py head -n 3 data/complexity data/debugging
--Tail--
python src/tt.py tail data/let3
python src/tt.py tail data/words200
python src/tt.py tail -n 4 data/words200
python src/tt.py tail -n 1 data/words200
python src/tt.py head -n 97 data/words200 > first97
python src/tt.py tail -n 17 first97
python src/tt.py tail -n 3 data/ages8 data/names8 data/words200
--Error--
python src/tt.py tail data/let3 DOES_NOT_EXIST data/complexity
python src/tt.py tail
python src/tt.py head -n
python src/tt.py head -n seven
````
````
- There was only really one main issue in debugging this program outside of fixing synatx errors: the values of 
numLine and what not -- which took the designated number of lines that the user wanted to have printed out -- 
would be completely reduced without being reset for the next file (this first happened in the Head function). 
The way that I fixed this was simply making a second variable called "refreshNum" which was copied to be 
the exast same as numLine. Then in the for-loop when numLine was reduced to 0 and the loop was about to happen again,
I equated numLine to refreshNum, effectively refreshing the number. 
- Going over the "Head" function again, however, I realized there were a couple chunks of code that I was implementing
that were unnecessary and only making the program 1.5 times bigger than it needed to be. I trimmed those away and 
made it smaller, but it still seems rather big. Not sure as of yet if there's a way to condense it even further. 
- Okay as of like 10 minutes after finishing that, I just realized I can cut the code in half if I just put the if/elif
statement checking for whether or not there's an "-n" into the same pair of statements.
- Finally with the "Tail" function, using the condensing/overlapping code just described, there was still
an issue with my original approach to this function. For instance, one of the main requirements for this function 
was that the tail could give the final chunk of the file (default 10 lines or x lines designated by the user). 
So initially I thought -- okay, reverse the list of lines in the file, take the top x (or 10) lines, then reverse
that list again and then print. 

For example:
-> Input: 
a 
b
c
-> 1st list: 
a
b
c
-> Reverse that List
c
b
a
-> Take x amount from list (let's say 2 for this example)
c
b
-> Then reverse a final time to return the lines to the original layout
b
c

- This however created a lot of repetitive code that was ultimately unnecessary. Looking back over the program,
I realized that I could get those final few lines by just 1) adding the lines of the file to the list and then 2)
cutting off the necessary amount of lines from the end of the file by doing 
    tailList = tailList[(len(tailList) - numLine):]
It was really astonishing to realize how simple the program really was by just using that line. 

````

###Sorting Function 
````
Test Cases Used:
--Sort--
python src/tt.py sort data/colors8
python src/tt.py sort data/complexity
python src/tt.py sort data/colors8 data/names10
python src/tt.py sort data/complexity data/debugging
python src/tt.py sort data/names10 data/colors8
python src/tt.py sort data/debugging data/complexity
python src/tt.py sort data/random20
python src/tt.py sort data/colors8 > sortedColors8
python src/tt.py tac sortedColors8
--Error--
python src/tt.py sort data/let3 DOES_NOT_EXIST data/complexity
python src/tt.py sort
````
````
The only real bug I ran into was when I sorted the gathered list of lines, I forgot that I had to then run
that list through its own for loop to finally print(line, end='') from list. Besides that, being able to use 
the .sort() function made this arguably the easiest program to develop. 
````

###Word Count Function
````
Test Cases Used:
--Word Count--
python src/tt.py wc data/num2
python src/tt.py wc data/words200
python src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity
python src/tt.py wc data/let3 data/let3 data/let3 data/let3 data/let3
--Error--
python src/tt.py wc data/let3 data/random20 DOES_NOT_EXIST data/dup5
python src/tt.py wc
````
````
- The initial design of the function had the three outputs of the file (line count, word count, and byte count) 
each handled in their own respective for loops. After tinkering around with that design, however, I realized that
you could instead have simply one loop in order to 1) make the code more compact/neat and 2) just have all the values
determined all at once. This worked cause I could simply increase the empty integers wordCount and lineCount at the
same time as I ran each one through a for loop of each line through a file: lineCount increasing by 1  everytime a loop
occurred and wordcount counting the length of the split up line (splitting everything up between spaces, thus containing
a list of only words). Then characterCount could be determiend simply by running .read() with an empty paramater outside
of the loop, automatically scanning and reading ALL of the bytes in the file. 
- The only bug fixes that were needed involved some simple syntax mis-inputs -- putting a paranthesis in the 
print statement in the wrong spot and forgetting to do the length of args in an if statement. 
````

## Phase 5: Deployment *(5%)*

## Phase 6: Maintenance

I believe I've cleaned my code enough to where it isn't entirely sloppy nor hard to understand. However I'd definately
say that hardest to read/follow would be the cut function. Beyond that, I worked on these programs for more hours than
I should've, and I feel pretty confident about how they work. If a bug were to be reported in a few months, I feel
fairly confident in my abilites to address it, especially now with the skills and knowledge I've gained with using
the debugger on Pycharm. 

While I don't think this is the best documentation I've maintained, I believe I make it clear enough to convey the
general outlines and functions of the program so that I and anyone else can understand what any of it is supposed
to do. I think six months from now I'd be able to follow it. 

I believe adding a new feature to this program would be fairly easy, if by new feature we mean a new text tool. If
we were to add further customization to the functions which utilize flags, that would be an entirely different matter. 

I believe the program will continue to work regardless of the hardware and operative system, however it's hard to say
whether or not it'll work on the next version of Python.
