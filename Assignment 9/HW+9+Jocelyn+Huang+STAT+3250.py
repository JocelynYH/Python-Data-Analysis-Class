
# coding: utf-8

# In[26]:



##
## File:           HW+9+Jocelyn+Huang+STAT+3250.py (STAT 3250)
## Topic:          Assignment 9
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3

# Background: This project centers on several related data sets, the centerpiece the set reviews.txt which 
#     consists of 100K movie reviews. There are 1682 different movies reviewed, with a total of 943 different reviewers. 
#     Each review is an integer between 1 (lowest) and 5 (highest). Other data files include information about each 
#     reviewer, about each movie, and relating zip codes to states/territories. The file README_assign09.txt gives 
#     more information about the data sets, including some that is required to answer the questions correctly. 
#     (So read it!)
    
# Please confine your work to the given data sets. (Work with the zip code file given – part of the assignment is 
#     data cleaning.) Use these data sets to answer the following questions.


# 1. Find the 5 reviewers with the most reviews, and then use their reviews to find a 95% confidence interval for 
# their average rating (taken as a group). Then find the average rating for the remainder of the reviewers. Is this 
# average within the top-5 confidence interval? Here the sample sizes are quite large, so we can use the confidence 
# interval formula

import pandas as pd # import pands and numpy
import numpy as np
reviews = pd.read_csv('reviews.txt', # read files and provide columns
                        sep='\t',
                        header=None,
                        names=['Reviewer','Movie','Rating','Date'])
# reviewsb = reviews # store original data under new dataframe

byreviewer = reviews['Reviewer'].groupby(reviews['Reviewer']) # group data by reviewer ID
top5 = byreviewer.count().sort_values(ascending=False).head(5)  # count the number of reviews each reviewer has, sort the ranking, then grab the most prolific Reviewers
print(top5)
'''
Reviewer
405    737
655    685
13     636
450    540
276    518
'''
mean_top5 = np.mean(top5) # find the means of the top reviewers
mean_top5

std_top5 = np.std(top5, ddof=1) # find the standard deviations of the top reviewers
std_top5

upper_bound = mean_top5 + (1.96*(std_top5/np.sqrt(5))) # calculate upper bound
lower_bound = mean_top5 - (1.96*(std_top5/np.sqrt(5))) # calculate lower bound
print(lower_bound, upper_bound)
# 541.297793534 705.102206466

therest = byreviewer.count().sort_values()[0:-5]
np.mean(therest)
# 103.28784648187633

'''
#1
The average of the rest of the reviewers (103.28784648187633) is no where within the confidence infernal of 
the top 5 (541.297793534, 705.102206466)'''


# In[27]:


# 2. Which movies were the top-10 based on of number of times reviewed? (Provide the movie title and the number 
# of times reviewed for each. If there is a tie for 10th place, include all that tied.)
movies = reviews['Movie'].groupby(reviews['Movie']) # group data by Movie ID and store as groupby object
movies.count().sort_values().tail(10) # count by Movie ID, and rank.  Grab the top 10 most reviewed Movies
movie_data = pd.read_csv('genres.txt', # read in movie data
                        sep='\t',
                        header=None,
                         names=['rawData'])

# to test one instance of splitting:
# pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')))[3]

movie_data['Movie ID'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[0])) # split data and assign data to their respective columns
movie_data['movie title'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[1]))
movie_data['release date'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[2]))
movie_data['video release date'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[3]))
movie_data['IMDb URL'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[4]))
movie_data['unknown'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[5])).astype(int)
movie_data['Action'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[6])).astype(int)
movie_data['Adventure'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[7])).astype(int)
movie_data['Animation'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[8])).astype(int)
movie_data['Childrens'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[9])).astype(int)
movie_data['Comedy'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[10])).astype(int)
movie_data['Crime'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[11])).astype(int)
movie_data['Documentary'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[12])).astype(int)
movie_data['Drama'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[13])).astype(int)
movie_data['Fantasy'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[14])).astype(int)
movie_data['FilmNoir'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[15])).astype(int)
movie_data['Horror'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[16])).astype(int)
movie_data['Musical'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[17])).astype(int)
movie_data['Mystery'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[18])).astype(int)
movie_data['Romance'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[19])).astype(int)
movie_data['SciFi'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[20])).astype(int)
movie_data['Thriller'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[21])).astype(int)
movie_data['War'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[22])).astype(int)
movie_data['Western'] = pd.Series(movie_data["rawData"].apply(lambda x: x.split('|')[23])).astype(int)

