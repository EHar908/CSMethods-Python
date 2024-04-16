# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
*   A detailed written description of the problem this program aims to solve.
Overall, the customer wants this program to produce as many bingo cards as they wish 
along with however many squares they have. However, there are certain parameters 
that should be automatically considered by the program rather than by the user. For
example, for bingo cards with odd numbered grids along either the vertical or horizontal
axis, there should be a center square where a "Free" square should automatically appear. 
Otherwise, if there is no one center square, the program should detect this and 
NOT add in a Free square. Additionally, the program will require a decent sized User Manual, as there 
will be various inputs the user can provide. These inputs are not case sensitive, and there isn't any command-line
prompts that will be offered. 

This is completed through various classes. However, this program had been worked on previously by a team using C++. 
They completed two classes, Menu and MenuOption, leaving bingo, card, deck, and UserInterface to complete. They also 
completed the RandNumberSet class, but the customer has reported a bug to fix. Additionally, 
for what has already been completed and designed by the previous team, the C++ language will need to be translated
to Python 3. While doing this, a UML class diagram will be produced to help any future programmers working with this 
code. 

One of the immediate challenges I see lies with translating C++. I'm not familiar 
with its specific principles/methods, so I'll need to research a fair bit to translate
it all. Additionally, I'm unfamiliar with creating UML documentation, so that'll take some time
to corroborate with the design phase. Beyond all of that, it seems the main challenge with this
project will be understanding the various options of inputs and sizes and such required
by the customer. The basics of converting strings to integers, displaying menus and prompts, and printing the 
final product is all easy enough. Picking the numbers for the bingo cards will also be a challenge. 

Ultimately a good solution will be a quick production of as many bingo cards as the user
wishes, with seamless integration of random numbers and free spaces for odd-numbered cards.

## Phase 1: System Analysis *(10%)*
In terms of data input used to operate the program, all of it should be case-insensitive. 
These will be gathered through interactive menus and prompts. Data will not be gathered through
command-line arguments. For any input requested, the range/options available must be displayed
for them. All user input should be validated. If invalid data is given, prompts should be created
to help the user. 

The data used and how it's handled in the Bingo Cards class is as follows,
* A Bingo Card is an N x N grid, N being the size of the card. The user chooses this value, 
and they will be provided a range from 3 to 16. 
* The numbers on the cards are drawn from a set of integers of 1 to M, M being
the variable chosen by the user. The range of numbers the user can choose depends upon the number
chosen for N -- specifically, the range is [2 * N^2 ... floor(3.9 * N^2)] (inclusive). 
* The program will have to ensure that any number that appears on a bingo card does NOT 
appear twice; it can appear on other bingo cards created. 
* Odd-sized cards will have a FREE! square in the center while even-sized do not.
* The data generated across all the created bingo cards should not change. Additionally,
they should not be lost. 

For the RandomNumberSet,
* It will act as an object used by a card as it is created; in other words, 
the RandomNumberSet will provide the randomized numbers/data across the rows of each 
bingo card as per the parameters described above set by the user. 
The class will not have to retain the sets it produces, 
thus it will only go row by row of each card (however, it will likely 
need to keep track of what numbers it has used as to prevent any repeats). 

For the Decks of Bingo Cards, 
* The number of Bingo Cards in a Deck is chosen by the user from the range [2...8192]
  (inclusive).
* After the deck is created, the data must be able to be shown to the user as one card
at a time or as the entire deck, and the user must be able to put the deck in a file 
named by the user. 
* The way this will be done is through identifiers given to each card, most likely 
an integer from 1 to the size of the deck. As stated before, these cards and their
data should not change or be lost. 
* When a new Deck is created, however, the previous one is deleted. 

The output of the cards should be as follows: 
1. The card's ID number is printed. 
2. The name of each column is centered above its cell. 
3. Columns are separated by pipe characters (|)
4. Rows are bounded by a line of the form +-----+-----+ that is as wide as the entire Card.
5. Cell contents are centered in a field 5 characters wide. 
6. The appearance of the Cards is always the same, regardless of whether they are printed to
the screen or written to a file. 

