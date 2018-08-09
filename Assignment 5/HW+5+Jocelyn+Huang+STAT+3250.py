
# coding: utf-8

# In[60]:

##
## File:           HW+5+Jocelyn+Huang+STAT+3250.py (STAT 3250)
## Topic:          Assignment 5
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

#### Part 1
##
## The questions in Part 1 refer to the data in the file
## 'fastfood2.csv'.  The file has several columns: "storenum"
## gives the store number, "secs" that gives the number of seconds 
## to fill the order, "dayofweek" gives the day of the week,
## "meal" gives which meal ordered, "drinkonly" is Yes if only
## a drink was ordered, "cost" gives the amount spent in cents.

##  (a) Determine the proportion of meals that were for Lunch.

import pandas as pd  #to import pandas
import numpy as np   # to import numpy

ff2 = pd.read_csv('fastfood2.csv',index_col=0) #reads data from csv
type(ff2) 

# subsets the data who's meal is Lunch
lunch = ff2.loc[ff2['meal'] == 'Lunch']

# print the division of Lunch meals over all meals
print(len(lunch)/len(ff2))

'''
#1A
0.5165224154435226
'''
print(ff2)


# In[61]:

##  (b) Determine the mean time for each day of the week.

timebyday = ff2['secs'].groupby(ff2['dayofweek']) # subset data by the day of the week, and pull their secs
timebyday.mean() # find the mean of the subset


# In[ ]:

##  (c) Find a 95% confidence interval for the proportion of "drink only"
##      orders for each of Breakfast, Lunch, and Dinner.  Does there appear
##      to be any difference among the three meals? 


drink = ff2.loc[ff2['drinkonly']=='Yes'] # subset data where drink only is yes
mealdrinks = drink.groupby(drink['meal']) # group the drink only's by meal
print(mealdrinks.count()) # count up by meal
drink_count = mealdrinks.count() # store values
print(drink_count.sum()) # all sum values for proportion's denominator


bfast_prp = 2769/14242   # the proportions of each meal for how many people ordered a drink
lunch_prp = 4757/14242
dinner_prp = 6716 / 14242
bfast_prp, lunch_prp, dinner_prp

# finds sigma necessary for the CI calculation
sigma_bfast = np.sqrt((bfast_prp*(1-bfast_prp))/14242)
sigma_lunch = np.sqrt((lunch_prp*(1-lunch_prp))/14242)
sigma_dinner = np.sqrt((dinner_prp*(1-dinner_prp))/14242)

# Confidence Intervals for all three meals

CIlower_bfast = bfast_prp -((1.96*sigma_bfast))  # lower bound
CIupper_bfast = bfast_prp +((1.96*sigma_bfast))  # upper bound

CIlower_lunch = lunch_prp -((1.96*sigma_lunch))  # lower bound
CIupper_lunch = lunch_prp +((1.96*sigma_lunch))  # upper bound

CIlower_dinner = dinner_prp -((1.96*sigma_dinner))  # lower bound
CIupper_dinner = dinner_prp +((1.96*sigma_dinner))  # upper bound

# print results
CIlower_bfast, CIupper_bfast, CIlower_lunch, CIupper_lunch, CIlower_dinner, CIupper_dinner
'''
2c
There is a much higher proportion of people ordering drinks with their breakfast. 

CI breakfast:
(0.18792514659813089, 0.2009247340366114)

CI lunch:
(0.32626594586324253, 0.34175820804772505)

CI dinner:
(0.46336443272123323, 0.47976153273305694)
'''


# In[63]:

##  (d) Find the mean cost for each of the meal types.

mealcost = ff2['cost'].groupby(ff2['meal']) # find the cost grouped by meal
mealcost.mean() # find the mean of each group

'''
#1d
meal
Breakfast    292.079191
Dinner       502.017676
Lunch        372.363622
'''


# In[ ]:

##  (e) Find the proportion of meals of each type, for each day of the week.
meals_by_day = ff2.groupby(['meal', 'dayofweek']) # groupby meal and dayofweek
mat_meals_by_day = meals_by_day.count() # counts each group

