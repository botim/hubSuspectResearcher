# hubSuspectResearcher
A R&amp;D API for searching and analyzing possible hubs of bots network

#Developed by Dani Movso
import features_extractor

#Developed by Yonatan Vernik
import twitter_client


The **suspect researcher (SR)** api creates the basic formality in order  
to analyze networks of bots using users' metadata.

The Problem was defined as follows: 
for given Twitter user u with metadata m, 
we are looking for a function f in SR (suspect researcher) 
which will return a score from 0 to 1 
(not included) which indicates the probability of u, being
a hub of a bot network.

f(u) to be implemented as a reducer.
