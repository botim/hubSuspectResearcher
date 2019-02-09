"""
Created on Thu Feb  7 21:03:31 2019

@author: Erez K Ashalim
"""

#Developed by Dani Movso
import features_extractor

#Developed by Yonatan Vernik
import twitter_client

'''
The suspect researcher (SR) api creates the basic formality in order  
to analyze networks of bots using users' metadata.

The Problem was defined as follows: 
for given Twitter user u with metadata m, 
we are looking for a function f in SR (suspect researcher) 
which will return a score from 0 to 1 
(not included) which indicates the probability of u, being
a hub of a bot network.

f(u) to be implemented as a reducer.
'''

def get_client_details_path():
	raise NotImplementedError("Connect configuration file path to SR")

def main():
    print 'Running Suspect Researcher';
	
	#local enviornment
    #working_path = GLOBALS.CURRENT_DEVELOPMENT_ENVIORNMENT
	
	#TODO create configuration file to init the twitter client
	#client_details_path = get_client_details_path()
	
	#TODO init client
	twitter_client.init(client_details_path)
	
    users_parameters = twitter_client.get_user_params(api, id)
	extracted_features = features_extractor(users_parameters)
	
	#TODO create the Data Access Object which will return normalized_features
	normalized_score = dao.store_features(extracted_features)
	
	#define the minimum suspicion score
	minimum_suspicion_score = 0.7
	
	if (normalized_score > minimum_suspicion_score):
		print "User is suspected as a bot/bot hub"
	else:
		print "User is probably a decent human struggling to make a living"
	
	return 'Finished Succesfully';
	
if __name__ == '__main__':
    status = main()
	print status
	