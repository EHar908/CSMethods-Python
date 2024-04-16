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

from RandNumberSet import RandNumberSet

class Card():
    def __init__(self, card_size, id_num, max_num):  #Determining the idnum and the "ns"?
        """  	    	       
        Initialize a Bingo! card  	    	       
        """
        self.COLUMN_NAMES = list("BINGODARLYZEMPUX") #Why was this outside of the def__init__?
        self.__size = card_size
        self.__rand_num = RandNumberSet(card_size, max_num)
        self.__rand_num.shuffle()
        self.__current_card = ""
        self.__id_num = id_num


    def id(self):
        return self.__id_num

    def number_at(self, row, col):  #I think call RandNumberSet here to determine the numbers in the rows.
        if (self.__size % 2) != 0: #If the size is not divisible by 2
            if row == col and col == (self.__size // 2): #At the center square of the card
                return "Free!"
        return self.__rand_num[row][col]

    def __len__(self): #Determining the __size of the bingo cards based on user input
        return self.__size

    def __str__(self): #The actual appearance/pattern of the card
        if self.__current_card:
            return self.__current_card
        self.__current_card += "\n"
        self.__current_card += ("Card #" + str(self.__id_num)) #Card ID
        self.__current_card += "\n"
        for i in range(self.__size):
            self.__current_card += f"   {self.COLUMN_NAMES[i]}  " #3 spaces, letter, 2 spaces
        self.__current_card += "\n" #After inserting the first line/title of the card, go to the next line
        for i in range(self.__size):
            self.__current_card += "+" + (self.__size * "-----+") + "\n"
            self.__current_card += "|"
            for j in range(self.__size):
                self.__current_card += (format(str(self.number_at(i, j)), "^5") + "|")
            self.__current_card += "\n"
        self.__current_card += "+" + (self.__size * "-----+") + "\n"
        return self.__current_card

