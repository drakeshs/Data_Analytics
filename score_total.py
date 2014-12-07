#! /usr/bin/env python

#v0.0.0
#********************************************************************************
#Adds the scores of the riskiest employees and saves it in a text file 
#********************************************************************************
#Importing modules

import csv
import os
import sys
import shutil

shutil.copy('Employee_Info_sub.csv', 'Database/Employee_Info_sub.csv')
os.chdir('Database')
if os.path.exists('score_total.txt'):
    os.remove('score_total.txt')
if os.path.exists('sum_file.txt'):
    os.remove('sum_file.txt')
if os.path.exists('score_total.txt'):
    os.remove('score_total.txt')
#with open ('score_acivity.txt' , 'rb') as fil:     #Opens the CSV file
 #   for col in (row.strip().split() for row in fil):


#with open ('score_info.txt', 'rb') as f:
 #   for cols in (row.strip().split() for row in f):
  #      score_info = int(cols[2])

# List of your files
file_names = ['score_info.csv', 'score_activity.csv']

# Output list of generator objects
o_data = []

# Open files in the succession and 
# store the file_name as the first
# element followed by the elements of
# the third column.
for afile in file_names:
    file_h = open(afile)
    a_list = []
    a_list.append(afile)
    csv_reader = csv.reader(file_h, delimiter=' ')
    for row in csv_reader:
        a_list.append(row[2])
    # Convert the list to a generator object
    o_data.append((n for n in a_list))
    file_h.close()

# Use zip and csv writer to iterate
# through the generator objects and 
# write out to the output file
with open('sum_file.txt', 'w') as op_file:
    csv_writer = csv.writer(op_file, delimiter=',')
    for row in list(zip(*o_data)):
        csv_writer.writerow(row)
op_file.close()


#***************************************************
#Summming the scores and generating the file with
#the total values
#**************************************************
with open('sum_file.txt', 'rb') as f:
    next(f)
    for cols in (row.strip().split(',') for row in f):
        total = int(cols[0]) + int(cols[1])
        orig_stdout = sys.stdout 
        out = file('score_total.txt', 'a')
        sys.stdout = out
        print total
        sys.stdout = orig_stdout
        out.close()

if os.path.exists('Employee_Info_sub.csv'):
        os.remove('Employee_Info_sub.csv')
if os.path.exists('sum_file.txt'):
    os.remove('sum_file.txt')
