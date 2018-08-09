
# coding: utf-8

# In[294]:

##
## File:           HW+11+STAT+3250+Jocelyn+Huang.py (STAT 3250)
## Topic:          Assignment 11
## Name:           Jocelyn Huang
## Section time:   3:30 - 4:45
## Grading Group:  3


# Background: The folder Stocks.zip contains nearly 300 files, each including daily data for
# a specific stock, with stock ticker symbol given in the file name. Each observation includes 
# the following:
#      Date = date information recorded
#      Open = opening stock price
#      High = high stock price
#      Low = low stock price
#      Close = closing stock price
#      Volume = number of shares traded
#      Adj Close = closing price adjusted for stock splits (ignored for this assignment)

# The time interval covered varies from stock to stock. There are some missing records, so the
# data is incomplete. Note that some dates are not present because the exchange is closed on 
# weekends and holidays. Those are not missing records. Answer the questions below based on 
# the data available in the files.

# 1. Use the collective data to determine when the market was open from January 2, 2005 to December 31,
# 2014. (Do not use external data for this question.) Report the number of days the market was open
# for each year 2005-2014. (Include the year and the number of days in table form.)

import pandas as pd  # import necessary libraries 
import numpy as np
import glob



filelist = glob.glob('*.csv')  # selects files ending in .csv

df = pd.DataFrame() # create an empty dataframe 

tickers = [] # empty list called tickers
for i in range(len(filelist)):   # for all the files, add each ticker name to a the empty tickers list
    tickers.append(filelist[i].split('.csv')[0])

tickers  # have a look at our tickers

x=0  # make an empty counter
startingdates = []
endingdates = []
for f in filelist:  # for each file, import the data and apply tickers to each row.  add the data to a larger dataframe.
    newdf = pd.read_csv(f)
    newdf['ticker'] = tickers[x]
    startingdates.append(newdf.sort_values(by='Date',ascending=True)['Date'].iloc[0]) # also add to a list, the date of the first record for the stock
    endingdates.append(newdf.sort_values(by='Date',ascending=True)['Date'].iloc[-1]) # also add to a different list, the date of the last record for the stock
    x += 1    # also increase the index to move down the tickers list
    df = pd.concat([df,newdf])

df

originaldf=df # saves original data without converting to datetime
df['Date'] = pd.to_datetime(df['Date']) # convert to datetime 
eachday = pd.Series(df['Date'].unique()) # cluster by individual date
opendays = eachday[(eachday.dt.year <= 2014) & (eachday.dt.year >= 2005)] # subset within the desired yearly range
print(opendays.groupby(opendays.dt.year).count()) # group dates by year and count, and print results
'''
#1
2005    252
2006    251
2007    251
2008    253
2009    252
2010    252
2011    252
2012    250
2013    252
2014    252
dtype: int64
'''

# 2. Determine the total number of missing records for all stocks for the period 2005-2014.

OD_df = opendays.to_frame() # create and store a dataframe from all the data of days market was open
OD_df  # check our work
OD_df = OD_df.rename(columns={0: 'dates'}) # appropriately name the date column
possibledates = pd.DataFrame([]) # initialize empty dataframe, using all the open days, to hold all the possible combinations of date and tickers.

x=0 # start counter

for i in range(len(tickers)): # initialize for loop
    OD_df['ticker'] = tickers[x]  # add a ticker to each open day
    possibledates = possibledates.append(OD_df[(OD_df['dates']>=startingdates[x]) & (OD_df['dates']<=endingdates[x])]) # append the each possible combination of date and ticker to the empty dataframe, but also, mask by the dates within the range of each stock
    x += 1 # increase counter by one to loop through tickers
    

possibledates = possibledates.rename(columns={0: 'dates'}) # appropriately name the date column
possibledates['dateticker']=possibledates['dates'].astype(str)+' '+possibledates['ticker'] # create a combined date and ticker column for merge purposes
possibledates['dateticker']  # list of the possible date + ticker combinations that could've been recorded
possibledates # holds all possible records considering all open days and tickers


originaldf['dateticker']=originaldf['Date'].astype(str)+' '+originaldf['ticker'] # do the same for data of all recorded dates
originaldf['dateticker']  # holds all the actual taken records

missingrecords = np.setdiff1d(possibledates['dateticker'],originaldf['dateticker']) # Elements in possible records which didn't have actual records taken
len(missingrecords)  # print length of missing reccords
'''
#2
9459
'''

# 3. For the period 2005-2014, and the 10 stocks (plus ties) that had the most missing records, and the 10
# stocks (plus ties) with the fewest missing records. (For the latter, don't include stocks that have no
# records for 2005-2014.) Report the stocks and the number of missing records for each.

