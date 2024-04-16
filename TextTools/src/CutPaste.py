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

def cut(args):
    largestFile = 0 #Determining the largest file to ensure empty columns won't prevent full columns from printing
    numF = [] #Fields specified
    result = [] #The list of lines that are then iterated through
    if args[0] != "-f":
        numF.append(1)
    elif args[0] == "-f": #1,2 -> [1] [2]
        if len(args) == 1:
            usage("A comma-separated field specification is required", "cut")
        checkF = args[1].split(",") # Checking the fields specified
        for element in checkF:
            if not element.isdigit():
                usage("A comma-separated field specification is required", "cut")
            numF.append(int(element))
        numF.sort()
        args = args[2:] #Cutting out the flag and the numbers; just have the files left
    for file in args:
        f = open(file)
        numLines = len(f.readlines()) #Number of lines
        f.seek(0)
        if numLines > largestFile:
            largestFile = (len(numF) * numLines)
        readLines = f.readlines()
        for line in readLines:
            list = line.split(",") #Temporary lists to hold the lines before appending to result
            lenLine = len(list) #Counts the number of objects
            if lenLine < int(numF[len(numF) - 1]):
                print("")
            elif lenLine >= int(numF[len(numF) - 1]): #Accounting for fields outside of the scope of the provided file
                for x in numF:
                    if int(x) <= 0:
                        usage("A comma-separated field specification is required.", "cut")
                    else:
                        result.append(list[int(x) - 1].strip("\n"))
                columnLength = len(numF) #The number of columns present based upon numF
                for product in result:
                    if columnLength > 1:
                        print(product, end=",")
                        columnLength -= 1
                    elif columnLength == 1:
                        print(product)
                        columnLength -= 1
            result = []
        f.close()

def paste(args):
    largestFile = 0
    list = []
    for file in args:
        f = open(file)
        if len(f.readlines()) > largestFile:
            f.seek(0)
            largestFile = len(f.readlines())
        f.seek(0)
        list.append(f)
    for x in range(largestFile):
        numArgs = len(args)
        for file in list:
            if numArgs > 1:
                print(file.readline().strip("\n"), end=",")
            elif numArgs == 1:
                print(file.readline().strip("\n"))
            numArgs -= 1
    for file in list:
        file.close()