sum_meals_by_day = mat_meals_by_day['drinkonly'].sum() # sums all (for denominator proportion purposes)
mat_meals_by_day['prop'] = mat_meals_by_day['drinkonly']/sum_meals_by_day # finds proportion of each group by total sum
print(mat_meals_by_day['prop']) # print result

'''
#1e
meal       dayofweek
Breakfast  Fri          0.024380
           Mon          0.024160
           Thur         0.024280
           Tues         0.024131
           Wed          0.023801
Dinner     Fri          0.071993
           Mon          0.073239
           Thur         0.071674
           Tues         0.073239
           Wed          0.072581
Lunch      Fri          0.104419
           Mon          0.103661
           Thur         0.102325
           Tues         0.103991
           Wed          0.102126
'''


# In[77]:

##  (f) Identify all stores with average order fill time 2 standard 
##      deviations below the mean average fill time for the 892 stores. 
##      (These are the high performing stores.) Similarly, identify all 
##      stores with average order fill time 2 standard deviations above 
##      the mean average fill time for the 892 stores. (These are the 
##      low performing stores.). For each, sort the store number from 
##      smallest to largest.
##      Note: Here the standard deviation is of the set of 892 store
##      averages, not of the 100,288 separate order times.
secs_SN =  ff2.groupby(['storenum']).mean() # groups data by storenum and finds their mean
secs_SN_mean = secs_SN.mean() # finds the mean of total subset
secs_SN_mean = secs_SN_mean['secs'] # subsets by seconds

secs_SN_std = secs_SN['secs'].std() # finds standard deviation

highpf = secs_SN_mean - (2*secs_SN_std) # 2 stds below
lowpf = secs_SN_mean + (2*secs_SN_std) # 2 stds above

print(highpf,lowpf) # print results

slowstores = secs_SN.loc[secs_SN['secs'] > lowpf] # find the stores with performances below (seconds above) the cutoff
print(slowstores)  # print results

faststores = secs_SN.loc[secs_SN['secs'] < highpf] # find the stores with performances above (seconds below) the cutoff
print(faststores)  # print results

'''
#1f
Low performing stores:
                secs        cost
storenum                        
30        247.413534  422.751880
47        245.446809  390.648936
59        244.228571  434.761905
128       247.854167  409.854167
149       254.926316  430.210526
154       247.103774  419.160377
155       244.339130  425.356522
231       255.208696  412.565217
233       245.375000  425.159091
281       249.500000  404.500000
318       245.991453  398.914530
387       248.477064  448.743119
392       245.058252  402.533981
402       246.212598  399.519685
422       254.519231  406.144231
452       243.153846  410.264957
474       243.724771  423.715596
528       250.406250  392.117188
614       243.913793  404.198276
621       250.213592  422.300971
657       264.463918  413.515464
718       248.175000  371.150000
723       248.692308  419.051282
725       245.333333  378.699187
726       244.935780  370.027523
887       250.571429  376.580357

High performing stores:
                secs        cost
storenum                        
27        184.487179  391.068376
43        188.419643  429.928571
53        188.631148  425.295082
122       180.400000  431.821053
201       185.615385  406.730769
243       173.637931  391.767241
312       187.411765  378.882353
500       187.403509  407.491228
511       175.470000  400.840000
514       184.151786  399.642857
550       180.363636  388.490909
570       183.800000  427.769231
651       186.946429  413.553571
699       186.082192  404.123288
722       188.973451  417.433628
852       189.460674  365.370787
859       187.463158  435.410526'''


# In[ ]:

##  (g) Some stores claim that using the mean is unfair due to outliers.
##      Repeat part (f) using the median in place of the mean, and determine
##      which stores (if any) are in both "high performing" groups or both
##      "low performing" groups.

secs_SN =  ff2.groupby(['storenum']).median() # groups data by storenum and finds their medians
secs_SN_med = np.median(secs_SN['secs']) # finds the overall median of the secs

secs_SN_std = secs_SN['secs'].std() # finds the standard deviation of subset data

highpf = secs_SN_med - (2*secs_SN_std) # high performing cutoff
lowpf = secs_SN_med + (2*secs_SN_std) # low performing cutoff

