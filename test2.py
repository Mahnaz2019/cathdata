#!/usr/bin/env python

# test2 python script
import pandas as pd

csv2_filename = "/Users/hosseinamiri/git/cathdata/funfam_members_in_sfam.csv"

uniq_member_id = set()

with open (csv2_filename) as csv2_fh:
    for line in csv2_fh:
        line = line.replace('"','')
        line = line.strip()
        funfam_number, member_id, sequence_md5, member_type = line.split(',')
        uniq_member_id.add(member_id)
for member_id in sorted(uniq_member_id):
    print(f"member_id: {member_id}")



