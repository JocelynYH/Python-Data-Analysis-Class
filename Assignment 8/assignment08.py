##
## File: assignment08.py (STAT 3250)
## Topic: Assignment 8
##

## The focus of this assignment is dates.  Not the fruit, but the time
## and date that data is put into a file.

## 1. The questions below require the data frame 'reviews.txt' that
##    is described in the README_assign08.txt file.  You can use the
##    code below to read in the data as a dataframe.

import pandas as pd # load pandas as pd
reviews = pd.read_csv('reviews.txt', 
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date'])

##  (a) Find the date and time of the oldest review, and the 
##      most recent review.  Give the result in the form
##      matching "2016-10-18 17:50:43".  (Times UTC)
##  (b) Determine the median date and time for the reviews.
##      Give the result in the form "Tuesday October 18 2016 17:50:43"
##      (Times UTC)
##  (c) Find the average rating for each month of the year.
##  (d) Determine which day of the week produced the most reviews.
##  (e) Determine the date and time of the first review for the 5 reviewers 
##      who had the most reviews.

## 2. The questions below require the file 'pizza_requests.txt' seen 
##    previously.  All questions refer to the date and time given in 
##    the variable "unix_timestamp_of_request_utc" for each request.

##  (a) Find the date and time of the oldest request, and the 
##      most recent request.  Give the result in the form
##      matching "2016-10-18 17:50:43".  (Times UTC)
##  (b) Determine the median date and time for the requests.
##      Give the result in the form "Tuesday October 18 2016 17:50:43"
##      (Times UTC)
##  (c) Determine the number of requests for each hour of the day.  Report
##      the 5 one-hour periods with the most requests, and the number of
##      requests for each.
##  (d) Find the hour of the day that resulted in the highest proportion
##      of successful pizza requests.
##  (e) Repeat (d), this time finding the hour with the lowest success rate.



