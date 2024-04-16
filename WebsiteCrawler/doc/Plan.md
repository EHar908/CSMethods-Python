# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

In this project, the customer has requested a "web crawler." This program's purpose is to highlight 
the "branches" which exist across the interconnected world wide web; these branches being websites
containing links to other websites, continuing until it reaches a "dead end" with a website lacking 
any such links. So in other words, a map of connected websites. A user manual is also required along with 
the program. This manual will first direct the user to run setup steps to prepare the program, it will 
explain how to the run the program, describe what they should see when the program runs correctly, and 
what types of common errors they might see if the program runs incorrectly. 

The actual output of this program is fairly straightforward: it will print all links available from the 
starting/given website to the furthest possible website. A good output of this will involve a few things: 
1. No revisited links. It is totally possible that a link found early on in a search can be found again 
on a different website. However, for the sake of not overloading the output with redundant info, these 
should be discarded/ignored. 
2. No unvisited links. If there wasn't a valid link visited, be it that it wasn't even on any of the websites
or for whatever reason that link is just not accessible, it should be not be printed with the rest. 
3. With every "depth", the indentation of each line of output increases. This won't be super clear yet, 
but the deeper down each branch you go, that should be signified by large indentations, so that 
the user can easily distinguish which links are in which depth. 
4. A report of the program's activity. The program will give this report even if it quits on an error. 
This report should contain the following info: 
    a. The amount of time the program ran. 
    b. The number of unique links visited. 
5. If there's any error with the "requests" or "BeautifulSoup4" libraries (refer to Phase 1) an error message 
should be displayed with the current amount of indentation. 

So those are the expected parameters for a good output. With all of that reviewed, I believe the main 
issue to grapple with here will have to do with formatting and working recursively. 



## Phase 1: System Analysis *(10%)*

Firstly, for the sake of designing, implementing, and testing this code, we will be using a variety
of 3rd-party libraries. Specifically it will use the Python's Standard URL Parsing Library, Requests HTTP 
Library and BeautifulSoup HTML Parsing Library. These libraries of code already address elements of this code,
thus saving us time and energy from "re-inventing the wheel." From Python's library, we'll primarily use code
like urlparse() to evaluate whether a URL is absolute or relative. The Requests library provides a simple 
interface for making HTTP requests from a Python program. The BeautifulSoup library provides pluggable 
HTML parser to parse a (possibly invalid) document into a tree representation, and they provide 
useful methods for navigating, searching, and modifying this tree. 

In terms of the code algorithms used in this program, we will be using the sys package in order to gather 
the user's input. The program will verify that there is at least one command line argument given. This first 
argument given is sent to a "crawl" function which will be written as a recursive function. It can use a loop, 
but ultimately the crawl() function will call upon itself over and over until the base parameter is met. Until
then, requests will fetch HTML content from the URLs and BeautifulSoup will find the <a> tags in the HTML content. 
THe URLS will then be manipulated with urlparse, urljoin, and urldefrag (partially to remove fragments 
in order to avoid duplicate visits). 

During all of this, a set will be created to keep track of all the urls visited. This will help crawl "remember"
what URLs have already been visited. This will be decided through whenever requests.get() is successfully used. 
Once this is done, the program must verify whether the URL is a valid one. 
Once a URL is successfully identified as unvisited, it will be printed along with identations multiplied by 
the current depth. Recursively, depth is increased. 

The URLs are thus printed line after line. Afterwards the report will print, including the amount of time and number
of links visited total. 

So altogether, the algorithms will run through the URLs recursively, meanwhile verifying that the URLs are valid 
and accessible. Once the validated URLs are visited, they'll be put into an empty set to verify no repeating URLs, and 
they'll be printed with indentation times the current depth level, meanwhile the program is counting how many URLs are 
successfully visited. Finally, a report of the time and number of links visited total. 



## Phase 2: Design *(30%)*

-- crawler module -- 
Import BeautifulSoup, urllib.parse, requests, sys, time

Call sys.argv and check the number of command-line arguments provided. 
Create empty datafields "StartingURL" and "MaximumDepth"
If there are no command-line arguments given,
    print "Please provide a Starting URL with an optional depth."
