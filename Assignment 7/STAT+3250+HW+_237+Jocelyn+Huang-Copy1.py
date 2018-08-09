
# coding: utf-8

# In[2]:

##
## File:           HW+7+Jocelyn+Huang+STAT+3250.py (STAT 3250)
## Topic:          Assignment 7
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

#### Part 1
##
# Background

# An active thread on Reddit is \Random Acts of Pizza" where a user can put in a request for a pizza to be
# donated by another user. Some requests are granted, others are not. The file pizza_requests.txt includes
# requests from approximately 5600 pizza requests. Data for each request includes a statement describing
# the nature of the request, and various other pieces of information. The file README_pizza.txt gives more
# information about the data set.
# Use the data set to answer the questions below.

import pandas as pd 
import numpy as np # to import numpy
# 1. What proportion of requests were successful? (The requester received pizza.)
pizza = pd.Series(open('pizza_requests.txt').read().splitlines())  #open and read text

req_data = pizza[pizza.str.contains('requester_received_pizza')] #subset lines with the needed data
req_data = pd.Series(req_data) # organize lines


truth = req_data[req_data.str.contains('true')] # find within subset, there requests were filled
print(len(truth)/len(req_data)) # find proportion by taking requests filled over all requests.

'''
#1
0.24634103332745547
'''


# In[3]:

#  2. Find the median account age at the time of request for all requests.


account = pizza[pizza.str.contains("requester_account_age_in_days_at_request")] # subset data at lines with needed data on account age
account = pd.Series(account) # organize data into series
ages = account.str.split().str[1].apply(pd.to_numeric) # split the data and isolate the numerical value for the age.  Also convert strings to numbers
np.median(ages) # find the median of all the numbers

'''
#2
155.64759259259259
'''


# In[4]:

# 3. Divide the requests into those with account age greater than the median found in the previous question,
# and those with account age less than or equal to the median. Find a 95% confidence interval for the
# difference in proportion of successful pizza requests between the two groups.

ages2 = ages.reset_index(drop=True) #reset the index of ages
reqs = req_data.str.split().str[1] # split and isolate the requests to only show true/false if the request was fulfilled or not
reqs2 = reqs.reset_index(drop=True) #reset the index of ages, so then you can put ages2 and reqs2 side by side


df = pd.DataFrame(columns=['Age','Request']) # create empty dataframe
df['Age'] = ages2 # fill dataframe with ages
df['Request'] = reqs2  # fill dataframe with request data

sorteddf = df.sort_values(by = 'Age') # sort dataframe by age account
req_received = sorteddf[sorteddf['Request']=='true'] # subset data where requests were fulfilled
old = sorteddf[sorteddf['Age']>155.64759259259259] # isolate the oldest accounts
young = sorteddf[sorteddf['Age']<=155.64759259259259] # isolate the youngest accounts

oldfulfilled = old[old['Request']=='true'] # find old accounts where requests were fulfilled
youngfulfilled = young[young['Request']=='true'] # find newer accounts where requests were fulfilled

n = len(sorteddf) # number of all requests submitted
n1 = len(old) # number of old accounts
n2 = len(young) # number of newer accounts
p1 = len(oldfulfilled)/n1 # proportion of old accounts & fulfilled requests over old accounts
p2 = len(youngfulfilled)/n2 # proportion of new accounts & fulfilled requests over new accounts

ci_upper = (p1-p2) + 1.96*np.sqrt(((p1*(1-p1))/n1)+((p2*(1-p2))/n2)) # upper bound
ci_lower = (p1-p2) - 1.96*np.sqrt(((p1*(1-p1))/n1)+((p2*(1-p2))/n2)) # lower bound
print(ci_lower, ci_upper)


# In[5]:

# 4. Determine the percentage of request texts that mention the word \student" or \children". (Upper or
# lower case.)
req_text = pizza[pizza.str.contains('request_text')][::2] # subset necessary data, but only select every other b/c of data duplication in the "edited form"
req_text = req_text.str.lower() # convert to lowercase, so we don't miss "Student" vs. "student"
pleading = req_text[req_text.str.contains('children')|req_text.str.contains('student')] # look for instances with either word
print(len(pleading)/len(req_text)*100, "%") # find the percentage of instances over all requests


