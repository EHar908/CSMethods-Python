# Software Development Plan

## Phase 0: Requirements Specification *(10%)*
The task of this program is to analyze a large body of data and to produce a report
of its findings. It will summarize national employment data collected by the U.S. Bureau of
Labor Statistics in 2021. The report will include a summary across all industries and 
a summary across the software publishing industry. 

So conceptually, the solution of this program is an organized output of statistics
taken from a large body of data. A good solution is therefore a list of data with
headers signifying from which areas, corporations, and fields they are associated
with. All of which must be given in a concise, organized format. 

In regards to what I already know how to do, I know how to open files, scan through
files, compare and contrast given strings with text in the file, and working through all of
that through various forms of if, elif, if not, etc statements.

The main challenge I anticipate is figuring out how to scan through the various
files and altogether sifting through such a large amount of data. I know that
in reality it will be rather simple and straight-forward so long as my code
is concise and structured. Thus the main obstacle is to deduce how exactly the
different files in their directories are distinguished from one another. 


## Phase 1: System Analysis *(10%)*
Preface: The data gathered for this program is from the 2021 Bureau of Labor Statistics' 
employment data. The relevant segments prepared for the program were done manually via 
text tools, creating .csv files. For each relevant state, a .csv file for all indusutries was made, 
a complete .csv file was made, a reversed file was made, and a software-industry file was made.

So the primary input of this program is going to be directories. There are 
various directories for different states, their specific industries, 
the software industries tied to them, both of which combined and given in one file or 
in a reversed file. Within each of these directories there are csv files which contains the data. 
So the program will be told to go to a certain directory and begin going through its files. The 
name of the directory shouldn't make any difference in how the code is written; it should be able 
to take the inputed directory and be able to access and work through it. 
The input will be given through the command-line terminal in the format given below:  

src/bigData.py [DATA_DIRECTORY]

Meanwhile, for the desired output of this program, there are example outputs provided by the customer which this 
program needs to match exactly. Thus, a good output involves 1) the appropriate statistics the user 
called for via the directory they gave as an input, and 2) the information needs to be displayed very precisely
in the format the customer gave. Additional forms of output include the amount of time taken to gather and 
organize the data (i.e. how long the program takes to run), 

Some key functions in the program will include using the Report object named 
rpt, which will accept the gathered information of the program bigData as it searches the relevant files; the rpt 
will then take the information and fill it into the format specified later in the output, based upon the year 2021.
Additionally, the files area-titles.csv and 2021.annual.singlefile.csv need to be hard-coded
into the program; not the name of the directory containing them, though. This can be done since this program
is being organized to work with a specific (albeit large) set of data; so long as it can alternate between the 
different directories and their information, it'll be fine. 

Additionally with the area-titles.csv, the report must not include US aggregate data, per-state aggregate
data, nor metropolitan areas. The customer further specified to exclude
- "U.S. combined" and "TOTAL" FIPS areas
- All areas labeled "statewide"
- MicroSAs
- MSAs
- CSAs
- Federal Bureau of Investigation – undesignated

They did clarify to not exclude Puerto Rico, Washington, D.C, and the 
Virgin Islands. 

With the 2021.annual.singlefile.csv, the fields from this file that are 
significant to the report are
- area_fips
- industry_code
- own_code
- total_annual_wages
- annual_avg_emp1v1
- annual_avg_estabs

Additionally, not all lines of this file will have information included in the report. 
It will look for a few data points the customer is interested in, and it will
skip over excluded FIPS areas and lines that don't belong to the sectors 
of the economy the customer is interested in. The program should as well 
seek out the specified area_fips, industry_code, and own_code regardless
of the directory that was specified. For example, if for whatever reason 
data from Utah was found in a directory for Virginia, the program should still
find and take up that Utah information if requested. 

In fact, the format of the original file shouldn't impact the program's ability to 
gather the appropriate information for the output. For example, there are some files
that have been reversed due to the Texttool "tac"; despite this, the program should 
be able to go through the file and gather the information just as it would with a 
file going top from bottom. 

Note: FIPS codes will be used to identify different areas in the data; although they are
quite large and can overlap the same area despite being different codes. This is 
correlated with the area title, and both should be set up in a dictionary. 

 


