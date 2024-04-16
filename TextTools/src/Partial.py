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

from Usage import usage

def head(args):
    numLine = 0
    refreshNum = numLine
    if args[0] == "-n":
        if not len(args) > 1:
            usage("Number of lines is required", "head")
        elif not int(args[1].isdigit()):
            usage("Number of lines is required", "head")
        numLine = int(args[1])
        refreshNum = numLine
        args = args[2:]
    elif args[0] != "-n":
        numLine = 10
        refreshNum = numLine
    for file in args:
        f = open(file)
        if len(args) > 1:
            print("==> " + file + " <==")
        for line in f:
            if numLine > 0:
                print(line, end='')
                numLine -= 1
        print("")
        numLine = refreshNum
        f.close()


def tail(args):
    numLine = 0
    refreshNum = numLine
    tailList = []
    if args[0] == "-n":
        if not len(args) > 1:
            usage("Number of lines is required", "tail")
        elif not int(args[1].isdigit()):
            usage("Number of lines is required", "tail")
        numLine = int(args[1])
        refreshNum = numLine
        args = args[2:]
    elif args[0] != "-n":
        numLine = 10
        refreshNum = numLine
    for file in args:
        f = open(file)
        if len(args) > 1:
            print("==> " + file + " <==")
        for line in f:
            #line.split()
            if numLine > 0:
                tailList.append(line)
        tailList = tailList[(len(tailList) - numLine):]
        for line in tailList:
            print(line, end='')
        print("")
        numLine = refreshNum
        tailList = []
        f.close()