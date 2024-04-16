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
import ImagePainter
import Mandelbrot
import Palette
import FractalInformation

# autocmd BufWritePost <buffer> !python3 runTests.py  	    	       

class TestMandelbrot(unittest.TestCase):
    def test_pickColorReturnInt(self):
        self.assertEqual(type(Mandelbrot.pickColor(complex(0, 0))), int)
        self.assertEqual(type(Mandelbrot.pickColor(complex(-0.751, 1.1075))), int)
        self.assertEqual(type(Mandelbrot.pickColor(complex(-0.2, 1.1075))), int)
        self.assertEqual(type(Mandelbrot.pickColor(complex(-0.75, 0.1075))), int)
        self.assertEqual(type(Mandelbrot.pickColor(complex(-0.748, 0.1075))), int)

    def test_colorOfThePixelMandelbrot(self):
        self.assertEqual(Mandelbrot.pickColor(complex(0, 0)), 110)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.751, 1.1075)), 2)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.2, 1.1075)), 9)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.75, 0.1075)), 30)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.748, 0.1075)), 56)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.7562500000000001, 0.078125)), 38)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.7562500000000001, -0.234375)), 12)
        self.assertEqual(Mandelbrot.pickColor(complex(0.3374999999999999, -0.625)), 10)
        self.assertEqual(Mandelbrot.pickColor(complex(-0.6781250000000001, -0.46875)), 29)
        self.assertEqual(Mandelbrot.pickColor(complex(0.4937499999999999, -0.234375)), 4)
        self.assertEqual(Mandelbrot.pickColor(complex(0.3374999999999999, 0.546875)), 22)

    def test_mandelbrotPalleteLength(self):
        self.assertEqual(111, len(Palette.mbPalette))

    def test_onlyStringsMandelbrotPalette(self):
        if all(isinstance(item, str) for item in Palette.mbPalette):
            return True
        else:
            return False

    def test_numberMandelbrotFractalsListLength(self):
        self.assertEqual(len(FractalInformation.mbKeys), 8)


if __name__ == '__main__':  	    	       
    unittest.main()  	    	       
