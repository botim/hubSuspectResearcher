'''
Created on Feb 09, 2019

@author: Dani Movso 
'''

import pandas as pd, numpy as np

# Insert the users file name.
# The Columns of the file should be in the following order: 
#                      "ID", "Handle", "Name", "Description", "Date Created", "Location", "Language", "Protected", "Followers", "Friends", "Favourites", "Statuses", "Listed", "Verified"
fileName = "users_kingdom_salvation.csv"

# Read the users CSV file.
# If the file has a header row, use the following command instead:
# df = pd.read_csv(fileName, sep=',')
df = pd.read_csv(fileName, sep=',', names = ["ID", "Handle", "Name", "Description", "Date Created", "Location", "Language", "Protected", "Followers", "Friends", "Favourites", "Statuses", "Listed", "Verified"])

# Remove all users with "Protected == TRUE"
df = df[df['Protected'].isna()]

# Fill empty values with "0"
df = df.fillna(0)

# Add the feature ratios needed
df['StatusesToFollowers'] = df['Statuses']/df['Followers']
df['FavouritesToStatuses'] = df['Favourites']/df['Statuses']
df['FavouritesToFollowers'] = df['Favourites']/df['Followers']

# Remove the unnecessary columns
# If there isn't a "Verified" column use:
# df = df.drop(["Name", "Description","Location", "Language", "Protected", "Followers", "Friends", "Favourites", "Statuses", "Listed"], axis=1)
df = df.drop(["Name", "Description","Location", "Language", "Protected", "Followers", "Friends", "Favourites", "Statuses", "Listed", "Verified"], axis=1)

# Create the userFeatures.csv file
df.to_csv("userFeatures.csv", sep=',', encoding='utf-8')





