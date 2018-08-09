##
## File: assignment06.py (STAT 3250)
## Topic: Assignment 6
##

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
# 1. How many log entries were for requests for a PDF version of an
#    assignment?  Those are indicated by "hardcopy" appearing in the 
#    WeBWorK element.
# 2. What percentage of log entries were for STAT 2120?
# 3. Find the percentage of log entries that came from the student's
#    initial log in.  For those, the WeBWorK element has the form
#
#          [/webwork2/ClassName]
#
#    where "ClassName" is the name of a class.
# 4. How many log entries were from instructors performing administrative
#    tasks?  Those are indicated by "instructor" in the 3rd position of
#    the WeBWorK element.
# 5. Which hour of the day had the most log entries?  Which had the least?
# 6. How many different classes use the system? (Treat each
#    different name as a different class, even if there is
#    more than one section.  Multiple sections with a single shared 
#    WeBWorK presence is a single class.)
# 7. Which 3 classes had the most use?  Answer this two ways:
#    (a) Based on the number of entries in the log file
#    (b) Based on the total "runTime" required.
# 8. Determine which 3 classes had the largest average "runTime".  Report
#    the classes and their runTime.
# 9. Determine the percentage of log entries that were accessing a problem.  
#    For those, the WeBWorK element has the form
#
#           [/webwork2/ClassName/AssignmentName/Digit/]
#
#    where "ClassName" is the name of the class, "AssignmentName" the
#    name of the assignment, and "Digit" is a positive digit.
# 10. Find the WeBWorK problem that had the most log entries,
#     and the number of entries.  If there is a tie, list all with the most.
#     (Note: The same problem number from different assignments represents
#     different WeBWorK problems.)

#%%
