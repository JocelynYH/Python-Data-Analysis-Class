
# coding: utf-8

# In[529]:

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
                        names=['Reviewer','Movie','Rating','Date'])  # read the text file

##  (a) Find the date and time of the oldest review, and the 
##      most recent review.  Give the result in the form
##      matching "2016-10-18 17:50:43".  (Times UTC)
reviewsa = reviews # starting a new dataframe to perserve the old data
reviewsa['Date'] = pd.to_datetime(reviewsa['Date'], unit='s') # convert the raw data to a 'datatime' object
reviewsa_sort = reviewsa.sort_values(by='Date') # sort by the new datatimes
# print the oldest review at the top and print the newest review at the bottom
print('Most recent review was on:', reviewsa_sort.iloc[0]['Date'],'.', 'Most recent review was on:', reviewsa_sort.iloc[-1]['Date'],'.')
'''
#1a
Most recent review was on: 1997-09-20 03:05:10 . Most recent review was on: 1998-04-22 23:10:38 .
'''


# In[530]:

##  (b) Determine the median date and time for the reviews.
##      Give the result in the form "Tuesday October 18 2016 17:50:43"
##      (Times UTC)

import datetime # load datetime
reviews = pd.read_csv('reviews.txt', 
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date']) # Reread the text to revert the format of the Date column
reviewsb = reviews # store original data under new dataframe

format = "%A %B %d %Y %H:%M:%S" # store the format to use in later lines

# find the median of the timestamps, then clean the value to an integer in order to change its format to a datetime
pd.to_datetime(int(np.median(reviews['Date'])), unit='s').strftime(format)
'''
#1b 
The median is Monday December 22 1997 21:42:24
'''


# In[284]:

##  (c) Find the average rating for each month of the year.

# split the formatted Date column into Day, Month, Date, Year, and Time, and store each respectively in separate columns
reviewsb["Day"] = pd.Series(reviewsa["Date"].apply(lambda x: x.split()[0]))
reviewsb["Month"] = pd.Series(reviewsa["Date"].apply(lambda x: x.split()[1]))
reviewsb["date"] = pd.Series(reviewsa["Date"].apply(lambda x: x.split()[2]))
reviewsb["Year"] = pd.Series(reviewsa["Date"].apply(lambda x: x.split()[3]))
reviewsb["Time"] = pd.Series(reviewsa["Date"].apply(lambda x: x.split()[4]))
reviewsb


group_b = reviewsb.groupby('Month') # group by the Month
dfc = group_b.mean()['Rating']  # grab the Ratings by Month and calculate their means
dfc
'''
#1c
Month
April        3.574848
December     3.580388
February     3.455009
January      3.397730
March        3.548831
November     3.559842
October      3.591421
September    3.540125
Name: Rating, dtype: float64
'''


# In[ ]:

##  (d) Determine which day of the week produced the most reviews.
pd.Series(reviewsb['Day']).value_counts().head(1)  # count the number of reviews for each Day, and isolate the first value, with the most reviews
'''
#1d
Wednesday, with 16621 reviews
Wednesday    16621
Name: Day, dtype: int64
'''


# In[ ]:

##  (e) Determine the date and time of the first review for the 5 reviewers 
##      who had the most reviews.

# # group_rank = reviewsb.groupby(reviewsb['Reviewer'])
# # group_rank[0:5]
# reviewsb['Reviewer'].value_counts()
# grouprank = reviewsb.groupby(reviewsb['Reviewer'])
# grouprank.count( )
# # grouprank.sort_values(grouprank['Reviwer'])


# # count = 0 
# # for x in range(len(reviewsb)):
# #     if reviewsb['Reviewer'][x] == 405: 
# #         count += 1
        
# # print(count)

pd.Series(reviewsb['Reviewer']).value_counts().head(5).index  # count the number of reviews by Reviewer number, and grab the index of  the top 5
405# for subset for which reviewer you're looking for, sort reviews by date, then grab the oldest (last) review. 
print("The first review of the top reviewer is:", reviewsa[reviewsa['Reviewer'] == top5[0]].sort_values(by='Date').iloc[-1]['Date'])
print("The first review of the 2nd top reviewer is:", reviewsa[reviewsa['Reviewer'] == top5[1]].sort_values(by='Date').iloc[-1]['Date'])
print("The first review of the 3rd top reviewer is:", reviewsa[reviewsa['Reviewer'] == top5[2]].sort_values(by='Date').iloc[-1]['Date'])
print("The first review of the 4th top reviewer is:", reviewsa[reviewsa['Reviewer'] == top5[3]].sort_values(by='Date').iloc[-1]['Date'])
print("The first review of the 5th top reviewer is:", reviewsa[reviewsa['Reviewer'] == top5[4]].sort_values(by='Date').iloc[-1]['Date'])

'''
#1e
The first review of the top reviewer is: Friday January 23 1998 10:05:43
The first review of the 2nd top reviewer is: Wednesday March 04 1998 04:08:59
The first review of the 3rd top reviewer is: Wednesday April 01 1998 16:49:31
The first review of the 4th top reviewer is: Monday December 15 1997 03:50:20
The first review of the 5th top reviewer is: Tuesday October 14 1997 10:17:46
'''


# In[516]:

## 2. The questions below require the file 'pizza_requests.txt' seen 
##    previously.  All questions refer to the date and time given in 
##    the variable "unix_timestamp_of_request_utc" for each request.

##  (a) Find the date and time of the oldest request, and the 
##      most recent request.  Give the result in the form
##      matching "2016-10-18 17:50:43".  (Times UTC)

pizza = pd.Series(open('pizza_requests.txt').read().splitlines()) # read and save the text file
pizza


req_data = pizza[pizza.str.contains('requester_received_pizza')] # subset where the data holds whether or not the request was successful or not
req_data = pd.Series(req_data) # convert the subset lines to a series
reqs = req_data.str.split().str[1]  # split the lines and grab the latter portion (with the true or false)
req = reqs.reset_index(drop=True)   # drop the index, so we can later put the data into a dataframe
req

time_data = pizza[pizza.str.contains('unix_timestamp_of_request_utc')]  # subset where the timestamps of each request
time_data = pd.Series(time_data)  # convert data to series
times = time_data.str.split().str[1] # split and grab the timestamp
times = times.reset_index(drop=True) # drop the index, so the timestamps will align with the request data in a dataframe
times

df = pd.DataFrame(columns=['Time','Request']) # create dataframe with columns 'Time' and 'Request'
df['Time'] = times # fill dataframe with times data
df['Request'] = req # fill dataframe with req data
df

df['Time'] = pd.to_datetime(df['Time'], unit='s') # format into strftime 
df

pizza_sort = df.sort_values(by='Time') # sort the dataframe by time
# find the oldest review (first entry) by index and print, and the most recent review (last entry).
print('Oldest review was on:', pizza_sort.iloc[0]['Time'],'.', 'Most recent review was on:', pizza_sort.iloc[-1]['Time'],'.')
'''
#2a
Oldest review was on: 2011-02-14 22:28:57 . Most recent review was on: 2013-10-12 01:30:36 .
In [504]:
'''


# In[548]:

##  (b) Determine the median date and time for the requests.
##      Give the result in the form "Tuesday October 18 2016 17:50:43"
##      (Times UTC)

df['strDate'] = df['Time'].apply(lambda x: x.strftime(format)) # format the timestamps into format to view each day, month, date, year, and time

# split the formatted strDate column into Day, Month, Date, Year, and Time, and store each respectively in separate columns

df["Day"] = pd.Series(df["strDate"].apply(lambda x: x.split()[0]))
df["Month"] = pd.Series(df["strDate"].apply(lambda x: x.split()[1]))
df["date"] = pd.Series(df["strDate"].apply(lambda x: x.split()[2]))
df["Year"] = pd.Series(df["strDate"].apply(lambda x: x.split()[3]))
df["Timest"] = pd.Series(df["strDate"].apply(lambda x: x.split()[4]))
df

tiempo = time_data.str.split().str[1] # take unformatted time data, split it, and pull actual values
tiempo = tiempo.reset_index(drop=True) # drop the index
tiempo = pd.to_numeric(tiempo, downcast='signed') # convert the numbers to straight integers to remove ".0"
df['Tiempo'] = tiempo # add to dataframe
pd.to_datetime(np.median(df['Tiempo']), unit='s').strftime(format) # find the median of the times, and reformat the timestamp
'''
#2b
'Friday July 20 2012 17:54:08'
'''


# In[549]:

##  (c) Determine the number of requests for each hour of the day.  Report
##      the 5 one-hour periods with the most requests, and the number of
##      requests for each.

# split the formatted time data and store Hour, Min, and Sec into separate, respective columns
df['Hour'] = df['Timest'].apply(lambda x: x.split(":")[0])
df['Min'] = df['Timest'].apply(lambda x: x.split(":")[1])
df['Sec'] = df['Timest'].apply(lambda x: x.split(":")[2])

pd.Series(df['Hour']).value_counts().head(5) # count each value in the hour column, and grab the top 5 entries

'''
#2c
00    508
22    497
23    491
21    464
01    441
Name: Hour, dtype: int64
'''


# In[553]:

##  (d) Find the hour of the day that resulted in the highest proportion
##      of successful pizza requests.
fulfilled = df[df['Request']=='true'] # subset and store the request data where the requests were filled
failed = df[df['Request']=='false'] # subset and store the request data where the requests weren't filled


fulfilled = pd.Series(fulfilled['Hour']).value_counts() # count the number of requests filled by hour
failed = pd.Series(failed['Hour']).value_counts() # count the number of requests unfilled by hour

df_requests = pd.DataFrame(columns=['Fulfilled','Failed']) # create a dataframe with columns for filled and unfilled requests
df_requests['Fulfilled'] = fulfilled  # fill column with successful requests, indexed by hour
df_requests['Failed'] = failed  # filled column with unsuccessful requests, indexed by hour

df_requests['Total'] = df_requests['Fulfilled'] + df_requests['Failed'] # horizontally sum columns for total number of requests, add to new column
df_requests['Prop'] = df_requests['Fulfilled'] /df_requests['Total'] # add new column to hold proportion of fulfilled requests over total number of requests
df_requests['Prop'].sort_values().tail(1) # sort proportions and grab the last value (with highest proportion)
'''
#2d
The hour with the highest proportion is 13.
'''


# In[368]:

##  (e) Repeat (d), this time finding the hour with the lowest success rate.

# the needed code is identical to above in 2d

df_requests['Prop'].sort_values().head(1) # grab the first entry (lowest proportion), instead of the late
'''
#2e
The hour with the lowest proportion is 8.
'''

