# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 19:56:48 2022

@author: anous
"""

# with gzip.open("C:/Users/anous/Desktop/Career/users.json.gz", 'r') as zipfile:
#     my_object = json.load(zipfile.read())
#     print(my_object.head())






import json
import gzip
import pandas as pd

'''
USERS TO DATAFRAME
'''
filename = 'C:/Users/anous/Desktop/Career/users.json.gz'  # Sample file.

json_content = []
with gzip.open(filename , 'rb') as gzip_file:
    for line in gzip_file:  # Read one line.
        line = line.rstrip()
        if line:  # Any JSON data on it?
            obj = json.loads(line)
            json_content.append(obj)

df = pd.DataFrame(json_content, columns =['_id', 'active', 'createdDate',
                                          'lastLogin', 'role', 'signUpSource', 'state']) 
print(df.isnull().sum())
print(df)
df.to_csv('users.csv')

'''
Pointers from observing users file through CSV:
    1. In some rows, signupsource is missing. Usually we can fill it with Null
    so that it runs in databases or during calculations. However, if this data
    can be backtracked to the source and if it could be filled with actual source, 
    then it will help with potential future consumer pattern analysis.
    2. Date format is confusing and not sure how it could be extracted for analysis. 
    3. Several missing lastlogindate. 

'''

'''
RECEIPTS TO DATAFRAME
'''

filename = 'C:/Users/anous/Desktop/Career/receipts.json.gz'  # Sample file.

json_content = []
with gzip.open(filename , 'rb') as gzip_file:
    for line in gzip_file:  # Read one line.
        line = line.rstrip()
        if line:  # Any JSON data on it?
            obj = json.loads(line)
            json_content.append(obj)

df = pd.DataFrame(json_content, columns =['_id', 'bonusPointsEarned', 'bonusPointsEarnedReason', 
                                          'createDate', 'dateScanned', 'modifyDate', 'finishedDate',
                                          'pointsEarned', 'purchaseDate' , 'pointsAwardedDate', 
                                          'purchasedItemCount','rewardsReceiptItemList','rewardsReceiptStatus',
                                          'totalSpent' , 'userId']) 
df['barcode'] = df['rewardsReceiptItemList'].astype(str).str.split().str[1]
df.to_csv('receipts.csv')

'''
Pointers from observing receipts file through CSV:
    1. rewardsReceiptItemList has a lot of content which is difficult to analyze
    with so many content inside it. Since the data is not filled for everything,
    extracting in a loop is difficult. it would be better to have different sections for it
    2. Accepted vs. Finished status for rewards
    3. Repetitive IDs which is difficult to work with in database since IDs are
    usually primary IDs and primary IDs can't be duplicated
'''

'''
BRANDS TO DATAFRAME
'''


filename = 'C:/Users/anous/Desktop/Career/brands.json.gz'  # Sample file.

json_content = []
with gzip.open(filename , 'rb') as gzip_file:
    for line in gzip_file:  # Read one line.
        line = line.rstrip()
        if line:  # Any JSON data on it?
            obj = json.loads(line)
            json_content.append(obj)
#print(json_content)
df = pd.DataFrame(json_content, columns =['_id', 'barcode', 'brandCode', 
                                            'category', 'categoryCode', 'cpg', 'name',
                                            'topBrand']) 
df.to_csv('brands.csv')

'''
Pointers from observing brands file through CSV:
    1. Barcode patterns conflicting with receipts barcode.
    2. Brandcode switching from integers and strings (words). Better to 
    streamline as one type (either have number IDs or brands names)
'''