#compile possible records by ticker and sort
possiblerecords = possibledates.groupby(possibledates['ticker']).count().sort_values(by='dates')
possiblerecords = possiblerecords.rename(columns={'dates': '# of possible records'}) #appropriately name the column.
possiblerecords = possiblerecords.drop('dateticker', 1) # drop uneccesary data
possiblerecords # check it out

merged = pd.merge(possibledates, originaldf, on='dateticker',how='outer') # merge and store the possible data dates with the taken data


missingno = pd.DataFrame(missingrecords)  # add missing record data to a dataframe
missingno = missingno.rename(columns={0: 'dateticker'})  # appropriately label the dates column with the right label
missingno['date']=pd.Series(missingno['dateticker'].apply(lambda x: x.split(' ')[0])) # create a column with only the date
missingno['ticker']=pd.Series(missingno['dateticker'].apply(lambda x: x.split(' ')[1])) # split the data to put only the ticker in its own column

dfmissingr = missingno.groupby(missingno['ticker']).count().sort_values(by='date') # group missing records by ticker, count, and sort, store as new df
dfmissingr = dfmissingr.rename(columns={'dateticker': 'count'}) # rename the counts as such
dfmissingr = dfmissingr.drop('date', 1) # drop redundant count columns


tickersdata = pd.DataFrame(tickers)  # create dataframe with just tickers, as to add in stocks without missing records
tickersdata = tickersdata.rename(columns={0: 'ticker'}) # name tickers column as such
tickersdata['zero'] = 0 # give each stock a missing record count of 0, with intention of summing with actual missing record counts, just to give stocks w/out missing records a count
tickersdata=tickersdata.set_index('ticker') # make the index the ticker names

result = pd.concat([dfmissingr, tickersdata], axis=1) # combine the data with only missing records, with the all the stocks with no missing records.  we now have a column with NAs and one with actual missing record data
dfmissingr.sort_index() # sort data
result['# of missing records']=result['count']+result['zero'] # sum the missing records with zero.  each stock should have a count or NAn
totalmissingr = result.fillna(value=0).sort_values(by='count') # replace NAn with zero.  each stock should have a count of zero or above now.
totalmissingr = totalmissingr.drop('count', 1) # drop columns used to calculate
totalmissingr = totalmissingr.drop('zero', 1) # drop columns used to calculate
print(totalmissingr.head(10)) # print least missing
print(totalmissingr.tail(14)) # print most missing
'''
#3
      # of missing records
ZTS                    0.0
XYL                    0.0
TRIP                   0.0
NWSA                   0.0
NLSN                   0.0
NAVI                   0.0
LYB                    0.0
GM                     0.0
ADT                    0.0
FB                     0.0
      # of missing records
LB                    42.0
GAS                   42.0
BBT                   42.0
QCOM                  42.0
HOT                   42.0
LVLT                  42.0
SWN                   42.0
PPG                   43.0
RF                    43.0
GE                    43.0
STJ                   44.0
FLR                   44.0
SO                    44.0
PDCO                  45.0
'''


# In[ ]:

# 4. Repeat the previous question, this time for the stocks with the greatest and least proportion of missing
# records during 2005-2014. Report the stocks and the number of missing records for each.


# compile missing records by ticker and store
missingr = missingno.groupby(missingno['ticker']).count().sort_values(by='dates')
missingr = missingr.rename(columns={'dates': '# of missing records'}) # rename the # of missing records appropriately as such

#compile possible records by ticker, count, and sort
possiblerecords = possibledates.groupby(possibledates['ticker']).count().sort_values(by='dates')
possiblerecords = possiblerecords.rename(columns={'dates': '# of possible records'}) # rename the # of missing records appropriately as such
possiblerecords = possiblerecords.drop('dateticker', 1) # drop old data

possiblerecords # check it out

