#!/usr/bin/env python3  	    	       


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
import Phoenix
import Palette
import FractalInformation


# autocmd BufWritePost <buffer> !python3 runTests.py  	    	       

class TestPhoenix(unittest.TestCase):
    def test_pickColorReturnInt(self):
        self.assertEqual(type(Phoenix.pickColor(complex(0, 0))), int)
        self.assertEqual(type(Phoenix.pickColor(complex(-0.751, 1.1075))), int)
        self.assertEqual(type(Phoenix.pickColor(complex(-0.2, 1.1075))), int)
        self.assertEqual(type(Phoenix.pickColor(complex(-0.75, 0.1075))), int)
        self.assertEqual(type(Phoenix.pickColor(complex(-0.748, 0.1075))), int)

    def test_colorOfThePixelPhoenix(self):
        self.assertEqual(Phoenix.pickColor(complex(0, 0)), 5)
        self.assertEqual(Phoenix.pickColor(complex(-0.751, 1.1075)), 0)
        self.assertEqual(Phoenix.pickColor(complex(-0.2, 1.1075)), 1)
        self.assertEqual(Phoenix.pickColor(complex(-0.750, 0.1075)), 34)
        self.assertEqual(Phoenix.pickColor(complex(-0.748, -0.1075)), 101)
        self.assertEqual(Phoenix.pickColor(complex(-0.75625, 0.078125)), 101)
        self.assertEqual(Phoenix.pickColor(complex(-0.75625, -0.234375)), 32)
        self.assertEqual(Phoenix.pickColor(complex(0.33749, -0.625)), 2)
        self.assertEqual(Phoenix.pickColor(complex(-0.678125, -0.46875)), 101)
        self.assertEqual(Phoenix.pickColor(complex(-0.406, -0.837)), 1)
        self.assertEqual(Phoenix.pickColor(complex(-0.186, -0.685)), 2)

    def test_phoenixPaletteLength(self):
        self.assertEqual(102, len(Palette.phPalette))

    def test_onlyStringsPhoenixPalette(self):
        if all(isinstance(item, str) for item in Palette.phPalette):
            return True
        else:
            return False

    def test_numberPhoenixFractalsListLength(self):
        self.assertEqual(len(FractalInformation.phKeys), 4)

if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