movie_data = movie_data.drop('rawData', 1) # drop the initial read of messy data

counted_movies = movies.count() # count and store data by movie ID
counted_movies = counted_movies.to_frame(name=None) # convert to dataframe
counted_movies=counted_movies.rename(columns = {'Movie':'Count'}) # name the column with the count for each movie appropriately
counted_movies['Movie ID'] = counted_movies.index # reassign Movie ID to be the index

movie_data['Movie ID'] = movie_data['Movie ID'].astype(int) # convert strings to integers


counted_movies.index.names = ['index'] # relabel the index title to indicate Movie ID
allmovies = pd.merge(counted_movies,movie_data) # merge the two dataframes
allmovies.sort_values(by='Count', ascending=False).head(10)[['movie title', 'Count']]  # rank the combined dataframe by count and grab the most ranked movie titles

'''
#2
	movie title	Count
49	Star Wars (1977)	583
257	Contact (1997)	509
99	Fargo (1996)	508
180	Return of the Jedi (1983)	507
293	Liar Liar (1997)	485
285	English Patient, The (1996)	481
287	Scream (1996)	478
0	Toy Story (1995)	452
299	Air Force One (1997)	431
120	Independence Day (ID4) (1996)	429
'''


# In[28]:


# 3. Which genre occurred most often, based on the number of reviews. Which was least often? 
# (Don’t include “unknown” as a genre.)

genres = pd.DataFrame(allmovies.sum(axis=0))  # sum the dummy values for each genres by summing columns
genres[6:].sort_values(by=[0], ascending=False).iloc[0] # isolate only genre data, sort, and grab highest reviewed
genres[6:].sort_values(by=[0], ascending=False).iloc[-2] # isolate only genre data, sort, and grab lowest reviewed, behind unknown
'''
#3 
The least reviewed genre is fantasy, and the most reviewed genre is drama.'''


# In[29]:


genres


# In[30]:


# 4. What percentage of reviews are for movies classified in at least two genres?

ct = 0 # start counter
genre_rows = allmovies.iloc[:,6:25] # isolate only genre data columns
over2count = genre_rows.sum(axis=1) # sum each movies # of listed genres and store
for i in range(len(over2count)): # start for loop for the length of the number of movies
    if over2count[i] >= 2:     # if the movie has two or more genres
        ct += 1                # increase the counter
print(((ct/(len(over2count)))*100),"%") # print the percentage by dividing the counter of at least 2 genres, over the entire number of all movies
'''
#4
50.4756242568371 %
'''


# In[31]:


# 5. Give a 95% confidence interval for the average rating for male reviewers, and do the same for female reviewers.

reviewers = pd.read_csv('reviewers.txt',  # read in data into 'rawdata'
                        sep='\t',
                        header=None,
                        names=['rawdata'])
reviewers['rawdata']  # check it out
reviewers['Reviewer'] = pd.Series(reviewers['rawdata'].apply(lambda x: x.split('|')[0])).astype(int) # split and store data into their respective columns, converting to intgers if numbers
reviewers['Age'] = pd.Series(reviewers['rawdata'].apply(lambda x: x.split('|')[1])).astype(int)
reviewers['Gender'] = pd.Series(reviewers['rawdata'].apply(lambda x: x.split('|')[2]))
reviewers['Occupation'] = pd.Series(reviewers['rawdata'].apply(lambda x: x.split('|')[3]))
reviewers['Zip Code'] = pd.Series(reviewers['rawdata'].apply(lambda x: x.split('|')[4]))
reviewers = reviewers.drop('rawdata', 1)


withppl = pd.merge(reviews,reviewers)  # merge the two sets of data


ctm = 0  # start counter for male reviewers
for i in range(len(withppl)):  # start for loop
    if withppl['Gender'][i] == 'M':  # if gender is male, add to the counter
        ctm += 1

ctf = 0 # same as above, but for females
for i in range(len(withppl)):
    if withppl['Gender'][i] == 'F':
        ctf += 1
        
