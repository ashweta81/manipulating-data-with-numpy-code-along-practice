# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data=np.loadtxt(path,delimiter=",",dtype=str)
# Number of unique matches 
matchcodes=data[:,0]
print('The number of unique matches are', np.unique(matchcodes).size)
 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.

# Number of unique teams
team1=data[:,3]
team2=data[:,4]
total_teams=np.concatenate((team1,team2))
print("The total number of unqiue teams are", np.unique(total_teams).size)
 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras


 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out
deliverydata=data[:,[11,20,21]]
for i in deliverydata:
    if (i[1]!=''):
        print(i)
    else:
        None
 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.

# Number of times Mumbai Indians won the toss
mumindian=data[data[:,5]=="Mumbai Indians"]
toss=np.unique(mumindian[:,0]).size
print("The total number of matches in which the MI won the toss are", toss)
 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex
sixruns=data[data[:,16]=="6"]
sixruns[:,13]
from collections import Counter
Counter(sixruns[:,13])
Counter(sixruns[:,13]).most_common(1)
 # An exercise to know who is the most aggresive player or maybe the scoring player 







