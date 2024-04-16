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

import sys
import FractalInformation
import ImagePainter

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in range(len(FractalInformation.allKeys)):
        print("\t{}".format(FractalInformation.allKeys[i]))
    sys.exit(1)

if sys.argv[1] in FractalInformation.mbKeys:
    ImagePainter.main(FractalInformation.mbKeys, sys.argv[1]) #Giving the ImagePainter the appropriate list and the desired image.
elif sys.argv[1] in FractalInformation.phKeys:
    ImagePainter.main(FractalInformation.phKeys, sys.argv[1])
else:
    print("ERROR: " + sys.argv[1] + " is not a valid fractal")
    print("Please choose one of the following:")
    for i in range(len(FractalInformation.allKeys)):
        print("\t{}".format(FractalInformation.allKeys[i]))
    sys.exit(1)