ctm+ctf  # double check to make sure we sum to the total number of reviews

meanM = np.mean(withppl.loc[withppl['Gender'] == 'M']['Rating']) # finds mean of rating with gender M
meanF = np.mean(withppl.loc[withppl['Gender'] == 'F']['Rating']) # finds mean of rating with gender F

stdM = np.std((withppl.loc[withppl['Gender'] == 'M']['Rating']),ddof=1) # finds std of rating with gender M
stdF = np.std((withppl.loc[withppl['Gender'] == 'F']['Rating']),ddof=1) # finds std of rating with gender F


upper_boundM = meanM + (1.96*(stdM/np.sqrt(ctm))) # CI for males
lower_boundM = meanM - (1.96*(stdM/np.sqrt(ctm)))

upper_boundF = meanF + (1.96*(stdF/np.sqrt(ctf))) # CI for females
lower_boundF = meanF - (1.96*(stdF/np.sqrt(ctf)))

print("CI for males:", lower_boundM,upper_boundM)
print("CI for females:", lower_boundF,upper_boundF)

'''
#5
CI for males: 3.52130852808 3.53726944122
CI for females: 3.517202288 3.54581247502
'''


# In[32]:


# 6. Which locations (state, territory, or Canada) formed the top-10 for number of reviews? (Provide a table of
# location and number of reviews. The location ’unknown’ should not be included.)


zips = pd.read_csv('zipcodes.txt',    # Read in zip codes, eliminate dups
                  usecols = [1,4],
                  converters={'Zipcode':str}).drop_duplicates()
zips

zipseries = pd.Series(data=zips['State'].values, index=zips['Zipcode'])  # creates series with state and zipcode



def ziptostate(zcode):  # function to assign a Location to each zipcode
      if str.isdigit(zcode)==False:
          return('Canada')
      elif zcode in zipseries.index:
          return(zipseries[zcode])
      else:
          return('Unknown')
    
withppl['Location'] = withppl['Zip Code'].apply(ziptostate) # within big dataframe, stores categorical Location according to zipcode using above function
withppl

print(withppl['Location'].groupby(withppl['Location']).count().sort_values(ascending=False).head(10)) # groups data by Location, ranks, and finds top 10 locations with most reviews
'''
#6
Location
CA    13842
MN     7635
NY     6882
IL     5740
TX     5042
OH     3475
PA     3339
MD     2739
VA     2590
MA     2584
Name: Location, dtype: int64
'''
rankedbylocation = withppl['Location'].groupby(withppl['Location']).count().sort_values(ascending=False) # provides ranking of number of reviews by location
rankedbylocation[~rankedbylocation.index.isin(['Unknown'])]  # removes unknown
'''
#6
Location
CA        13842
MN         7635
NY         6882
IL         5740
TX         5042
OH         3475
PA         3339
MD         2739
VA         2590
MA         2584
MI         2454
CO         2389
GA         2317
WA         2252
MO         2204
Canada     2086
NC         2008
ID         1801
WI         1785
OR         1767
SC         1733
CT         1723
NJ         1702
FL         1679
IA         1587
AZ         1463
DC         1411
TN         1206
IN         1006
KY          962
OK          962
NH          915
UT          901
LA          698
NM          574
NE          528
AK          437
VT          431
RI          429
KS          406
HI          298
NV          266
MS          251
AL          248
ND          231
MT          186
ME          123
WV          116
DE          110
AP          105
WY           48
SD           39
AR           26
AE           21
Name: Location, dtype: int64
'''


# In[33]:


# 7. Find the occupations that gave the highest average reviews, and the lowest average reviews. (Here “other” and 
# “none” are not occupations, but “student” is.)

groupedocc = withppl['Rating'].groupby(withppl['Occupation']) # group data by occupation
print("The occupation that gives the lowest average reviews is", groupedocc.mean().sort_values().index[0],'.')  # rank the data and find/print occupation giving lowest reviews
print("The occupation that gives the highest average reviews is", groupedocc.mean().sort_values().index[-2],'.') # rank the data and find/print occupation giving highest reviews
'''
#7
The occupation that gives the lowest average reviews is healthcare .
The occupation that gives the highest average reviews is lawyer .
'''