## Phase 2: Design *(30%)*
In the program bigdata.py: 

    import time, sys, and Report from Report

    Create the variable rpt and assign to it the imported Report function, specifying the year as 2021. 

    Create a function gathering the main name of the directory input 
        Check to make sure that a directory was provided, print a usage message and exit if not provided 

        Print "Reading the databases..." 
        Start a timer to moniter the time taken to search the databases; create a variable before and store it in there. 

        If opening the file 'area-titles.csv' from the inputted directory fails, let the program crash. 
        Convert the file 'area-titles.csv' into a dictionary. 

        If opening the file '2021.annual.singlefile.csv' from the inputted directory fails, let the program crash.
        Fill the Report() for all industries related to the inputted directory's opened annual singlefile. 
            Go line by line, splitting it up into a list. 
                The following values should be added into the rpt Report object. 
                If at the first index the FIPS code matches the industry and software areas 
                    For all industries (if the own code and industry code matches) 
                        Number of areas 
                        Total annual wages 
                        Maximum annual wages 
                            If at the annual wage index it is bigger than the last line's, copy value and FIPS code
                        Total establishments 
                        Maximum establishments
                            If at the establishment index it is bigger than the last line's, copy value and FIPS code 
                        Total employees 
                        Maximum employees
                            If at the employee index it is bigger than the last line's, copy value and FIPS code
                    For the software publishing industry (if the own code and industry code matches) 
                        Number of areas 
                        Total annual wages
                        Maximum annual wages 
                            If at the annual wage index it is bigger than the last line's, copy value and FIPS code
                        Total Establishments
                        Maximum Establishments 
                            If at the establishment index it is bigger than the last line's, copy value and FIPS code 
                        Total Employees 
                        Maximum Employees 
                            If at the employee index it is bigger than the last line's, copy value and FIPS code
        Print the filled rpt 

        End the timer here and store it into the variable 'after.' 
        print out from start to finish how long it took to gather the information using the variables 'before' and 'after' 




In the program Report.py:

    Create a function called IndustryDataSet(): 
        This contains the statistics for an industry provided by the inputted directory. This is gathered before being put into the output related to the file. 
        Create a function that accepts the current file being worked through: 
            Search and gather the following statistics: 
                Number of areas 
                Total annual wages 
                Maximum annual wages 
                Total establishments
                Maximum establishments
                Total employees 
                Maximum Employees 

    Create a class called Report():
        Create a function to accept the industry datasets and format them identically: 
            Gather the information from the file under "all"
            Gather the information from the file under "soft" 
            Gather the year from the file 
        Create a function to collect statistics from multiple industries. 
            Accept the list of information from all industries specified in the bigData() program: 
                Number of areas 
                    Total annual wages
                    Maximum annual wages 
                    Total Establishments
                    Maximum esstablishments 
                    Total Employees 
                    Maximum Employees 
            
    The final report which is printed through printing the program after being called and worked through via bigData.py
    Format: 

    Statistics over all industries in {specified years}:
    =========================================================
    Number of FIPS areas in report       {The gathered data for directory is placed respectively with each category}

    Total annual wages                   {}
    Area with maximum annual wages       {}
    Maximum reported wage                {}

    Total number of establishments       {}
    Area with most establishments        {}
    Maximum # of establishments          {}

    Total annual employment level        {}
    Area with maximum employment         {}
    Maximum reported employment level    {}


    Statistics over the software publishing industry in {specified years}:
    =========================================================
    Number of FIPS areas in report       {}

    Total annual wages                   {}
    Area with maximum annual wages       {}
    Maximum reported wage                {}

    Total number of establishments       {}
    Area with most establishments        {}
    Maximum # of establishments          {}

    Total annual employment level        {}
    Area with maximum employment         {}
    Maximum reported employment level    {}


    Provide a function that allows the user to use the repl in order to get help with using the program. 