# In[6]:

# 5. Determine the number of requests from Canada.
pizza_lower = pizza.str.lower() # convert all data to lowercase, to avoid errors due to capitalization or lack thereof
maple = pizza_lower[pizza_lower.str.contains('request_title')][pizza_lower.str.contains('canada')]  # search for Canada as a location within the post title
maple 
'''
#5 
103'''


# In[7]:

# 6. Find a 95% confidence interval for the proportion of successful pizza requests donated anonymously.

user = pizza[pizza.str.contains("giver_username_if_known")] # subset lines with needed data
user= user.str.split().str[1] # split and subset data from data header
user = user.reset_index(drop=True) # drop the index, so data can be added into a dataframe beside the received request data

df6 = pd.DataFrame(columns=['Received','User Known']) # create a dataframe 
df6['Received'] = reqs2 # fill dataframe with previous data on whether or not request was fulfilled
df6['User Known'] = user # fill dataframe with data on whether donor was anonymous or not
successes = df6[df6['Received']=='true'] # subset data where requests were fulfilled
success_anon = successes[successes['User Known']=='"N/A"']  # further subset to find fulfilled requests with anonymous donors

pp = len(success_anon)/len(successes) # proportion of fulfilled requests and anonymous over all fulfilled requests

ci_upper6 = pp + (1.96*(np.sqrt((pp*(1-pp))/len(successes)))) # upper bound
ci_lower6 = pp - (1.96*(np.sqrt((pp*(1-pp))/len(successes)))) # lower bound
print(ci_lower6, ci_upper6)


# In[52]:

# 7. Find the maximum number of subReddits subscribed to by a single requestor.


import re

joined = " ".join(pizza)  # make a massive block of text

submission = pd.Series(joined.split('%%%%%%%%%%')) # split into each submission
# run and create a function that isolates data between brackets, remove brackets and other non important characters, then split between each subreddit
lengths = submission.apply(lambda x: len(str(re.findall('{.+}', x)).replace('{', "").replace('}', "").replace('[', "").replace(']', "").replace("'", "").split()))
np.max(lengths)    # find the maximum

'''
#7
235
'''


# In[84]:

# 8. Determine the number of distinct subReddits among all the requests, and the number of times that
# each appears. Place a table of the 10 most frequently occurring (in order, starting with most frequent)
# in your Python code file, organized
# subReddit01, count01
# subReddit02, count02
# subReddit03, count03
# subReddit04, count04
# subReddit05, count05
# subReddit06, count06
# subReddit07, count07
# subReddit08, count08
# subReddit09, count09
# subReddit10, count10
# Also write to file all of the subReddits and their corresponding counts to the file named
# XXXXX-assignment07-subreddits.txt


# run and create a function that isolates data between brackets, remove brackets and other non important characters, then split between each subreddit
subreddits = pd.Series(" ".join(submission.apply(lambda x: str(re.findall('{.+}', x)).replace('{', "").replace('}', "").replace('[', "").replace(']', "").replace("'", ""))).split())
subreddits = subreddits.tolist()
columns=['Received','User Known']

df8 = pd.DataFrame(columns=['Subreddits','Count']) # create dataframe
df8['Subreddits'] = subreddits # add subreddit data
df8["Count"] = 1  # create a column of counts to sum up subreddits


top10 = pd.DataFrame(df8.groupby('subreddits').sum()).sort_values('count', ascending = False) #group together by subreddit and sum the count colum
print(top10[0:11]) print the top 10 subreddits


top.to_csv('XXXXX-assignment07-subreddits.txt') # creates csv

'''
#8
                        count
subreddits                   
"AskReddit"              3241
"pics"                   2734
"funny"                  2704
"IAmA"                   2138
"WTF"                    2133
"gaming"                 2079
"Random_Acts_Of_Pizza"   1978
"videos"                 1620
"todayilearned"          1556
"AdviceAnimals"          1452
'''


# In[ ]:



