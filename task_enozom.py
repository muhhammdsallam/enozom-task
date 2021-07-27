import pandas as pd
import hashlib
data = pd.read_csv('annual-enterprise-survey-2020-financial-year-provisional-csv.csv') #read data using pandas library
col = data['Industry_code_NZSIOC']              #get data of the third column
oddrows =  col.iloc[::2]                        #get the odd rows only  
resultOfConcatenation = oddrows.tolist()        #put the data in a list using pandas method .tolist()
string = ''.join(resultOfConcatenation)         #concatenate the data using join method to create the string
Finalresult = hashlib.md5(string.encode())      #hashing using md5 algorithm
print(Finalresult.hexdigest().upper())          #printing result