## Phase 3: Implementation *(15%)*
Given that I am still new to Python, I kept the design relatively broad to accommodate new code that I wasn't 
familiar with. During my coding on the 10th in bigData, I learned the following: 
- With the str.split() method, you can specify how many times in a given string you want to split it. The reason this 
came up was because with the data taken from area-titles, the fips code and the related area titles were two strings
separated by a comma. However, within the string for the area titles, there would be some that had additional 
commas in there. Therefore, just doing .split(",") wouldn't work because it would end up splitting the string 
for area titles, which we need for the dictionary areaFips. Thus, I learned about maxsplit, which I could equal to 1
and then going from left to right, it would only split the given string when it comes across the first ",", which was 
the main one separating the fips code from the area titles. 
- Additionally, I learned that with the lines from area-titles, the quotation marks would still be included when 
determining whether or not to put them into the dictionary areaFips. Therefore, those quotation marks had to be 
removed; however, rather than using .strip() with them, I learned to instead use .replace('"', ""), essentially
telling the program to get rid of every quotation mark still in the string via replacing it with an empty string. 
- Moving onto the annual singlefile data, implementing the dictionary made from the area titles file in conjunction 
with the two parameters for the general industries and the software industries -- was fairly easy! Initially 
I thought it was a lot more complicated due to the extra commas throughout the annual singefiles, but then I realized
that those are simply used for the csv format and won't actually impact the code -- or at least I believe it won't. 
Will see during phase 4. 
- So I figured out that the rpt objects given in Report.py were essentially the variables used to collect
and print out the information from the given file of the directories. That was a big revelation, cause then 
the only temporary variables I had to create were for finding the areas with the maximum amount of wages, 
establishments, and then employees. In that regard, I had to create additional if statements with those 
variables to keep track as I went through line by line -- so like if through the first line, I find that the statistics
for all industries in that area have a maximum amount of 10,000 establishments, that's the new max value for 
that area and the FIPS code of that area is thus recorded. THEN if while going through a subsequent line
(that is also for all industries) it has more than 10,000 establishments, the FIPS code of that line is copied
and the maximum value of establishments in that file is changed to that new value. Then at the very end,
I use that FIPS code with the previously made dictionary from "area titles" to print out the area with the maximum. 
- Last thing I had to fix up on after doing a couple of tests was inserting the FIPS code of the max values 
into the dictionary -- cause in the event that a given file does not have any software industries or all industries
statistics, that would mean an empty string is being given as a key into the dictionary areaTitles, which causes 
an error. Thus, I inserted additional if statements to verify that the FIPS code is in the dictionary; if it's an 
empty string, it won't attempt to put that as a key into the dictionary, and so the printed string is empty and 
that's perfect. 

  
## Phase 4: Testing & Debugging *(30%)*
- The first test that I ran after the implementation was simply going through DC_complete data. However, it came back
with an error specifically for the own_code and industry_codes. How I had them initially set up was to take the 
number in the list as a conversion to an integer; however, it turned out that some of these codes can actually 
include additional characters, such as "31-33"; thus, the program couldn't just convert "31-33" to an integer 
and then add that to my variable. So what I did was pretty simple: I changed the variables to just accept the strings,
and then if the strings have to match the strings of "10" and "0" or "5112" and "5" rather than their numerical 
counterparts. 
- The other main error was pretty simple, too: the if statement to verify that enough arguments are provided. 
Initially had it as if sys.argv[1] == "":, but then it turned out that didn't work exactly; probably because the 
input of sys.argv isn't exactly a list. Like I tried changing it to sys.argv[2] to double check, but the same error 
came up for that, as well. So I changed it to if len(sys.argv) < 2: which fixed it. 

Besides these bugs, when comparing the output of the program with the output examples provided by the customer, 
it seems to be working perfectly! Examples of the commands used are as follows: 

python src/bigData.py data/DC_all_industries 
python src/bigData.py data/DC_complete 
python src/bigData.py data/DC_reversed 
python src/bigData.py data/DC_software_industry

The rest were tested with near identical commands, simply swapping out the "DC" for the respective state's acronym: 
- HI
- ME
- OH
- USA_full
- UT
- WV

## Phase 5: Deployment *(5%)*

## Phase 6: Maintenance
Reflecting on this project, I'm not sure if there is anything with the code that is too poorly written or 
difficult to understand. What would be the most difficult to understand I think would be the various indexes 
and codes required to extract data from all industries and software industries. Knowing to split up the csv files into
lists line-by-line and then taking out data via indexes is arguably the most complicated part of the program. After 
going through the implementation and debugging phase, I don't believe there's any part that I don't understand; it is
in comparison to previous programs relatively straight-forward; again, the complexity was in the requirements/codes. 
Thus, if a bug were to be reported on this program in the next few months, I don't believe it would be very difficult 
to handle. 

The documentation should make sense to anyone, including myself in six month's time. The plan is a little vague, 
but the implementation phase and the debugging phase should provide the additional details used to finish the code. 

It should be fairly easy to add a new feature to this program later on. Depends of course on the feature, especially 
if it has to do with extracting more data or manipulating the csv codes and such further. 

Upgrading computer would make this program run faster, especially with collecting information from the USA_full 
file. It's hard to say whether or not the program would work come the next version of Python; it does use a lot of 
fairly basic arguments, so I would think so. 

