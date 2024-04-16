#!/usr/bin/env python  	    	       

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

import time
import sys
from Report import Report

rpt = Report(year=2021)  	    	       

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: src/bigData.py DATA_DIRECTORY")
        sys.exit(1)

    print("Reading the databases...", file=sys.stderr)  	    	       
    before = time.time()

    areaFips = {}
    d = open(f"{sys.argv[1]}/area-titles.csv")
    d.readline()
    for line in d:
        line = line.strip().replace('"', "")
        area_fips, area_title = line.split(",", maxsplit=1)
        if area_fips.isdigit() and not area_fips.endswith("000"):
            areaFips[area_fips] = area_title
    d.close()

    a = open(f"{sys.argv[1]}/2021.annual.singlefile.csv")
    a.readline() #Skip first line

    all_maxAnnualWage = 0
    all_maxWageFip = ""

    all_maxEstab = 0
    all_maxEstabFip = ""

    all_maxEmployee = 0
    all_maxEmployeeFip = ""

    soft_maxAnnualWage = 0
    soft_maxWageFip = ""

    soft_maxEstab = 0
    soft_maxEstabFip = ""

    soft_maxEmployee = 0
    soft_maxEmployeeFip = ""

    for line in a:
            splitLine = line.replace('"', "").split(",") #.replace to get rid of them dang quotations
            #print(splitLine)
            if splitLine[0] in areaFips:
                own_code = splitLine[1]
                industry_code = splitLine[2]
                if industry_code == "10" and own_code == "0":
                    #All industries portion of data
                    rpt.all.num_areas += 1
                    rpt.all.total_annual_wages += int(splitLine[10]) #Total wages
                    if all_maxAnnualWage < int(splitLine[10]):
                        all_maxWageFip = splitLine[0]
                        all_maxAnnualWage = int(splitLine[10])
                    rpt.all.total_estab += int(splitLine[8])  # Total establishments
                    #print(rpt.all.total_estab)
                    if all_maxEstab < int(splitLine[8]):
                        all_maxEstabFip = splitLine[0]
                        all_maxEstab = int(splitLine[8])
                    rpt.all.total_empl += int(splitLine[9])  # Total employees
                    if all_maxEmployee < int(splitLine[9]):
                        all_maxEmployeeFip = splitLine[0]
                        all_maxEmployee = int(splitLine[9])
                elif industry_code == "5112" and own_code == "5":
                    #Software publishing industry
                    rpt.soft.num_areas += 1
                    rpt.soft.total_annual_wages += int(splitLine[10]) #Total wages
                    if soft_maxAnnualWage < int(splitLine[10]):
                        soft_maxWageFip = splitLine[0]
                        soft_maxAnnualWage = int(splitLine[10])
                    rpt.soft.total_estab += int(splitLine[8])  # Total establishments
                    if soft_maxEstab < int(splitLine[8]):
                        soft_maxEstabFip = splitLine[0]
                        soft_maxEstab = int(splitLine[8])
                    rpt.soft.total_empl += int(splitLine[9])  # Total employees
                    if soft_maxEmployee < int(splitLine[9]):
                        soft_maxEmployeeFip = splitLine[0]
                        soft_maxEmployee = int(splitLine[9])

    a.close()

    after = time.time()  	    	       
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	    	       
    if all_maxWageFip in areaFips:
        rpt.all.max_annual_wage = [areaFips[all_maxWageFip], all_maxAnnualWage]
    if all_maxEstabFip in areaFips:
        rpt.all.max_estab =        [areaFips[all_maxEstabFip], all_maxEstab]
    if all_maxEmployeeFip in areaFips:
        rpt.all.max_empl =          [areaFips[all_maxEmployeeFip], all_maxEmployee]

    if soft_maxWageFip in areaFips:
        rpt.soft.max_annual_wage    = [areaFips[soft_maxWageFip], soft_maxAnnualWage]
    if soft_maxEstabFip in areaFips:
        rpt.soft.max_estab          = [areaFips[soft_maxEstabFip], soft_maxEstab]
    if soft_maxEmployeeFip in areaFips:
        rpt.soft.max_empl           = [areaFips[soft_maxEmployeeFip], soft_maxEmployee]
    # Print the completed report  	    	       
    print(rpt)
