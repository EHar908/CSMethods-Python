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
import FractalInformation

class TestFractalInformation(unittest.TestCase):
    def test_fractalOptions(self):
        self.assertTrue("phoenix" in FractalInformation.allKeys)
        self.assertFalse("lmaofunnyimage" in FractalInformation.allKeys)
        self.assertTrue("peacock" in FractalInformation.allKeys)
        self.assertFalse("epic" in FractalInformation.allKeys)
        self.assertTrue("monkey-knife-fight" in FractalInformation.allKeys)
        self.assertFalse("tubular" in FractalInformation.allKeys)
        self.assertTrue("shrimp-cocktail" in FractalInformation.allKeys)
        self.assertFalse("what'sthis" in FractalInformation.allKeys)
        self.assertTrue("elephants" in FractalInformation.allKeys)
        self.assertFalse("1323" in FractalInformation.allKeys)
        self.assertTrue("leaf" in FractalInformation.allKeys)
        self.assertFalse(1234 in FractalInformation.allKeys)
        self.assertTrue("mandelbrot" in FractalInformation.allKeys)
        self.assertFalse(3.1 in FractalInformation.allKeys)
        self.assertTrue("mandelbrot-zoomed" in FractalInformation.allKeys)
        self.assertFalse(complex(0, 0) in FractalInformation.allKeys)
        self.assertTrue("seahorse" in FractalInformation.allKeys)
        self.assertFalse("wowza" in FractalInformation.allKeys)
        self.assertTrue("spiral0" in FractalInformation.allKeys)
        self.assertFalse("ayoooo" in FractalInformation.allKeys)
        self.assertTrue("spiral1" in FractalInformation.allKeys)
        self.assertFalse("pogger" in FractalInformation.allKeys)
        self.assertTrue("starfish" in FractalInformation.allKeys)

    def test_fractalKeysAndTypes(self):
        # self.assertTrue(FractalInformation.mbKeys in FractalInformation.allKeys)
        # self.assertTrue(FractalInformation.phKeys in FractalInformation.allKeys)
        listTypes = ['centerX', 'centerY', 'axisLen', 'type']
        for i in FractalInformation.allKeys[:3]:
            self.assertTrue(type(FractalInformation.phKeys[i][listTypes[0]]), float)
            self.assertTrue(type(FractalInformation.phKeys[i][listTypes[1]]), float)
            self.assertTrue(type(FractalInformation.phKeys[i][listTypes[2]]), float)
            self.assertTrue(type(FractalInformation.phKeys[i][listTypes[3]]), int)
        for i in FractalInformation.allKeys[4:11]:
            self.assertTrue(type(FractalInformation.mbKeys[i][listTypes[0]]), float)
            self.assertTrue(type(FractalInformation.mbKeys[i][listTypes[1]]), float)
            self.assertTrue(type(FractalInformation.mbKeys[i][listTypes[2]]), float)
            self.assertTrue(type(FractalInformation.mbKeys[i][listTypes[3]]), int)
