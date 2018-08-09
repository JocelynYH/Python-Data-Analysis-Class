
Here are brief descriptions of the movie review data.

reviews.txt     

The full data set, 100000 ratings by 943 reviewers on 1682 movies.
Each user has rated at least 20 movies.  Reviewers and movies are
numbered consecutively from 1.  The data is randomly ordered. This 
is a list of the form
	          
	reviewer id | movie id | rating | timestamp. 
              
The time stamps are unix seconds since 1/1/1970 UTC.
   

genres.txt
           
Information about the movies; this is a list of the form
              
	movie id | movie title | release date | video release date |
	IMDb URL | unknown | Action | Adventure | Animation |
	Childrens | Comedy | Crime | Documentary | Drama | Fantasy |
	FilmNoir | Horror | Musical | Mystery | Romance | SciFi |
	Thriller | War | Western
              
The last 18 fields are the genres, a 1 indicates the movie
is of that genre, a 0 indicates it is not; movies can be in
several genres at once.  (If the genre is unknown, then a 1
is in the ‘unknown’ column.)  The movie ids are the same as 
in the reviews.txt data set.


zipcodes.txt

A comma-delimited text file listing information about every US zip
code.  The only columns that are needed for Assignment 9 are
‘Zipcode’ and ‘State’.  There is considerable repetition because 
of how the data set is constructed.


reviewers.txt
           
Demographic information about the users; this is a list of the form

	user id | age | gender | occupation | zip code
              
The reviewer IDs are those used in the movie reviews.txt data set.
Zip codes that include letters are from Canada.  Zip codes that are
not contained in the ‘zipcodes.txt’ data set should have state classified
as ‘Unknown’. 
              