nofour = pd.merge(possiblerecords,totalmissingr, left_index=True, right_index=True) # merge the data by the ticker/index
# create a new column for the proportion, calculate the proportion of missing records to possible records and store in column
nofour['prop']=nofour['# of missing records']/nofour['# of possible records'] # calculate the proportions
nofour = nofour.sort_values(by='prop') # sort the values of the proportions
print(nofour.head(10)) # lowest proportion of missing records
print(nofour.tail(15)) # highest proportion of missing records
'''
#4
Stocks with the lowest proportion of missing records:
ticker                                                       
      # of possible records  # of missing records  prop
NAVI                    179                   0.0   0.0
GM                      909                   0.0   0.0
XYL                     809                   0.0   0.0
TRIP                    771                   0.0   0.0
NLSN                    737                   0.0   0.0
LYB                     927                   0.0   0.0
ADT                     566                   0.0   0.0
ZTS                     483                   0.0   0.0
NWSA                    239                   0.0   0.0
FB                      659                   0.0   0.0

Stocks with the highest proportion fo missing records:
      # of possible records  # of missing records      prop
LB                     2517                  42.0  0.016687
BBT                    2517                  42.0  0.016687
SWN                    2517                  42.0  0.016687
GAS                    2517                  42.0  0.016687
HOT                    2517                  42.0  0.016687
LVLT                   2517                  42.0  0.016687
GGP                    2432                  41.0  0.016859
GE                     2517                  43.0  0.017084
RF                     2517                  43.0  0.017084
PPG                    2517                  43.0  0.017084
STJ                    2517                  44.0  0.017481
FLR                    2517                  44.0  0.017481
QCOM                   2367                  42.0  0.017744
PDCO                   2517                  45.0  0.017878
SO                     2412                  44.0  0.018242
'''


# In[303]:

# 5. Identify the top-10 dates (plus ties) in 2005-2014 that were missing from the most stocks.
missingno = missingno.rename(columns={'dates': 'dateticker'}) # rename column appropriately to reflect the date with the ticker
missingno['date']=pd.Series(missingno['dateticker'].apply(lambda x: x.split(' ')[0])) # split the data to only get and store the date
print(missingno.groupby(missingno['date']).count().sort_values('ticker', ascending=False).head(10)) # group and count data by the date, then sort and grab top
'''
#5
            dateticker  ticker
date                          
2007-06-25          11      11
2012-04-23          11      11
2005-12-15          11      11
2013-01-30          10      10
2013-09-23          10      10
2011-03-08          10      10
2005-05-05          10      10
2005-07-14          10      10
2006-12-04          10      10
2005-02-28          10      10
'''


# In[ ]:

# 6 ) For each stock, impute (
ll in) the missing records using linear interpolation.
# 6 a) Find the Open, High, Low, and Close for the imputed Python Index for each day the market was
# open in October 2010. Give a table the includes the Date, Open, High, Low, and Close, with one
# date per row.
merged = pd.merge(possibledates, originaldf, on='dateticker',how='outer')  # merge our known data with missing records
merged[merged['dateticker'] == '2005-01-03 HPQ'] # check to make sure the missing records are showing up
merged.sort_values(by='Date') # so now we have all possible dates, with empty slots for missing records, sorted by date

inter_data = merged.apply(pd.Series.interpolate) # lienarly interpolate all data and store
inter_data.sort_values(by='Open') # sort the data by open to ensure there are no more NaNs.  we have succeeded

oct2010 = inter_data[(inter_data['Date'].dt.year==2010)&(inter_data['Date'].dt.month==10)] # subset data at october 2010
oct2010.loc[:,'Date':'Close'].groupby(oct2010['Date']).mean() # group all records by the date, and average the data for the indexes
'''
#6a
	Open	High	Low	Close
Date				
2010-10-01	47.183709	47.499999	46.515018	46.981636
2010-10-04	46.989388	47.425611	46.409676	46.835467
2010-10-05	47.169303	47.971465	46.859743	47.699230
2010-10-06	47.788974	48.186630	47.169230	47.625457
2010-10-07	47.824139	48.056812	47.095018	47.542893
2010-10-08	47.596231	48.142753	47.201956	47.859565
2010-10-11	47.644175	48.051428	47.266520	47.613516
2010-10-12	47.759230	48.346190	47.280329	48.120366
2010-10-13	47.996678	48.568357	47.642335	48.129160
2010-10-14	48.161904	48.534175	47.623626	48.045274
2010-10-15	48.473935	48.738881	47.757508	48.288592
2010-10-18	48.614488	49.135109	48.231459	48.835802
2010-10-19	48.014799	48.545927	47.387163	47.838799
2010-10-20	47.983695	48.808659	47.688768	48.379384
2010-10-21	48.476726	49.041510	47.808417	48.391978
2010-10-22	48.418260	48.906268	48.009746	48.553804
2010-10-25	48.752981	49.211963	48.344581	48.595381
2010-10-26	48.515470	49.145905	48.149601	48.791014
2010-10-27	48.379025	48.907183	47.845198	48.594873
2010-10-28	48.797189	49.125036	47.991970	48.517627
2010-10-29	48.627308	49.246836	48.306763	48.884036
'''


# In[ ]:

