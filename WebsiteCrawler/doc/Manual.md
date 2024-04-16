# Recursive Web Crawler User Manual

Welcome to the Recursive Web Crawler! 

Firstly, for all commands run for this program, verify that you start in the "/cs1440-assn-6" directory.
Next, this program requires three libraries to operate. For your convenience, these can be downloaded all at once 
through the following command: 

python -m pip install --user -r requirements.txt

Once downloaded, you are ready to run the program! 

When you activate this program, you can provide two arguments: A web URL and a maximum depth. 
The web URL that you provide is where the Recursive Web Crawler begins its search from. It's
important that you provide an Absolute URL and not a Relative URL. 

What's the difference? 
An Absolute URL contains enough information by itself for your browser to locate resources
or websites online. Specifically, they contain (at minimum) a Scheme followed by the token :// followed by 
the hostname/website (including .com, .org, etc). The Scheme is the http, https, ftp, telnet, ssh, etc, seen 
whenever you connect to a website. These are used by your computer to indicate with servers
exactly it will communicate once connected. After the Scheme and token :// is provided, 
the hostname/website is used to identify the machine you're trying to connect to on the internet. 
After this you can provide additional paths, query parameters, and/or fragments.

Examples: 
- https://duckduckgo.com
- http://dwm.suckless.org/tutorial/#content
- https://usu.instructure.com/courses/547414/assignments/2698431?module_item_id=3503120

A Relative URL is missing one or more of the three requirements (Scheme, ://, hostname). 
They do not contain enough information for the program to work with. 

Examples: 
- duckduckgo.com
- assignments/2698431?module_item_id=3503120
- #content 

In summary, the URL you provide must contain at minimum the following: 
[A Scheme, such as http or https] + :// + [Hostname/Website]

The Maximum Depth is used to specify how many levels from the beginning URL you want the 
program to gather other URLs. The output's format is in the form of indentations signifying 
on what levels URLs are found on, so this specifies how many levels the program will explore.

The Maximum Depth you provide MUST be a positive integer, elsewise the program will not run. 

While the absolute URL is necessary for this program to run, you do not need to specify the 
Maximum Depth; by default, it will expand to 3 levels. 

If you attempt to run the program with no command-line arguments provided, you will receive the following error: 
$ python src/crawler.py
Error: no URL supplied

If you attempt to run the program with a relative URL, you will receive the following error: 
$ python src/crawler.py cs.usu.edu
Error: Invalid URL supplied.
Please supply an absolute URL to this program

When your program is working correctly, you will see something like this example:
$ python src/crawler.py https://cs.usu.edu 1
Crawling from https://cs.usu.edu to a maximum distance of 1 link
https://cs.usu.edu
    http://www.usu.edu
    http://usu.edu/azindex/
    http://usu.edu/myusu/
    https://cs.usu.edu/about/index.php
    https://cs.usu.edu/news/main-feed/2018/awards-banquet.php 
    https://engineering.usu.edu/news/main-feed/2019/a-pin.php
    https://engineering.usu.edu/news/main-feed/2019/student-awards.php
    https://cs.usu.edu/students/resources/microsoft-imagine.php
    https://cs.usu.edu/files/pdf/department-map.pdf
    https://appcamp.usu.edu
    https://cs.usu.edu/students/resources/why-comp-sci.php
    https://cs.usu.edu/employment/
    https://www.youtube.com/watch?v=CRYfNVlg4lE&feature=youtu.be
    http://a.cms.omniupdate.com/10?skin=usu&account=usu&site=Engineering_CS&action=de&path=/index.pcf
... (etc) 
Visited 366 unique pages in 1.5355 seconds

Along with the URLs printed and indented, the program provides a report of how many unique URLs were
visited and how long it took. 

Now when you specify higher levels of Maximum Depth, you will see output like this one where it was set to 10:
$ python src/crawler.py http://unnovative.net/level0.html 30
Crawling from http://unnovative.net/level0.html to a maximum distance of 30 links
http://unnovative.net/level0.html
    http://unnovative.net/level1.html
        http://unnovative.net/level2.html
            http://unnovative.net/level3.html
                http://unnovative.net/level4.html
                    http://unnovative.net/level5.html
                        http://unnovative.net/level6.html
                            http://unnovative.net/level7.html
                                http://unnovative.net/level8.html
                                    http://unnovative.net/level9.html
                                        http://unnovative.net/level10.html
                                            http://unnovative.net/level11.html
                                                http://unnovative.net/level12.html
                                                    http://unnovative.net/level13.html
                                                        http://unnovative.net/level14.html
                                                            http://unnovative.net/level15.html
Visited 16 unique pages in 0.7414 seconds

Note that you can specify MaximumDepth to be 0, which will print out only the URL you provided. Understand
that any negative value will not work and the program will not run. 

Now while the program is running, if at anytime you enter Ctrl-C on your keyboard, the program will stop and quit.
(Note: It may requre several attempts for this to work)
It will still print a report of how many pages were visited and in what time, such as with the following example: 

$ python src/crawler.py http://unnovative.net/level0.html 30
Crawling from http://unnovative.net/level0.html to a maximum distance of 30 links
http://unnovative.net/level0.html
    http://unnovative.net/level1.html
        http://unnovative.net/level2.html
            http://unnovative.net/level3.html
                http://unnovative.net/level4.html
                    http://unnovative.net/level5.html
^C
Exiting...
Visited 6 unique pages in 0.9590 seconds

Meanwhile, a common error you may see involves an issue with "Requests" or "BeautifulSoup." 
This may happen when the one of those functions attempts to work with a "broken website." 
The program will display a statement about this and continue on until it is finished. 

Example:
$ python src/crawler.py http://cs.usu.edu (Links to an external site.)
Crawling from http://cs.usu.edu to a maximum distance of 3 links
https://cs.usu.edu
    http://www.usu.edu
        http://www.usu.edu/azindex/
            https://my.usu.edu
            http://directory.usu.edu
            http://www.usu.edu/about/
            http://usueastern.edu/about/
            http://www.usu.edu/aa/
            http://www.usu.edu/calendar/academic.cfm
            http://catalog.usu.edu/content.php?catoid=4&navoid=546
Requests or BeautifulSoup ctor() HTTPSConnectionPool(host='catalog.usu.edu', port=443): Max retries exceeded with url: /content.php?catoid=4&navoid=546 (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify       failed')])")))
            http://www.usu.edu/arc/tutoring/
            http://www.usu.edu/arc/
            http://banner.usu.edu
            https://id.usu.edu/Personal/Lookup
Requests or BeautifulSoup ctor() HTTPSConnectionPool(host='myid.usu.edu', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
    ...
Visited 418 unique pages in 228.7696 seconds

Finally, when the crawler comes across a website that is unaccessible (and the reason for such can vary wildly), 
it will attempt to access it for 10 seconds before printing an error message with "Timed Out" near the end and 
moving on. 

Example: 
Requests or BeautifulSoup HTTPSConnectionPool(host='www.tiktok.com', port=443): Read timed out. (read timeout=10)

Alright, you are good to go! Enjoy your crawling!