# In[37]:


# 8. What percentage of movies have exactly 1 review? 2 reviews? 3 reviews? Continue to 20 reviews.
reviewpermovie = withppl['Movie'].groupby(withppl['Movie']).count() # groupby and count # of times each movie was reviewed 


myindex = list(range(20)) # creates a list of 0-19
myindex = [i+1 for i in range(20)] # increases list to go from 1-20
myindex = pd.Series(myindex) # converts to series

storage = [] # empty list
dfmovie = pd.DataFrame(reviewpermovie) # converts Movie rankings to dataframe
dfmovie['blank']= 0 # creates an empty column for dummy variable if movie has desired number of reviews
dfmovie['count'] = 0 # creates an empty column to hold the count for how many times the above occurs

# To test a single instance of the for loop, gives how many times we find a movie with 452 reviews
# cownt = 0
# for i in range(len(dfmovie)): # goes through all movies 
#     if dfmovie['Movie'].iloc[i] == 452: # goes through by ID, and if the # of reviews matches 452, 
#         dfmovie['blank'][i] = 1  # then assign a 1 into the blank column in the row
#         cownt += 1   # also, increase the counter
# cownt  # check this counter to make sure the loop worked.  it works. 


def counter(parameter): # convert the above for loop into a function
    dfmovie['blank']= 0
    for i in range(len(dfmovie)):
        if dfmovie['Movie'].iloc[i] == parameter:
            dfmovie['blank'][i] = 1
    storage.append(dfmovie['blank'].sum())  # store the number of movies that have the desired number of reviews into our empty list
    return(dfmovie['blank'].sum())  # returnsthe number of movies that have the desired number of reviews
counter(2)

storage = myindex.apply(counter) # for 1-20, applies our function and stores values into a list

propdf = pd.DataFrame(columns=['Cnt','n']) # create empty dataframe
propdf['Cnt']=storage # fill Cnt columm with values from storage (how many movies had a certain # of reviews)
propdf['n']=storage.sum() # filled with the sum of all movies that had 1-20 reviews
propdf['percentage']=propdf['Cnt']*100/propdf['n'] # proportion of how many movies had the certain number of reviews over the total
propdf.index = propdf.index + 1 # increase index to match # of reviews desired
propdf.index.name = '# of Reviews' # rename index to reflect the # of reviews tested for
propdf.iloc[:,[2]] # show only # of reviews and percentage
'''
#8
# of Reviews	percentage
1	18.675497
2	9.006623
3	7.947020
4	8.476821
5	6.754967
6	5.165563
7	5.827815
8	3.973510
9	4.370861
10	4.370861
11	2.649007
12	3.708609
13	3.311258
14	1.854305
15	2.913907
16	2.516556
17	1.324503
18	3.178808
19	2.384106
20	1.589404
'''


# In[ ]:


# 9. Which genre had the highest average review, and which had the lowest average review?

allmovies # review dataframe
withppl= withppl.rename(columns = {'Movie':'Movie ID'}) # rename column name to clarify where the ID is
withppl  # check our work
reviewgenres = pd.merge(allmovies,withppl) # merge the data to include review info

# store all genre names in a list
genreslist = ['unknown' , 'Action' , 'Adventure' , 'Animation' ,
                                'Childrens' , 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
                                'FilmNoir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'SciFi' ,
                                'Thriller' , 'War' , 'Western']
genrelist = [] # create empty list to hold ratings
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Action']).mean()[1]) # get the ratings of action movies, find the mean, and store the avg rating, store into genrelist
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Adventure']).mean()[1]) # repeat for all genres
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Animation']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Childrens']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Comedy']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Crime']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Documentary']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Drama']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Fantasy']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['FilmNoir']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Horror']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Musical']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Mystery']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Romance']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['SciFi']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Romance']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Thriller']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['War']).mean()[1])
genrelist.append(reviewgenres['Rating'].groupby(reviewgenres['Western']).mean()[1])
ndf = pd.DataFrame({ # create new dataframe
      'Rating': genrelist}, # ratings are filled with data from genrelist
      index=genreslist) # index is the list of genres
