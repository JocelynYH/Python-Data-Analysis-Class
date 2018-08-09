
# coding: utf-8

# In[4]:

##
## File: HW+#4+STAT+3250+Jocelyn+Huang.py (STAT 3250)
## Topic: Assignment 4
##

#### Part 1
##
## The questions in Part 1 refer to the data in the file
## 'fastfood1.csv'.  The file has two columns, "storenum"
## that gives the store number, and "secs" that gives the 
## number of seconds required to fill the order.

##  (a) Determine the average amount of time required to fill
##      all orders in the data set.

import pandas as pd  #to import pandas
import numpy as np   # to import numpy

ff = pd.read_csv('fastfood1.csv',index_col=0) #reads data from csv
type(ff) 

np.mean(ff['secs']) # finds mean of the secs column
'''
#1A
216.32710792916401
'''


# In[261]:

##  (b) Find the maximum and minimum amount of time required to
##      fill an order.  Then determine the number of orders with
##      the maximum time, and the number of orders with the minimum time.

themin = np.min(ff['secs'])  # finds the min from the secs column
themax = np.max(ff['secs'])  # finds the max from the secs column
print(themin)
print(themax)

nummin=0  # begin the counting.  nummin holds the count

for i in ff['secs']:  # for every secs value
    if i == themin:   # if the value equals the minimum
        nummin += 1   # add one count
print(nummin)         # determines the final number of values that are equivalent to the min


nummax=0             # begin the counting.  nummax holds the count
for i in ff['secs']: # for every secs value
    if i == themax:  # if the value equals the max
        nummax += 1  # add one count
print(nummax)        # determines the final number of values that are equivalent to the max

'''
#1B
30
600
123
23
'''


# In[268]:

##  (c) Determine the average amount of time required by store 777 to fill
##      its orders.

avg = np.mean(ff.loc[777]['secs'])  # finds the mean of the secs with storenum 777
print(avg)                          # prints result

'''
#1C
198.51908396946564
'''


# In[272]:

##  (d) Determine the number of records from store 321 in the data set. 
ff.loc[321]  # finds all records with storenum 321
'''
#1d
	secs
storenum	
321	46
321	208
321	170
321	114
321	128
321	283
321	134
321	158
321	121
321	140
321	113
321	432
321	97
321	261
321	292
321	340
321	266
321	364
321	91
321	126
321	43
321	175
321	113
321	112
321	152
321	43
321	147
321	570
321	127
321	134
...	...
321	130
321	99
321	549
321	103
321	589
321	161
321	342
321	241
321	213
321	151
321	117
321	277
321	294
321	167
321	72
321	164
321	379
321	148
321	75
321	97
321	140
321	141
321	88
321	108
321	250
321	123
321	162
321	100
321	111
321	135
97 rows × 1 columns'''


# In[241]:

##  (e) Find the mean number of seconds 
##      needed to fill an order by stores 700-750.
sortme = ff.sort_index()      # sorts the dataframe ff
subset = sortme.loc[700:750]  # subsets dataframe with storenums between 700 and 750
np.mean(subset['secs'])       # finds the mean of the subset

'''
#1e
215.89245446660885
'''


# In[273]:

##  (f) Find a 95% confidence interval for the proportion of orders for 
##      stores 500-600 that required more than 200 seconds to fill.

CIrange_raw = ff.sort_index() # sorts ff
CIrange = CIrange_raw.loc[(500 <= CIrange_raw.index) & (CIrange_raw.index <= 600)] # subsets the entires with storenum between 500 and 600
CIrange_slow = CIrange[CIrange['secs'] > 200]  # finds the stores between 500-600 that also took >200 secs to fill

CIavg = len(CIrange_slow)/len(CIrange) # the proportion of slow stores over it's sample space


sigma = np.sqrt((CIavg*(1-CIavg))/len(CIrange)) # finds sigma necessary for the CI calculation
CIlower = CIavg -((1.96*sigma))  # lower bound
CIupper = CIavg +((1.96*sigma))  # upper bound

print("The lower bound confidence interval is " + str(CIlower))
print("The upper bound confidence interval is " + str(CIupper))

'''
#1f
The lower bound confidence interval is 0.368388686223
The upper bound confidence interval is 0.386205528145
'''


# In[234]:

##  (g) Determine the number of distinct stores in the data set.
len(ff.index.unique())  # gives the number of unique values of storenum
'''
#1g
892
'''


# In[257]:

##  (h) Determine which store has the lowest mean order time, and which
##      store has the highest mean order time.

unique_SN = ff.groupby(['storenum']).mean()  # finds the mean within their storenum

print(unique_SN.max())  # finds the Max 
print(unique_SN.min())  # finds the min

'''
#2h
264.463918
173.637931
'''


# In[248]:

##  (i) Determine the median number of orders for a single store.
unique_med_SN = ff.groupby(['storenum']).median()  # finds the median within their storenum
unique_med_SN

