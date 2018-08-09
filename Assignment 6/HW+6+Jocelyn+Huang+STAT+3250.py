
# coding: utf-8

# In[97]:

##
## File:           HW+6+Jocelyn+Huang+STAT+3250.py (STAT 3250)
## Topic:          Assignment 6
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3


# The file "timing_log.txt" contains a log of all WeBWorK
# log entries on April 1, 2012.  The entries are organized 
# by line, with each line including the following:
#
#  --the date and time of the entry
#  --a number that is related to the user (but not unique)
#  --something that appears to be the epoch time stamp
#  --a hyphen
#  --the WeBWorK element that was accessed
#  --the "runTime" required to process the problem
#
# Answer the questions below based on "timing_log.txt".
#

import pandas as pd  #imports necessary packages
import numpy as np

entries = open('timing_log.txt').read().splitlines() # read the data and split into individual lines
entr = pd.DataFrame(entries)  # make a dataframe with each of the entries

# entr

# for line in entries:
#     list.append(line.split('/')[1])
# 1. How many log entries were for requests for a PDF version of an
#    assignment?  Those are indicated by "hardcopy" appearing in the 
#    WeBWorK element.

ct = 0 # intialize empty counter
for line in entries:  # for all the entries available
    if line.count("hardcopy") > 0:  # look for string "hardcopy" and if found, then
        ct += 1   # increase count by one
print("Number found:",ct)  # print answer

"""
#1
Number found: 138
"""


# In[98]:

first = entries[0]
first

# 2. What percentage of log entries were for STAT 2120?

cnt = 0 #intialize empty counter
for aline in entries:  # for each entry in entries
    if aline.count("STAT2120") > 0:  # If desired string is found (STAT2120)
#         print(line)
        cnt += 1  # increase the count by 1


entr['sum'] = 1  # add a column of 1's, thereby assigning a 1 to each line of the data
the_n = sum(entr['sum'])  # sum and store up the 1's to find the total number of entries in the data

print("Percentage is:", (cnt/the_n)*100,"%")  # divide the # entries for STAT 2120 over total entries and multiply by 100 to find the percentage

'''
#2
Percentage is: 52.4924392533 %
'''


# In[103]:

# 3. Find the percentage of log entries that came from the student's
#    initial log in.  For those, the WeBWorK element has the form
#
#          [/webwork2/ClassName]
#
#    where "ClassName" is the name of a class.
webwork = []  # intialize empty list
count = 0  #intialize counter
for x in range(len(entries)):  # for all the entries
    lil_list = entries[x].split('[/')[1].split('/]')[0].split('/') # split each line where webwork begins, ends, and split each directory
    webwork.append(lil_list)  # add the split values to our empty list
#     for y in range(len(entries)):
    if len(lil_list) == 2:  # if each line contains exactly 2 list elements/directories, then
            count += 1   # increase the count
# for bline in three:
#     three.split("[/")

print(count/the_n*100,'%')  # divide by total number of entries to find the proportion and multiply by 100 for percentage. 
'''
#3 
3.7921055376 %
'''


# In[100]:

# 4. How many log entries were from instructors performing administrative
#    tasks?  Those are indicated by "instructor" in the 3rd position of
#    the WeBWorK element.
count2 = 0  # empty counter intialized
for z in range(len(webwork)):   # go through the length of the number of entries in webwork
    if "instructor" in " ".join(webwork[z]):   # join each line, and find the prescence of "instructor"
        count2 +=1      # if instructor is found, increase the count by 1
count2 # print the total count
'''
#4
392
'''


# In[105]:

webwork[4][1].split('-')[1]
# webwork[1].split('-')


# In[102]:

# 5. Which hour of the day had the most log entries?  Which had the least?
hours = []  # empty list for holding the hours of log entries
for r in range(len(entries)):
    hour = entries[r].split()[3].split(":")[0] # subsets each line between a space and the first colon (hence, pulling the hour)
    hours.append(hour)  # adds each hour to our empty list
np.unique(hours)  # confirms we found all the values of the hours
ranked_hours = pd.Series(hours).value_counts()  # counts and ranks the quantity of entries per hour
ranked_hours

'''
#5
22    6331
16    6183
21    6113
17    5563
23    5523
20    5116
19    4458
18    4405
15    4325
00    4152
14    4035
13    3722
01    3107
12    2944
02    2600
11    1782
03    1750
10     903
04     819
05     751
08     737
09     649
07     412
06     332
dtype: int64


ANSWER:  The hour with the most log entries was 22, or 10:00pm, and the hour with the least log entries was 06, or 6:00am.
'''


# In[167]:

# 6. How many different classes use the system? (Treat each
#    different name as a different class, even if there is
#    more than one section.  Multiple sections with a single shared 
#    WeBWorK presence is a single class.)


course = [] # creates empty list to hold course values

for m in range(len(webwork)):
    joinedww ="".join(webwork[m])  #takes previous webwork string, and joins lists together. 
    noSPR = joinedww.replace("Spring11","")  #removes webwork and semester values to leave the course number
    noWW2 = noSPR.replace("webwork2-","")
    noww2 = noWW2.replace("webwork2","")
    nosp12 = noww2.replace("Spring12-","")
    nofall08 = nosp12.replace("Fall08-","")
    nofall10 = nofall08.replace("Fall10-","")
    nofall11 = nofall10.replace("Fall11-","")
    nosp10 = nofall11.replace("Spring10","")
    course.append(nosp10[0:8])   #isolates the strings with only the course number
np.unique(course)  #finds the unique values for course number

'''
#6
array(['', '-STAT212', 'APMA1110', 'APMA2120', 'APMA2130', 'APMA308-',
       'APMA3080', 'APMA310-', 'APMA3100', 'CEE2100', 'CEE2100-',
       'CEE2100H', 'CEE2100]', 'CEE2100g', 'CEE2100i', 'CEE2100l',
       'CEE6010', 'CEE6010-', 'CEE6010H', 'MATH1310', 'MATH132-',
       'MATH1320', 'MATH2310', 'MATH3351', 'STAT2120', '] [runTi', 'admin',
       'apma2130'], 
      dtype='<U8')
ANSWER:  There are 15 different classes that use webwork.
      '''


# In[ ]:

# 7. Which 3 classes had the most use?  Answer this two ways:
#    (a) Based on the number of entries in the log file
#    (b) Based on the total "runTime" required.


# In[ ]:

# 8. Determine which 3 classes had the largest average "runTime".  Report
#    the classes and their runTime.


# In[ ]:

# 9. Determine the percentage of log entries that were accessing a problem.  
#    For those, the WeBWorK element has the form
#
#           [/webwork2/ClassName/AssignmentName/Digit/]
#
#    where "ClassName" is the name of the class, "AssignmentName" the
#    name of the assignment, and "Digit" is a positive digit.


# In[1]:

# 10. Find the WeBWorK problem that had the most log entries,
#     and the number of entries.  If there is a tie, list all with the most.
#     (Note: The same problem number from different assignments represents
#     different WeBWorK problems.)

#%%

