# # ### To print unique ec_codes using pandas
# # !/usr/bin/env python
#import csv
#import pandas as pd
#f = pd.read_csv('ec_terms_in_sfam.csv') 
#print(f['EC_CODE'].unique()) 


###### This code how to make a bar chart using csv file
# # !/usr/bin/env python
import csv
import numpy as numpy
from collections import Counter
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('ec_terms_in_sfam.csv') 
ec_ids = data['EC_CODE']
uniprot_ids = data['UNIPROT_ACC']

ec_counter = Counter()

for ec in ec_ids:
    ec_counter.update(ec.split(','))

ec_code = []
repeat = []

ec_code.reverse()
repeat.reverse()

for item in ec_counter.most_common(20):
    ec_code.append(item[0])
    repeat.append(item[1])

plt.barh(ec_code, repeat)
plt.title("The most repeated EC (Top 20s)")
plt.ylabel('ec code')
plt.xlabel('No. of repeats')
plt.tight_layout()
plt.show()




# ### count number of repeats for each ec_code   
# # !/usr/bin/env python
# import csv
# from collections import Counter
# import operator
# with open('ec_terms_in_sfam.csv') as f:
#     ec_code = Counter(row[1] for row in csv.reader(f))
#     print(ec_code)
#     print(len(ec_code))






# ####Unique funfam_numbers/member id ###worked
# !/usr/bin/env python
# import csv
# import pandas as pd
# f = pd.read_csv('funfam_members_in_sfam.csv') 
# # print(f['FUNFAM_NUMBER'].unique()) 
# print(len(f['FUNFAM_NUMBER'].unique()))
# print(f['MEMBER_ID'].unique()) 
# print(len(f['MEMBER_ID'].unique()))



# #! /usr/bin/env python
# import pandas as pd
# import csv
# from collections import Counter
# import operator
# with open('funfam_members_in_sfam.csv') as f:
#     for line in f:
#         line = line.replace('"', '')
#         line = line.strip()
#         FUNFAM_NUMBER,MEMBER_ID,SEQUENCE_MD5,MEMBER_TYPE = line.split(',')
#         if "CATH" in line:
#             print(line)
#             funfam_number = Counter(row[1] for row in csv.reader(f))
#             # print(funfam_number)
#             print(len(funfam_number))


#! /usr/bin/env python
#import pandas as pd
#df = pd.read_csv('funfam_members_in_sfam.csv')  ##opening a csv file with pd
#print(df)    ## parse the csv file
#print(df.shape)    ## dimention of the dataframe/csv file (rows:columns)
#df.info()    ## type of data in the file, object=string, int64, float64
#pd.set_option('display.max_rows', 188805)   ## print all rows/columns
#schema_df = pd.read_csv('funfam_members_in_sfam.csv')   ## meaning of each columns if defined
#print(df.head(10))   ###see a few first(head)/last(tail) raws, number inside()is to show how many rows
#print(df.columns)   ###to see the head title of columns
#print(df['FUNFAM_NUMBER'])   ###access only on column
#print(df['FUNFAM_NUMBER'].value_counts())    ###to see how many times each value is repeated
#print(df.loc[0])    ###specific row (0 = index that pandas gives to the datafeame)
#print(df.loc[0,'FUNFAM_NUMBER'])    ### specific row and specific column
#print(df.loc[[0,1,2],'FUNFAM_NUMBER'])   ### multiple specific row and specific column
#print(df.loc[0:2,'FUNFAM_NUMBER'])   ### multiple specific row and specific column using sclicing. NO SQR bracket
#print(df.loc[0:2,'FUNFAM_NUMBER':'MEMBER_TYPE'])   ### msclicing rows and columns (slicing in inclusive for the last value)

#df.set_index('SEQUENCE_MD5', inplace=True)
#print(df)   ###set the index based on a specific column
#print(df.index) ###print new indexex
#print(df.loc['3673695274e6db176cef64c64a05a616'])    ###to see all details of that specic index
#print(df.loc['3673695274e6db176cef64c64a05a616', 'MEMBER_TYPE'])  ###to see the details of that specic index
#print(df.iloc[0])   ###to see all details of the pandas index(0,2,6, etc)

#df.reset_index(inplace=True)    ###to reset the index to defult panda(inplace make it permanent)
#print(df)

#filt = (df['MEMBER_TYPE'] == 'CATH')
#print(len(df.loc[filt, 'FUNFAM_NUMBER']))
### filter and display only selected columns, filter in filter

#filt1 = df.sort_values(by=['MEMBER_TYPE', 'FUNFAM_NUMBER'], ascending=[True, False])
#print(filt1)
### sort different columns based on order

#print(df['FUNFAM_NUMBER'].nlargest(10))   ###10 largest values in that specefied column
#print(df['FUNFAM_NUMBER'].nsmallest(10))    ###10 smallest values in that specefied column
#print(df.nsmallest(10, 'FUNFAM_NUMBER'))    ### print the 10 smallest and display other info of that 10









###Unique Go terms and count how many###
# # !/usr/bin/env python
# import csv
# import pandas as pd
# f = pd.read_csv('go_terms_in_sfam.csv') 
# print(f['GO_ACC'].unique()) 
# print(len(f['GO_ACC'].unique()))