'''
#1i
	secs
storenum	
1	144.0
2	177.0
3	163.0
4	162.0
5	152.0
6	150.0
7	149.0
8	157.0
9	168.0
10	170.0
11	157.0
12	151.0
13	156.0
14	190.0
15	174.0
16	172.0
17	171.0
18	170.5
19	165.5
20	154.0
21	177.0
22	156.0
23	157.5
24	157.5
25	165.5
26	150.0
27	141.0
28	178.0
29	177.5
30	181.0
...	...
863	162.0
864	166.5
865	170.5
866	167.0
867	161.0
868	164.0
869	156.0
870	167.5
871	162.5
872	174.0
873	160.0
874	154.0
875	200.0
876	170.5
877	164.0
878	164.0
879	157.0
880	146.0
881	154.0
882	150.5
883	164.0
884	176.0
885	167.0
886	162.0
887	192.0
888	156.5
889	166.5
890	152.0
891	165.0
892	154.0
892 rows × 1 columns
'''
#%%


# In[250]:

#### Part 2
##
## The questions in Part 2 refer to the data in the file
## 'samplegrades.csv'.

samplegrades = pd.read_csv('samplegrades.csv',index_col=0)

##  (a) Compute the mean and sample standard deviation for 
##      both the Course Average and the SAT Writing score.

mean_CA = np.mean(samplegrades['CourseAve']) #finds the mean of course average
std_CA = np.std(samplegrades['CourseAve'])  # finds the st.dev. of course average
mean_SG = np.mean(samplegrades['Write'])    # finds the mean of write
std_SG = np.std(samplegrades['Write'])      # finds the st.dev. of course average
mean_CA, mean_SG, std_CA, std_SG 

'''
#2a
(80.40115017667841, 666.7234042553191, 10.657040532534158, 94.35507904507598)
'''


# In[147]:

##  (b) Find the mean Final exam score for all females
##      in the class.

np.mean(samplegrades.loc[samplegrades['Gender'] == 'F']['Final']) # finds mean of Final with values with gender F

'''
#2b
71.35179153094462
'''


# In[278]:

##  (c) Repeat (b), this time for all males in the TR930
##      section.

 # finds mean of Final with values with gender M
np.mean(samplegrades.loc[(samplegrades['Gender'] == 'M') & (samplegrades['Sect'] == 'TR930')]['Final'])

'''
#2c
68.1534090909091
'''


# In[163]:

##  (d) Compute the mean Homework score for all 1st-years
##      and then for all 4th-years.

first_mean = np.mean(samplegrades.loc[(samplegrades['Year']==1)]['HW'])  # finds mean of HW with values with Year 1
fourth_mean = np.mean(samplegrades.loc[(samplegrades['Year']==4)]['HW']) # finds mean of HW with values with Year 4
first_mean, fourth_mean

'''
#2d
First year mean: 189.24376811594195
First year mean: 192.95172413793105
'''


# In[173]:

##  (e) Find the probability that a randomly selected 2nd-year
##      was in the MW200 section.

second_MW = samplegrades.loc[(samplegrades['Year']==2) & (samplegrades['Sect']=='MW200')]  # a second year and in MW200 section
second = samplegrades.loc[samplegrades['Year']==2]  # all second years
prob = len(second_MW)/len(second) # number of second yrs in section over number of second yrs
prob
'''
#2e
0.32142857142857145
'''


# In[185]:

##  (f) Sort the DataFrame on the CourseAve
##      variable, then determine the mean course average
##      for the students with the top-20 averages.

sorted_CA = samplegrades.sort_values('CourseAve')  #sorts dataframe samplegrades by CourseAve
np.mean(sorted_CA.iloc[-20:]['CourseAve'])  # finds the mean of the last 20 values of the sorted dataframe

'''
#2f
95.21865

'''


# In[201]:

##  (g) Determine the bottom-10 final exam scores for 
##      students in the MW200 section.

sorted_CA = samplegrades.sort_values('Final')  # sorts by Final exam scores
sorted_MW = sorted_CA.loc[sorted_CA['Sect']=='MW200']  # subsets sorted values by those in the MW200 section
sorted_MW[:10]['Final']  # looks at the first 10 values

'''
#2g
StudID
CRAMQ     0.0
ISCWI    27.5
HBTSX    35.0
BEYTQ    40.0
HYXDY    45.0
ZMERR    45.0
CBDIH    45.0
WQHKF    45.0
EFTKY    50.0
TVKOR    50.0
'''


# In[228]:

##  (h) Among the students in the top-20% for APDE,
##      determine the percentage that finished in the
##      top-20% for course average.
##      (The top-20% is the top 113 students.  Be careful of ties!)
   
sorted_APDE = samplegrades.sort_values('APDE', ascending=False)  # sorts APDE scores from highest to lowest
sorted_APDE = sorted_APDE.loc[sorted_APDE['APDE'] >= 6]  # counts top 20% of scores as a 6 or higher
sorted_APDE

descending_CA = sorted_CA.sort_values('CourseAve', ascending = False)   # sorts course averages from highest to lowest
descending_CA = descending_CA[:113]  # subsets first 113 highest scores

# divides the intersection of the top 20% APDE and course averages, over all the students
len(np.intersect1d(sorted_APDE.index, descending_CA.index))/len(sorted_APDE)*100

# top_APDE_CA = samplegrades.loc[samples]

'''
#2h
16.9811320754717
'''


# In[ ]:



