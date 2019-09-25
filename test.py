#!/usr/bin/env python

# test python script
import pandas as pd

csv1_filename = "/Users/hosseinamiri/git/cathdata/ec_terms_in_sfam.csv"

uniq_ec = set()

with open(csv1_filename) as csv1_fh:
    for line in csv1_fh:
        line = line.replace('"', '')
        line = line.strip()
        uniprot_acc, ec_code = line.split(',')
        uniq_ec.add(ec_code)

for ec_code in sorted(uniq_ec):
    print(f"ec_code: {ec_code}")

# cereal_df = pd.read_csv (csv1_filename)
# cereal_df2 = pd.read_csv ("ec_terms_in_sfam.csv")

# print (cereal_df.head(10))

# for index, row in cereal_df.head(5).iterrows():
#     print("row:{}  row[1]={}  row['EC_CODE']=".format(index, row[1]))




# a = "3.1.1."
# while a = "3.1.1.":
# print (a)
# a = a + a + *
# a = a + a + **
# Print ("done")