slowstores = secs_SN.loc[secs_SN['secs'] > lowpf]  # find the stores with performances below (seconds above) the cutoff
print(slowstores)

faststores = secs_SN.loc[secs_SN['secs'] < highpf]  # find the stores with performances above (seconds below) the cutoff
print(faststores)

'''
#1g
Slow Stores:
          secs   cost
storenum              
14        190.0  435.0
59        200.0  426.0
130       187.0  389.0
149       209.0  430.0
161       193.0  463.5
173       187.5  411.0
200       187.0  370.0
233       201.0  420.5
240       192.0  365.0
242       193.0  406.0
267       188.5  375.0
290       191.0  416.0
304       194.0  410.0
318       188.0  392.0
320       187.5  432.0
357       186.5  388.0
365       191.0  423.0
402       188.0  396.0
438       193.0  402.0
448       191.0  434.5
452       191.0  410.0
478       190.0  403.0
517       188.0  409.0
528       187.0  384.0
531       187.5  434.5
546       191.0  415.0
568       190.5  434.0
611       188.0  387.0
640       189.0  417.0
657       233.0  389.0
702       191.0  445.0
718       191.5  352.0
723       187.0  415.0
725       190.0  381.0
726       196.0  352.0
755       188.0  401.0
796       192.0  383.5
875       200.0  409.0
887       192.0  385.5

Fast Stores: 
           secs   cost
storenum              
27        141.0  385.0
243       136.5  401.5
312       140.5  360.0
722       141.0  406.0
'''


# In[67]:

#### Part 2
##
## The questions in Part 2 refer to the data in the file
## 'fastfood3.csv'.  This file has the columns in 'fastfood2.csv'
## plus a new column 'satisfaction'.  This new column gives the
## customer's satisfaction on a scale of 1-10 (10 being most satisfied)

ff3 = pd.read_csv('fastfood3.csv',index_col=0) #reads data from csv
type(ff3) 

##  (a) What percentage of customers gave the highest possible satisfaction 
#       rating?  What percentage gave the lowest rating?

perfect = ff3.loc[ff3['satisfaction'] == 10] # subsets where satisfaction is highest.
perfect_prop = len(perfect)/len(ff3)  # finds proportion over total data

awful = ff3.loc[ff3['satisfaction'] == 1] # subsets where satisfaction is lowest
awful_prop = len(awful)/len(ff3)  # finds proportion over total again

perfect_prop*100, awful_prop*100  # multiply by 100 to get percentages
'''
#2a
(0.1296266751754946%, 0.004985641352903638%)
'''


# In[68]:

##  (b) Determine the mean satisfaction for each day of the week.
sat_per_day = ff3['satisfaction'].groupby(ff3['dayofweek']) # find satisfaction by day of week
sat_per_day.mean() # find the mean of each group


# In[79]:

##  (c) The company considers a satisfaction rating of 7 or higher 
##      to indicate a "satisfied" customer.  Find a 95% confidence interval
##      for the proportion of satisfied customers for each of Breakfast,
##      Lunch, and Dinner.  

satisfied = ff3.loc[ff3['satisfaction'] > 6] # subset where satisfaction is 7 or higher
satisfied_group = satisfied.groupby('meal') # group subset by meal
print(satisfied_group.count()) # count the groups (satisfied and by meal) and print result

ff3_meals = ff3.groupby(ff3['meal']) # group data by meals
print(ff3_meals.count()) # print and count groups

sat_b_prop = 6695/12110   # finds proportion of satisfied by meal over by meal
sat_l_prop = 15938/36377
sat_d_prop = 18799/51801


# # finds sigma necessary for the CI calculation
sat_b_sig = np.sqrt((sat_b_prop*(1-sat_b_prop))/12110)
sat_l_sig = np.sqrt((sat_l_prop*(1-sat_l_prop))/36377)
sat_d_sig = np.sqrt((sat_d_prop*(1-sat_d_prop))/51801)

# # Confidence Intervals for all three meals

CIlower_b_sat = sat_b_prop -((1.96*sat_b_sig))  # lower bound
CIupper_b_sat = sat_b_prop +((1.96*sat_b_sig))  # upper bound