Examples of every possible size have been given by the customer. Two examples are as follow: 

Odd-sized Card. 
Card #62
   B     I     N     G     O
+-----+-----+-----+-----+-----+
| 10  | 17  | 35  | 50  | 64  |
+-----+-----+-----+-----+-----+
| 15  | 19  | 44  | 56  | 70  |
+-----+-----+-----+-----+-----+
|  8  | 30  |FREE!| 55  | 63  |
+-----+-----+-----+-----+-----+
| 11  | 26  | 32  | 59  | 67  |
+-----+-----+-----+-----+-----+
|  1  | 23  | 45  | 52  | 62  |
+-----+-----+-----+-----+-----+

Even-sized Card. 
Card #10
   B     I     N     G
+-----+-----+-----+-----+
|  8  | 16  | 20  | 27  |
+-----+-----+-----+-----+
|  1  |  9  | 22  | 31  |
+-----+-----+-----+-----+
|  3  | 13  | 19  | 29  |
+-----+-----+-----+-----+
|  7  | 14  | 24  | 26  |
+-----+-----+-----+-----+



## Phase 2: Design *(30%)*
bingo.py--------------------------------------------------------------------------------------------------------

This is the class called to activate the other classes.
Ex: python bingo.py 
bingo.py calls the class UserInterface.py


UserInterface.py (and all affiliated classes)--------------------------------------------------------------------

This class ties everything together; it's the interface that accepts the user input. 
Note: For strings, their input is case-insensitive. 

It will print the program logo and present the main Menu, called from Menu.py. 

From here the user can quit the program or continue on to make a deck.

For the following Deck creation to work, the following functions are created in UserInterface: 
    Create a function named get_int. 
        It contains there inputs: Prompt, low int, high int. 
        This calls the prompt function from MenuOption and inserts the integers low int and high int into the prompt. 
        Then the prompt is printed to the user, typically with an indication to type in an appropriate value in response.
        If they provide a non-numerical input or one that is outside of the given range, 
        repeat the prompt until they do. 
    Create a function name get_string. 
        It contains one input: Prompt.
        This will print a prompt to indicate to the user to provide a string. Return the input. If the input isn't 
        a string, repeat the prompt until they provide one. 
    Create a function called create_deck. 
    Create a function called save_deck. 

If they proceed, the Deck creation menu is created and presented:
    Choose the size of the Bingo Cards. 
        Print a prompt using get_int to collect the value for N. Indicate to the user that this value must lie between
        3 and 16 (inclusive). 
        This value N is used first for the size of the Bingo Cards, determined by N x N. 
    Determine the max number to appear on a Card. This value is stored in M. 
        First calculate the range of possible maximum numbers appropriate for the bingo cards. 
            This uses the given value N in [2 * N^2 ... floor(3.9 * N^2)]
        Then print a prompt using get_int with the ranges calcualted above. Indicate to the user to choose a maximum 
        number from this range. 
    Determine the size of the deck. This value is stored in S. 
        Print a prompt using get_int with the range [2...8192]. 