print(ndf.sort_values(by='Rating').index[0],'had the lowest reviews') # sort the data and find genre with lowest reviews
print(ndf.sort_values(by='Rating').index[-1],'had the highest reviews') # sort the data and find genre with highest reviews
'''
#9
Drama had the lowest reviews
Fantasy had the highest reviews'''


# In[11]:


# 10. Suppose that a “positive review” is one with a rating of 4 or 5.
# (a) Find a 95% confidence interval for pf − pm, where pf is the proportion of positive reviews from females and 
# pm is the proportion of positive reviews from males. Is there evidence that the proportions differ?
Fonly = withppl[withppl['Gender'] == 'F'] # subset data where gender is female
posF = 0  # start counter for positive reviews from females
for i in range(len(Fonly)):  # go through all the female reviews
    if Fonly['Rating'].iloc[i] == 4|5:  # if review is "positive" 
        posF += 1  # add one count
pfn = len(Fonly) # store total n of all female reviews
pf = (posF/pfn) # calculate proportion of positive female reviews over total female reviews

pfs = np.sqrt((pf*(1-pf))/pfn) # calculate sigma for the CI calculation

Monly = withppl[withppl['Gender'] == 'M']  # repeat above process again for males
posM = 0
for i in range(len(Monly)):
    if Monly['Rating'].iloc[i] == 4|5:
        posM += 1
pnm = len(Monly)
pm = posM/(pnm)
pms = np.sqrt((pf*(1-pf))/pnm)           

# equation is:
# pf - pm +- 1.96*sqrt(s1^2/sqrt(n1)+s2^2/sqrt(n2))
up_bound = (pf - pm) + 1.96*np.sqrt(((pfs**2)/np.sqrt(pfn)+((pms**2)/np.sqrt(pnm)))) # calculate upper bound
low_bound = (pf - pm) - 1.96*np.sqrt(((pfs**2)/np.sqrt(pfn))+((pms**2)/np.sqrt(pnm))) # calculate lower bound
print(low_bound, up_bound)
'''
#10
0.0266458014818 0.027539445297
Out[14]:
'''


# In[743]:


# (b) It is thought that Canadians are nicer than Americans. Find a 95% confidence interval for pC −pA, where pC 
# is the proportion of positive reviews from Canadians, and pA is the proportion of positive reviews from Americans. 
# (Exclude those whose location is unknown.) Is there evidence that Canadians give more positive reviews?


# used above method, where we subset by gender, but instead subset where Canada was the location

Conly = withppl[withppl['Location'] == 'Canada']  
posC = 0

for i in range(len(Conly)):
    if Conly['Rating'].iloc[i] == 4|5:
        posC += 1
pCn = len(Conly)
pC = (posC/pCn)

pCs = np.sqrt((pC*(1-pC))/pCn)

withppl['US'] = "" # creates an empty list to hold logic test if the reviewer lives in the US


# From here on out, I knew what to do conceptually, but I hit a snag with trying to store the 1's for American locations.
# Though the syntax wouldn't let me find the actual numbers, I coded and commented what I would've done if I had gotten the values.
posA = 0
for i in range(len(withppl)):
    if len(withppl['Location'][i]) == 2:
        withppl['US'][i] = 1
America = withinppl[withinppl['US']==1] # subset where locations are in the US

posA = 0 # start empty counter to hold positive American reviews

for i in range(len(Conly)):    # start for loop
    if Conly['Rating'].iloc[i] == 4|5:  
        posC += 1                     # tallies and stores the number of positive American reviews
pAn = len(America)  # find total number of reviews where reviewers live in the US
pC = (posC/pCn) # finds proportion for # of positive American reviews over total # of American reviews

pAs = np.sqrt((pC*(1-pC))/pCn) # finds sigma for CI calculation

# equation is:
# pC - pA +- 1.96*sqrt(s1^2/sqrt(n1)+s2^2/sqrt(n2))
up_bound2 = (pC - pA) + 1.96*np.sqrt(((pCs**2)/np.sqrt(pCn)+((pAs**2)/np.sqrt(pAn)))) # calculate upper bound
low_bound2 = (pC - pA) - 1.96*np.sqrt(((pCs**2)/np.sqrt(pCn)+((pAs**2)/np.sqrt(pAn)))) # calculate lower bound
print(low_bound2, up_bound2)