CIlower_l_sat = sat_l_prop -((1.96*sat_l_sig))  # lower bound
CIupper_l_sat = sat_l_prop +((1.96*sat_l_sig))  # upper bound

CIlower_d_sat = sat_d_prop -((1.96*sat_d_sig))  # lower bound
CIupper_d_sat = sat_d_prop +((1.96*sat_d_sig))  # upper bound
CIlower_b_sat, CIupper_b_sat, CIlower_l_sat, CIupper_l_sat, CIlower_d_sat, CIupper_d_sat

'''
#2c
CI for breakfast
(0.54399335890671141, 0.56170441153094353)
CI for lunch
(0.43303525024777823, 0.44323272127268798)
CI for dinner
(0.35876723189754983, 0.3670488720386676)
'''


# In[70]:

##  (d) The company suspects that the time required to fill an order can
##      influence customer satisfaction.  Find a 95% confidence interval
##      for the proportion of satisfied customers among those whose orders
##      took no more than 180 seconds to fill.  Do the same for those
##      whose orders too at least 360 seconds to fill.

short = ff3.loc[ff3['secs'] <= 180] # subsets data with seconds equal to or below 180 cutoff
long = ff3.loc[ff3['secs'] >= 360]  # subsets data with seconds equal to or above 360 cutoff

short_sat = short.loc[short['satisfaction']>=7] # finds those under or equal to 180 secs that are also satisfied
long_sat = long.loc[long['satisfaction']>=7]   # finds those above or equal to360 secs that are also satisfied

short_prop = len(short_sat)/len(short) # finds proportion of those satisfied and took less than or equal to 180 secs, over those less than 180 secs
long_prop = len(long_sat)/len(long) # same but with over or equal to 360

# finds sigma necessary for calculation
sigma_short = np.sqrt((short_prop*(1-short_prop))/len(short))
sigma_long = np.sqrt((long_prop*(1-long_prop))/len(long))

CIlower_short = short_prop -((1.96*sigma_short))  # lower bound
CIupper_short = short_prop +((1.96*sigma_short))  # upper bound

CIlower_long = long_prop -((1.96*sigma_long))  # lower bound
CIupper_long = long_prop +((1.96*sigma_long))  # upper bound

CIlower_short, CIupper_short, CIlower_long, CIupper_long # print results

'''
#2d
CI for orders that took 180 seconds or under:
(0.53217460518638282, 0.54038739287204096)
CI for orders that took 360 seconds or over:
(0.1024361195473813, 0.11139622888772485)
'''


# In[71]:

##  (e) Company analysts have developed a formula for predicting customer
##      satisfaction ratings.  It is
##
##         predicted satisfaction= 4 + 0.002*cost - 0.005*secs + m,
##
##      where m = 1 if the meal is Breakfast, and 0 otherwise.
##
##      Predict each customer's satisfaction based on this formula, and
##      add this prediction as a new column on the data frame named
##      "predsatis".  Then compute the mean predicted rating.

ff3['predsatis'] = "" # create empty column

ff3['predsatis'] = 4 + 0.002*ff3['cost'] - 0.005*ff3['secs'] # calculate prediction for all
ff3.loc[ff3['meal']== 'Breakfast']['predsatis'] += 1  # add the m if meal is breakfast

np.mean(ff3['predsatis']) # find the mean of all predicted ratings

'''
#2e 
3.7377602803925534
'''


# In[ ]:

##  (f) For all the customers, find the maximum difference between the 
##      predicted satisfaction rating and the actual satisfaction rating.
##      (This should be the absolute value of the difference.)  Do the same
##      for the minimum difference, and then find the average of all the
##      differences.

ff3['difference']= abs(ff3['predsatis'] - ff3['satisfaction']) # finds the difference between all predicted values and all actual
print("The max difference is", np.max(ff3['difference'])) # prints and finds the highest pair difference
print("The min difference is", np.min(ff3['difference'])) # prints and finds the lowest pair difference
print("The avg difference is", np.mean(ff3['difference'])) # prints and finds the mean of all pair differences

'''
#2f
The max difference is 5.77
The min difference is 0.0
The avg difference is 2.3934124022814744
'''