Once these values N, M, and S are collected, the Card.py class will be called. 
    Define a function that uses N to create an N x N Bingo card. 
        There will be N number of columns by N number of rows.
        Run a loop that prints out a series of dashes, plus signs, and pipes (like "---", "+", and "|") that matches 
        the desired format of the Bingo cards. The number of times this is done will be equal to N + 1.
        In the 0th row of each of these columns, run an if/loop statement to print out a name for the card depdenent 
        upon N. 
            Hard-code in a series of string characters that will be printed out on the range [3..16] chosen for N.
            Example: If N = 5, columns 0-4 should have "BINGO" printed at the top.
    Once the size of the Bingo card is determined, call upon the RandNumberSet.py class. 
        In here, a list will be created that runs through the range [1..M], the maximum value given by the user. The size
        of this list is determined by N, and it will be N number of values take from the range [1...M]. Then
        the list is randomized before being iterated through number by number, inserting them into each spot on the 
        Bingo Card. 
        To make sure that the numbers are oriented largest to biggest from the left-most column to the right, 
        the size of the bingo card N must be known. Then divide up the list into N segments. 
            First sort the function so that we know the randomized numbers have been gathered smallest to largest. 
            Create a loop that iterates a number of times equal to the length of the gathered list of randomized numbers. 
                Within this loop, create new lists that equal 1/N. 
                Determine a way to generate and name these lists without hard coding them in. 
                Exit the loop with the newly created lists. 
    Once the random values have been gathered into lists, place them in order from the 0th/1st column to the Nth column
    after the 0th row is filled. 
        If the size of the Card (N) is odd, replace the center square with the String "FREE!"
    For each finished card is given an ID number.

The Card.py process is repeated a number of times equal to S, the size of the deck, filling it with randomized Bingo 
cards. 

The UserInterface will then hold onto the Deck object until the user returns to the main Menu; at that time the 
Deck is discarded. 

Until then, the user can view each bingo card individually by typing in their ID number, 
they can print the entire deck on their terminal to scroll through, and they can save the deck onto a newly created
file (this uses the get_String method).



## Phase 3: Implementation *(15%)*
* So, I've had to go through a bit of a logic/learning curve while working on this project. Namely, I found it 
extremely confusing trying to work with the given outline. This is most likely a combination of my inexperience
with classes/initializers and misinterpreting the outline for each function in each class. After reviewing the 
concept a couple of times with peers, I feel more confident about it and was able to orient my code into the proper
functions and such. 
* That said, one bit that I had to change was the arguments accepted by Card.py. Originally, it only took the ID number
and the input for the RandomNumberSet. I found this incredibly confusing since the basis for a lot of the coding
in the Card class required knowing its size. So I added the argument "card_size". 
* Also with Card, for some reason the string for "COLUMN_NAMES" was outside the initializer, so I wasn't able 
to call it in the __str__ function. So I put it into the initializer and set it as a self. variable to then be 
called inside __str__. 
* Another thing with the classes, there was another learning curve with the "dunders." Besides just understanding the 
concept of them being a tool for your class to use in its functions so as to avoid repetitive code, 
also had to understand that they could also be called as a function from the class. So like the .shuffle() 
function from RandNumberSet, didn't realize you could do that. 
* An additional bit I should add to the User Manual in regards to their inputs includes empty spaces. 
There is no parameter accounting for whether or not there are empty spaces inserted. Even if they provide 
an input such as " 5", that first empty space will cause an error and the program will request 
for a valid input. I don't believe this is necessarily something I need to edit my code to account for,
hence detailing it in the manual. 
* In order to make the program more secure -- several variables would need to be made private to prevent users from 
manipulating code outside the program's design. This was primarily done for the UserInterface, Deck and Card classes. 



## Phase 4: Testing & Debugging *(30%)*
Initial Testing and Debugging Phase
Preface: There was no special command run to test the program; it was run multiple times to evaluate the following
series of bugs/issues detailed below. This was considered a straight-forward approach to pick out any errors/bugs
as they would be quite quickly/easily seen by the user. 

For clarity, the program was run with the following command: 
* Command Run: python src/bingo.py
Additional commands/runs of the program are included with certain bugs.  

* Example Command Ran: 
"Enter a value between 3 and 16: "
User Input: ""
* Bug Found: Class Dunders and Handling Improper User Input
* Bug Fixed: The three primary dunders in UserInterface.py had to account for the following three potential 
user inputs: A numerical integer input, An empty input, and an input with mixed characters or only characters (special
and ordinary). To avoid repetitive code, __get_str was given the responsibility of verifying that no 
empty input was given. This was then used in __get_int, __print_card, and __save_deck. Because __save_deck 
is set up to naturally crash only if the user provides an invalid name for their new file, checking for an 
empty input was the only parameter set up. For __get_int and __print_card, they each differed enough that 
each had to be given a couple of if-statements in order to verify that the user input was a valid numerical integer. 
This was done by first evaluating if the string input was compromised of all digits and was an integer, and then
if that value rested in the specified ranges. 