# 6b) Determine the mean Open, High, Low, and Close imputed Python index for each month in 2008-
# 2012, and report that in a table that includes the month and year together with the corresponding
# Open, High, Low, and Close.
subset0812 = inter_data[(inter_data['Date'].dt.year>=2008)&(inter_data['Date'].dt.year<=2012)] # subset data between years 2008 and 2012
subset0812['month']=subset0812['Date'].dt.strftime("%B") # create a column for entry's each month
subset0812['year']=subset0812['Date'].dt.year # create a column for each entry's year
answer6b = subset0812.groupby([subset0812['year'],subset0812['month']]).mean() # group the data by the year and month, then average it

print(answer6b) 
'''
#6b
                     Open       High        Low      Close  year
year month                                                      
2008 April      51.640228  52.403922  50.945630  51.725537  2008
     August     48.098275  48.882723  47.322931  48.165635  2008
     December   30.981463  31.920355  30.108581  31.081610  2008
     February   50.272420  51.048850  49.430426  50.246411  2008
     January    50.279512  51.393324  49.179037  50.298608  2008
     July       47.585185  48.567172  46.502628  47.543447  2008
     June       51.363681  52.069156  50.511769  51.180004  2008
     March      49.080260  49.957831  48.166801  49.076179  2008
     May        53.301140  54.013001  52.566951  53.331671  2008
     November   31.315743  32.383279  30.046909  31.181540  2008
     October    35.641150  37.147038  33.818383  35.385159  2008
     September  46.140310  47.290055  44.724880  45.957682  2008
2009 April      31.347888  32.177743  30.754320  31.585001  2009
     August     38.512748  39.034628  37.995506  38.575497  2009
     December   43.297032  43.716087  42.873368  43.287988  2009
     February   29.249619  29.950511  28.495666  29.188955  2009
     January    31.234588  31.949379  30.380906  31.181079  2009
     July       35.149212  35.720311  34.641283  35.279366  2009
     June       35.133990  35.660350  34.530486  35.114363  2009
     March      27.654333  28.424036  26.950749  27.744994  2009
     May        33.685057  34.385651  32.984938  33.728064  2009
     November   42.048139  42.580570  41.596935  42.161562  2009
     October    41.514723  42.072514  40.912662  41.450374  2009
     September  40.295434  40.837742  39.769576  40.344315  2009
2010 April      47.804243  48.356849  47.279819  47.874026  2010
     August     44.246688  44.753835  43.765462  44.296390  2010
     December   51.711626  52.166650  51.297028  51.766025  2010
     February   42.695303  43.203673  42.200830  42.804060  2010
     January    44.031372  44.504720  43.410329  43.925347  2010
     July       43.563721  44.141218  42.947984  43.637365  2010
     June       44.317248  44.883014  43.657056  44.188142  2010
     March      45.628555  46.082256  45.250786  45.709041  2010
     May        45.738701  46.460366  44.813632  45.655941  2010
     November   49.358278  49.882375  48.879930  49.443469  2010
     October    48.056046  48.552765  47.551996  48.101544  2010
     September  45.856727  46.372941  45.426274  45.954266  2010
2011 April      55.100053  55.594095  54.564920  55.122453  2011
     August     49.291852  50.177957  48.196480  49.181974  2011
     December   50.250116  50.750146  49.625060  50.128873  2011
     February   54.190026  54.804639  53.691072  54.324831  2011
     January    53.065118  53.581905  52.497199  53.063342  2011
     July       55.732773  56.304547  55.173108  55.721020  2011
     June       53.971690  54.531249  53.445774  53.952277  2011
     March      53.427655  54.001616  52.836841  53.436288  2011
     May        56.015628  56.548972  55.440558  56.009784  2011
     November   50.331379  50.947453  49.638084  50.298013  2011
     October    49.189210  50.050573  48.443982  49.378636  2011
     September  48.905190  49.656284  48.051786  48.817746  2011
2012 April      56.266089  56.815349  55.735189  56.299536  2012
     August     54.716102  55.193727  54.270498  54.753964  2012
     December   56.578488  57.101834  56.099892  56.634827  2012
     February   54.904598  55.450985  54.411957  54.996522  2012
     January    52.036402  52.623336  51.507692  52.156083  2012
     July       53.671972  54.257423  53.085923  53.726576  2012
     June       53.066392  53.650040  52.455763  53.096744  2012
     March      56.346826  56.844947  55.864258  56.424728  2012
     May        54.609653  55.183426  53.964887  54.529016  2012
     November   55.324477  55.902471  54.790672  55.360890  2012
     October    56.348170  56.844565  55.756877  56.267065  2012
     September  56.495799  57.028566  56.021981  56.547290  2012
'''

