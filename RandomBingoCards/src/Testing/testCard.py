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

import unittest  	    	       

from Card import Card

class TestCard(unittest.TestCase):  	    	       

    def setUp(self):  	    	       
        """  	    	       
        Create no fewer than 5 Card objects to test  	    	       

        Create a mixture of odd and even-sized cards  	    	       
        """  	    	       
        self.c1 = Card(5, 5, 50) #Card size, ID number/Number of Cards, Maximum Number
        self.c2 = Card(4, 25, 40)
        self.c3 = Card(9, 24, 163)
        self.c4 = Card(12, 16, 300)
        self.c5 = Card(15, 23, 500)
        self.c6 = Card(16, 330, 631)


    def test_len(self):
        """Assert that each card's size is as expected"""
        self.assertEquals(len(self.c1), 5)
        self.assertEquals(len(self.c2), 4)
        self.assertEquals(len(self.c3), 9)
        self.assertEquals(len(self.c4), 12)
        self.assertEquals(len(self.c5), 15)
        self.assertEquals(len(self.c6), 16)

    def test_id(self):  	    	       
        """Assert that each card's ID number is as expected"""  	    	       
        self.assertEquals(self.c1.id(), 5)
        self.assertEquals(self.c2.id(), 25)
        self.assertEquals(self.c3.id(), 24)
        self.assertEquals(self.c4.id(), 16)
        self.assertEquals(self.c5.id(), 23)
        self.assertEquals(self.c6.id(), 330)

    def test_freeSquares(self):  	    	       
        """  	    	       
        Ensure that odd-sized cards have 1 "Free!" square in the center  	    	       
        Also test that even-sized cards do not have a "Free!" square by examining the 2x2 region about their centers  	    	       
        """
        self.assertEquals(self.c1.number_at(2, 2), "Free!")

        self.assertNotEqual(self.c2.number_at(1, 1), "Free!")
        self.assertNotEqual(self.c2.number_at(1, 2), "Free!")
        self.assertNotEqual(self.c2.number_at(2, 1), "Free!")
        self.assertNotEqual(self.c2.number_at(2, 2), "Free!")

        self.assertEquals(self.c3.number_at(4, 4), "Free!")

        self.assertNotEqual(self.c4.number_at(5, 5), "Free!")
        self.assertNotEqual(self.c4.number_at(5, 6), "Free!")
        self.assertNotEqual(self.c4.number_at(6, 5), "Free!")
        self.assertNotEqual(self.c4.number_at(6, 6), "Free!")

        self.assertEquals(self.c5.number_at(7, 7), "Free!")

        self.assertNotEqual(self.c6.number_at(7, 7), "Free!")
        self.assertNotEqual(self.c6.number_at(7, 8), "Free!")
        self.assertNotEqual(self.c6.number_at(8, 7), "Free!")
        self.assertNotEqual(self.c6.number_at(8, 8), "Free!")




    def test_no_duplicates(self):  	    	       
        """Ensure that Cards do not contain duplicate numbers"""
        no_dup_1 = True
        s1 = set()
        for i in range(len(self.c1)):
            for j in range(len(self.c1)):
                if self.c1.number_at(i, j) not in s1:
                    s1.add(self.c1.number_at(i, j))
                else:
                    no_dup_1 = False
        self.assertEqual(no_dup_1, True)

        no_dup_2 = True
        s2 = set()
        for i in range(len(self.c2)):
            for j in range(len(self.c2)):
                if self.c2.number_at(i, j) not in s2:
                    s2.add(self.c2.number_at(i, j))
                else:
                    no_dup_2 = False
        self.assertEqual(no_dup_2, True)

        no_dup_3 = True
        s3 = set()
        for i in range(len(self.c3)):
            for j in range(len(self.c3)):
                if self.c3.number_at(i, j) not in s3:
                    s3.add(self.c3.number_at(i, j))
                else:
                    no_dup_3 = False
        self.assertEqual(no_dup_3, True)

        no_dup_4 = True
        s4 = set()
        for i in range(len(self.c4)):
            for j in range(len(self.c4)):
                if self.c4.number_at(i, j) not in s4:
                    s4.add(self.c4.number_at(i, j))
                else:
                    no_dup_4 = False
        self.assertEqual(no_dup_4, True)

        no_dup_5 = True
        s5 = set()
        for i in range(len(self.c5)):
            for j in range(len(self.c5)):
                if self.c5.number_at(i, j) not in s5:
                    s5.add(self.c5.number_at(i, j))
                else:
                    no_dup_5 = False
        self.assertEqual(no_dup_5, True)

        no_dup_6 = True
        s6 = set()
        for i in range(len(self.c6)):
            for j in range(len(self.c6)):
                if self.c6.number_at(i, j) not in s6:
                    s6.add(self.c6.number_at(i, j))
                else:
                    no_dup_6 = False
        self.assertEqual(no_dup_6, True)

if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