* Example Command Ran: 
"Enter a value between 3 and 16: " 
User Input: "2"
* Bug Found: __get_int Dunder and Infinite Loop
* Bug Fixed: With __get_int, it was bugging out and going through an infinite loop because I had the user input
for the integer value OUTSIDE the while loop. So if they ever gave an invalid number and the dunder would try to have 
them provide a new input, there was no line of code allowing them to do so, thus it got stuck in an infinite loop. 
So I simply had to set that as the first line in that loop.

* Bug Found: RandNumSet class had repeating numbers
* Bug Fixed: Reviewing the testing and debugging of the C++ team, it was discovered that the error with RandomNumberSet
was actually really simple. One of their lines included a range at which they were uncertain if  
it was inclusive or exclusive; in an attempt to make it extra-inclusive, they added a +1. However, this was 
unnecessary and was the culprit for the repeating numbers bug occurring. Thus removing it fixed the bug. 

* Command Ran: "P" option after creating the deck 
* Bug Found: Printing a Card or the Entire Deck multiple times with the same deck resulted in Card duplicates 
* Bug Fixed: It seemed that the program as I had set it up would run through the card creating dunder in __str__ 
everytime a card would be printed regardless of whether or not the list full_deck had a card at the called upon index. 
So to fix this, there were two lines of code added onto the front of __str__ that would verify whether or not 
the called upon card already existed in the deck. If it existed, it would return to the deck without 
creating another. If it didn't exist, it would continue with the card creation process as normal. 

runTests Phase
Preface: Similar to the initial debugging phase, the main command used here was simpy running the UnitTests
and reading what the errors were coming out as. This was primarily done in creating the testCard class, but
due to changes that deviated from the original C++ design and thus the layout of the testDeck class provided by 
the customer, there were some changes made there, as well. 

* Command Run: python src/runTests.py

* Bug Found: In testDeck's testCard dunder, it couldn't verify that a card could be accessed from within the deck. 
* Bug Fixed: Because I hadn't created a function card in the Deck class, the original "deck#.card(index)" didn't work. 
To fix this, I rewrote it as "deck#[index]", since I directly created the deck object as a list a list of cards
in full_deck.

* Bug Found: In testCard, collecting the RandNumSet into a set()
* Bug Fixed: I was unfamiliar with this type of variable, and it ended up just needing specific functions to 
manipulate it, such as the .add() function rather than .append() like with a list.



## Phase 5: Deployment *(5%)*




## Phase 6: Maintenance
* Thoughts Regarding Project
** I believe the program overall, while consisting of many moving parts, is fairly written and understandable. 
*** Likely the most confusing part of the program involves the Card class and its __str__ function, where the 
actual card is made. This, however, does make more sense if the desired product is known, thus I don't think it's that bad. 
*** If a bug were to be reported in a few months from now, it would take a decent effort to track it down; of course, 
because the program is comparamentalized into various classes, knowing where the error is occurring would be a bit 
easier. 
** In terms of the documentation, I believe that it will make sense to other programmers and myself in six-months-time. 
The UML diagram is extremely helpful in this regard. 
** For adding new features to the program, I believe it wouldn't be terribly hard, again since everything is in their
own classes and we have it all outlined in the UML diagram. It would still take some work, but it wouldn't be as a 
confusing mess. 
** This program should still work regardless of a computer's hardware and operatring system -- it's fairly simple. 
It's again unclear whether or not upgrading to a different version of Python would impact the code that significantly,
but because this project does involve a fair bit of dunders and math operations, perhaps some code would need to be
altered. 
