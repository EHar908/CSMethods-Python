# Bingo! User Manual

## Running The Program

To run this program, first type in the following command into the command line interface:
"python bingo.py"

## Menu And Functionality

When the program starts, you will be brought to the main menu, displaying the title "BINGO!"
Below the title, you should see the following prompt: 

Main menu: 
C) Create a new deck 
X) Exit the program

This is the first of many prompts that will indicate to you for an input command. Simply type in the appropriate input
and the program will run like clockwork. There are two types of prompts in this program: 
- Menu Commands
- Input Commands 
The Menu Commands are used to navigate through the program, and only require for you to type in the indicated 
letters. These letters are case insensitive, so it doesn't matter if you give a capital or lower-case letter. 
Input Commands are used in the creation of the Bingo Cards, and mostly require a numerical integer value. 

Returning to the Main Menu, if you enter in "X", you will exit the program.
If you enter "C", you will begin creating your new deck of bingo cards and the following prompt will appear: 

"Please choose a card size between [3, 16]: "

This input command requires a number between 3 and 16, which includes 3 and 16. 
After you provide a numerical integer value, it will ask 

"Select a number for the size of your deck from [2, 8192]: "

Like the previous prompt, enter numerical integer value from 2 to 8192. 
It will then ask

"Please choose a maximum number between [x, y]: "

The maximum number is the highest possible value which may appear on your Bingo cards. 
The x and y are placeholders for the possible numbers because it is calculated from the size of the card. 
Note: If you create an exceptionally large deck, expect the program to take a little while to finish. 

Congratulations! Your Bingo Deck has been created! You will be brought now to the Deck menu: 

Deck menu:
P) Print a card to the screen
D) Display the whole deck to the screen
S) Save the whole deck to a file       
X) Return to the Main menu

Enter a Deck command (P, D, S, X)

Here, you will now return to Menu commands. 
If you enter in "P", it will prompt you to enter an ID number:

Please provide the card's ID number: 

The ID numbers for each card start from 1 and go up to the maximum amount of cards in your deck. 
For example, if you have a deck of 5 cards, the ID numbers will be 1, 2, 3, 4, and 5. 
Providing the ID number, it will display the card to your screen and return you to the Deck menu. 

If you enter "D", it will display the entire Deck to your screen in order of their IDs.
You are then returned to the Deck menu.

If you enter "S", it will prompt you to provide a name for your file:

Please provide a name for this new file: 

Here you can type whatever name you would like for your Bingo deck file.
Note: The program doesn't verify whether your file name is valid for Python 3. Thus, the program will naturally crash
if you enter an invalid file name. 

It will display what you named your file, and it will appear on your computer before returning you to the Deck menu.

Finally, entering "X" will return you to the Main Menu. 
Note that navigating between the different Deck menu options will not discard or change the Bingo deck you've
created. 
However, if you exit to the Main Menu, it will be discarded. Thus, if you'd like to create several Bingo decks
without needing to restart the program, this is how you can do that. 

## Common Errors and How to Fix Them

Common Error 1: Invalid Inputs
This program includes various prompts indicating your input. For most of these prompts, the program is designed 
to verify that your input is valid. This prevents the program from crashing and there being any errors. In the event
that you do give an invalid input, the prompt will inform you of such and indicate for you to provide another input. 
Some of these prompts will help by clarifying what type of input it needs. 

For example, while responding to the Input Commands for creating your deck, 
if it were to ask for a Card Size between 3 and 16, and you enter a value such as "2", 
it will display the following statement: 

Please provide an integer value from 3 through 16.

Common Error 2: Invalid filenames
As detailed in the guide above, the program doesn't account for filenames which are invalid in Python 3. Due to this, 
the program will naturally crash if you provide such an input. Note that your deck will be lost if this happens. 
So it is recommended to give simple titles to your saved files, containing only letters and/or numbers. 