If the command-line argument is one, 
    Verify that the URL is valid: 
        See if it's an accessible URL. 
        See if it's an absolute URL or it begins with either http:// or https://)
            Do this by inspecting the ParseResult after using urllib.parse()
            Print an error message to sys.stderr and quit the program if it's not absolute or if it's missing the http:// or https://. 
    Since a MaximumDepth wasn't provided, set it as 3. 
If the command-line argument is two, 
    Verify that the first argument is the StartingURL, and the second argument is the MaximumDepth, which must be a positive integer. 
    If the second argument is not a positive integer, set the MaximumDepth to 3. 
Extra arguments are ignored; the program doesn't exit, there's not message displayed.

Before calling crawl, wrap it within a try/catch block monitoring for KeyboardInterruptions. When this exception rises, 
implement a "finally" block afterwards that calls the report(timeStart, visitedURLs) method; thus, even if the crawl()
function fails, the report is still created:
    Create an empty set "visitedURLs"
    Once StartingURL and MaximumDepth have been assigned, create a float data-field timeStart and begin tracking the time 
    Call the crawl(StartingURL, Depth=0, MaximumDepth, visitedURLs)
Implement down here a list of "catch" blocks. 
    KeyboardInterruption
        Print an error message stating that the user has quit the program. 
        Quit the program.
    General Exceptions 
        Print an error message stating the type of exception caught. 
Implement a "finally" block
    Calls report() 

Create the method crawl(URL, Depth, MaximumDepth, visitedURLs):
    Wrap everything in crawl in a try/catch method
        If depth is greater than MaximumDepth:
            Immediately return. 
        If the URL is in the set visitedURLs:
            Immediately return.
        If the URL is invalid (i.e. it isn't an absolute URL or it misses HTTP or HTTPS): 
            Immediately return.
        Else: 
            print URL with a number of indentations equal to 4 spaces * (Depth)  
            add the URL about to be visited into visitedURLs
            Use the requests library to fetch webpage by URL, storing it into "response"
            Run a for loop going through "response": 
                Scan the resulting HTML for anchor tags <a>. For each one: 
                    If an anchor doesn't have an href attribute, continue to the next iteration of this loop. 
                    If it does, remove the fragment portion of the URL 
                    Determine if the href attribute refers to an absolute URL. 
                        If it doesn't, use urljoin() to make it into an absolute URL with the current URL
                    Call crawl(url, Depth + 1, MaximumDepth, visitedURLs)
    Create a catch block: 
        Exception with requests.get() 
        Exception with BeautifulSoup
            Putting them within the crawl method prevents these exceptions from crashing the program. 

Create the method report(timeStart, visitedURLs):
    Create a double data-field timeEnd and complete tracking time. 
    Calculate and print the amount of time spent by doing timeEnd - timeStart. 
    Print the length of the set visitedURLs
    

## Phase 3: Implementation *(15%)*

* Implementation went well. 

## Phase 4: Testing & Debugging *(30%)*

* The design for this program was relatively straight forward; thus, there weren't many bugs to work through. 
* The main bug came from misuse of the Requests and BeautifulSoup methods. Lines 57-65 contains the end result 
of this process; it wasn't necessarily anything wrong with my design or implementation, ultimately it was my 
lack of experience with these libraries. I was at first unable to store them properly via Requests, and then I had
to double-check the logic behind searching for <a> and "href". Once I understood that the point of crawl was to 
search for "a" so that you could locate "href" which gives you the available URLs, the issue was quickly resolved. 
* The other main issue with the program cropped up when running into broken websites, such as TikTok. So with the 
requests.get() method used, I added a timeout=10 so that after 10 or so seconds, if the requests method can't 
get into the website, it'll move on. I initially was going to include this as a potential error into the try/catch, 
but timeout still prints an additional error message at the very end. 


## Phase 5: Deployment *(5%)*

## Phase 6: Maintenance

* Overall, the sloppiest part of the program is the main method. Otherwise I kept things pretty tidied up with 
the report and crawl methods. I am still confused about how exactly Requests and BeautifulSoup work, specifically 
in regards to all of their methods and such, but at the end of the day I used what I needed so that's not a huge
issue (for now). Future bugs will require a better understanding of the Requests and BeautifulSoup.
* The documentation is concise enough to make sense to anyone else and in the future.
* Additional features to this program will again depend upon becoming more familiar with Requests, BeautifulSoup, 
and a general understanding of information embedded within websites. 
* This program should work if the hardware of the computer is designed, windows operating system, and most likely 
with the next version of python. 
