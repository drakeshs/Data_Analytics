#! /usr/bin/env python

#---------------------------------------------------------------
#        Data Analytics for ECE3822:  Activity Score
# This will search through the three csv files(Access Logs,Phone
# Call Logs, and Air Travel) to calculate a score to express the
# activity of each employee.
#---------------------------------------------------------------

#------------------------------------------
#
# Initialize Libraries
#
#------------------------------------------

import os
import csv 
import sys
import string
import shutil

#------------------------------------------
# Remove the activity_score.txt file so new
# data is not appended further if the 
# script is rerun.
#------------------------------------------
os.chdir('Database')
if os.path.exists('score_activity.txt'):
    os.remove('score_activity.txt')
os.chdir('..')
#-----------------------------------------------------------------
# The process in this section consists of opening the Employee
# Info csv file to search through each employee directory by
# id number.  Then enter the directories Access Logs, Phone Call
# Logs and Air Travel to access the text file within.  Then it
# will count the number of lines in the text files and go through
# a scoring criteria which will then be stored in the text file
# activity_score.txt
#-----------------------------------------------------------------

shutil.copy('Employee_Info_sub.csv', 'Database/Employee_Info_sub.csv')
os.chdir('Database')
with open ('Employee_Info_sub.csv', 'rb') as csvfile:
    employee_info = csv.reader(csvfile, delimiter=',')
    num_access_lines = 0 #---------------------------
    phone_call_lines = 0 # Initialize counters
    air_travel_lines = 0 #---------------------------
    for col in employee_info:
        emp_id = col[0].strip()
        if os.path.exists(emp_id):
            os.chdir(emp_id)
            #--------------------------------------------------------
            # Change into necessary subdirectory and access text file
            # to count the number of lines, increment counter
            #--------------------------------------------------------
            os.chdir('Access_Log')         
            if os.path.exists('access_log.txt'):
                with  open('access_log.txt', 'rb') as f:
                    for line in f:
                        num_access_lines = num_access_lines + 1
            #----------------------------------------
            # Count is zero if there is no text file
            #----------------------------------------
            else:
                num_access_lines = 0
            os.chdir('..')
            os.chdir('Phone_Call_Logs')
            if os.path.exists('phone_call_logs.txt'):
                with open('phone_call_logs.txt', 'rb') as f:
                    for line in f:
                        phone_call_lines = phone_call_lines + 1
            else:
                phone_call_lines = 0
            os.chdir('..')
            os.chdir('Air_Travel')
            if os.path.exists('air_travel.txt'):
                with open('air_travel.txt', 'rb') as f:
                    for line in f:
                        air_travel_lines = air_travel_lines + 1
            else:
                air_travel_lines = 0
            os.chdir('..')
            os.chdir('..')
            orig_stdout = sys.stdout
            out = file('score_activity.txt', 'a')
            sys.stdout = out
            #-------------------------------------------------
            # Set scoring citeria - starting with access_logs
            #-------------------------------------------------
            if num_access_lines < 100:
                access_log_score = 1
            if (num_access_lines >= 100) and (num_access_lines < 200):
                access_log_score = 5
            if (num_access_lines >= 200) and (num_access_lines < 250):
                access_log_score = 8
            if (num_access_lines >= 250) and (num_access_lines < 300):
                access_log_score = 13
            if (num_access_lines >= 300) and (num_access_lines < 350):
                access_log_score = 17
            if (num_access_lines > 350) and (num_access_lines < 400):
                access_log_score = 23
            if (num_access_lines > 400):
                access_log_score = 33
            #---------------------------------------
            # Phone log criteria
            #---------------------------------------
            if phone_call_lines < 100:
                phone_log_score = 1
            if (phone_call_lines >= 100) and (phone_call_lines < 200):
                phone_log_score = 5
            if (phone_call_lines >= 200) and (phone_call_lines < 250):
                phone_log_score = 8
            if (phone_call_lines >= 250) and (phone_call_lines < 300):
                phone_log_score = 13
            if (phone_call_lines >= 300) and (phone_call_lines < 350):
                phone_log_score = 17
            if (phone_call_lines > 350) and (phone_call_lines < 400):
                phone_log_score = 23
            if (phone_call_lines > 400):
                phone_log_score = 33
            #--------------------------------------
            # Air travel criteria
            #--------------------------------------
            if air_travel_lines < 5:
                air_travel_score = 1
            if (air_travel_lines >= 5) and (air_travel_lines < 15):
                air_travel_score = 5
            if (air_travel_lines >= 15) and (air_travel_lines < 25):
                air_travel_score = 8
            if (air_travel_lines >= 25) and (air_travel_lines < 35):
                air_travel_score = 13
            if (air_travel_lines >= 35) and (air_travel_lines < 50):
                air_travel_score = 17
            if (air_travel_lines > 50) and (air_travel_lines < 65):
                air_travel_score = 23
            if (air_travel_lines > 65):
                air_travel_score = 33
            print emp_id,
            print ':',
            print (phone_log_score + access_log_score + air_travel_score)
            sys.stdout = orig_stdout
            out.close()
            num_access_lines = 0
            phone_call_lines = 0
            air_travel_lines = 0
           # os.chdir('Database')
if os.path.exists('Employee_Info_sub.csv'):
        os.remove('Employee_Info_sub.csv')                
#-------------------------------------------------------------------
# Based on the scoring criteria, anyone with an overall score of 69
# to 99 would be considered highly active, from 24 to 51 moderately
# active and anything less than 24 not very active.
#-------------------------------------------------------------------
