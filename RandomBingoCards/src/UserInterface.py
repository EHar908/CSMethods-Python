#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       

from math import floor
from Deck import Deck
from Menu import Menu  	    	       
from MenuOption import MenuOption

class UserInterface():
    """  	    	       
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	    	       

    Also provides methods for accepting and validating user input  	    	       
    """

    def __init__(self):  	    	       
        self.__m_currentDeck = None  	    	       
        self.__m_menu = Menu("Main")  	    	       
        self.__m_menu += MenuOption("C", "Create a new deck")  	    	       
        self.__m_menu += MenuOption("X", "Exit the program")

        self.card_size = 0
        self.max_num = 0
        self.num_cards = 0

    def run(self):  	    	       
        """  	    	       
        Return None: present the main menu to the user  	    	       

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	    	       
        """  	    	       

        print("""
 ########   ####  ##    ##   ######     #######   ####
 ##     ##   ##   ###   ##  ##    ##   ##     ##  ####
 ##     ##   ##   ####  ##  ##         ##     ##  ####
 ########    ##   ## ## ##  ##   ####  ##     ##   ##
 ##     ##   ##   ##  ####  ##    ##   ##     ##
 ##     ##   ##   ##   ###  ##    ##   ##     ##  ####
 ########   ####  ##    ##   ######     #######   ####

    Welcome to the DuckieCorp Bingo! Deck Generator""")  	    	       

        while True:  	    	       
            command = self.__m_menu.prompt()  	    	       
            if command.upper() == "C":  	    	       
                self.__create_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __create_deck(self):  	    	       
        """  	    	       
        Return None: Create a new Deck  	    	       

        The Deck is stored in self.__m_currentDeck  	    	       

        """
        self.__card_size = self.__get_int("Please choose a card size between [3, 16]: ", 3, 16)
        self.__num_cards = self.__get_int(f"Select a number for the size of your deck from [2, 8192]: ", 2, 8192)
        self.__max_num = self.__get_int(f"Please choose a maximum number between [{2 * (int(self.__card_size) * int(self.__card_size))}, {floor(3.9 * (int(self.__card_size) * int(self.__card_size)))}]: ", (2 * (int(self.__card_size) * int(self.__card_size))), (floor(3.9 * (int(self.__card_size) * int(self.__card_size)))))

        self.__m_currentDeck = Deck(self.__card_size, self.__num_cards, self.__max_num)
        self.__deck_menu()

    def __deck_menu(self):
        """  	    	       
        Return None  	    	       

        Present the deck menu to user until a valid selection is chosen  	    	       
        """  	    	       
        menu = Menu("Deck")  	    	       
        menu += MenuOption("P", "Print a card to the screen")  	    	       
        menu += MenuOption("D", "Display the whole deck to the screen")  	    	       
        menu += MenuOption("S", "Save the whole deck to a file")  	    	       
        menu += MenuOption("X", "Return to the Main menu")  	    	       

        while True:  	    	       
            command = menu.prompt()  	    	       
            if command.upper() == "P":  	    	       
                self.__print_card()  	    	       
            elif command.upper() == "D":  	    	       
                print(self.__m_currentDeck)
            elif command.upper() == "S":  	    	       
                self.__save_deck()  	    	       
            elif command.upper() == "X":  	    	       
                break  	    	       

    def __get_str(self, prompt): #Perhaps for what to name the file?
        while True:
            input_str = input(prompt)
            if input_str != "":
                return input_str
            print("Please enter an input.")


    def __get_int(self, prompt, lo, hi): #Parameters for the bingo cards
        correct_input = False
        while correct_input == False:
            user_input = self.__get_str(prompt)
            if user_input.isdigit():
                if lo <= int(user_input) <= hi:
                    correct_input = True
                    return int(user_input)
                else:
                    print(f"Please provide an integer value from {lo} through {hi}.")
            else:
                print("Please provide a numerical integer value.")


    def __print_card(self):
        correct_input = False
        while correct_input == False:
            input_id = self.__get_str("Please provide the card's ID number: ")
            if input_id.isdigit():
                input_id = int(input_id)
                if 0 < input_id <= self.__num_cards:
                    correct_input = True
                    print(str(self.__m_currentDeck[input_id]))
                else:
                    print(f"Please provide a valid ID number (1 through {self.__num_cards})")
            else:
                print("Please provide a numerical integer value.")


    def __save_deck(self):  	    	       
        file_str = self.__get_str("Please provide a name for this new file: ")
        print("Your new file name: " + file_str)
        f = open(file_str, "x")
        f.write(str(self.__m_currentDeck))
        f.close()
        return f


