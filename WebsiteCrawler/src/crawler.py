#!/usr/bin/python3  	    	       

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
# python -m pip install --user -r requirements.txt  	    	       
from bs4 import BeautifulSoup  	    	       
from urllib.parse import urlparse, urljoin, urldefrag  	    	       
import requests  	    	       
import sys  	    	       
import time

def crawl(url, depth, maxDepth, visitedURLs):
    """  	    	       
    Given an absolute URL, print each hyperlink found within the document.  	    	       
    This function will need more parameters.  	    	       

    Your task is to make this into a recursive function that follows hyperlinks  	    	       
    until one of two base cases are reached:  	    	       

    0) No new, unvisited links are found  	    	       
    1) The maximum depth of recursion is reached  	    	       
    """
    try:
        if depth > maxDepth:
            return
        if url in visitedURLs:
            return
        parseResult = urlparse(url)
        if not parseResult.scheme.startswith("http"):
            return
        else:
            print(depth * "    " + url)
            visitedURLs.add(url)
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            elements = soup.find_all("a")
            for element in elements:
                if not element.get('href'):
                    continue
                defragURL = urldefrag(element.get('href'))
                newURL = urljoin(url, defragURL[0])
                crawl(newURL, depth + 1, maxDepth, visitedURLs)
    except Exception as e:
        print(f"Requests or BeautifulSoup {e}")

def report(timeStart, visitedURLs):
    endTime = time.time()
    totalTime = endTime - timeStart
    print("Visited " + str(len(visitedURLs)) + " unique pages in " + str(totalTime) + " seconds!" )

# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	    	       
if __name__ == "__main__":
    commandInput = sys.argv[1:]
    if len(commandInput) == 0:
        print("Please provide a Starting URL with an optional Maximum Depth.")
        exit(0)  	    	       
    if len(commandInput) == 1:
        url = str(commandInput[0])
        maxDepth = 3
    if len(commandInput) > 1:
        url = str(commandInput[0])
        maxDepth = int(commandInput[1])
    visitedURLs = set()
    if not url.startswith("http"):
        print("Please provide an Absolute URL.")
        exit(0)

    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")  	    	       

    startTime = time.time()
    try:
        crawl(url, 0, maxDepth, visitedURLs)
    except KeyboardInterrupt as e:
        print("Exiting...")
    finally:
        report(startTime, visitedURLs)
