#! /usr/bin/env python 

#v2.0.0
#*************************************************************************************
# Scoring risk levels of the employee
#The code should be ran from the directory where the Database has been stored
#*************************************************************************************
#Importing modules

import csv
import os
import sys
import shutil
import datetime

#*************************************************************************************
#The dictionaries assign score values to different employee citizenship and information attributes

Citizenship_Dict = {'Citizen of Costa Rica' : 15, 'Citizen of Eritrea' : 10, 'Citizen of Nepal' : 20, 'Citizen of Peru' : 20, 'Citizen of Sweden' : 30, 'Citizen of United States' : 20 }

Marital_Dict = {'M' : 5, 'D' : 50, 'S' : 45}

Gender_Dict = {'F' : 45, 'M' : 55}

Age_Dict = {'20-30' : 15, '30-40': 25, '40-50' : 25, '50-60' : 20, '60-70' : 10, '70-80' : 5}


#*******************************************************************************
#Initializes the text files that will store each employee's score
#Prevents the appending of repeated information every time the code is implemented
shutil.copy('Employee_Info_sub.csv', 'Database/Employee_Info_sub.csv') #moves CSV info file to the 'Database' directory
os.chdir('Database')                                                   #CSV is used as a guide to iterate through all the employee IDs
with open ('Employee_Info_sub.csv', 'rb') as csvfile:     #Opens the CSV file
    employee_info = csv.reader(csvfile, delimiter=',') #Stores the fileds in a variable 'employee_info'
    next(employee_info, None)              #Skips the first line of the CSV (Headers)
    for col in employee_info:              #Iterates through the columns in the CSV file, reading info for the same employee
        emp_id = col[0].strip()            #stores the employee id in variable 'emp_id'. It is stripped to avoid undesired blank spaces
        os.chdir(emp_id)
        if os.path.exists('score.txt'):
            os.remove('score.txt')
        os.chdir('..')
os.chdir('..')                                     #Return to the main directory from which code was executed
 

#**************************************************************************************
#Score generation of the scores according to info and citizenship

shutil.copy('Citizenship_sub.csv', 'Database/Citizenship_sub.csv')

os.chdir('Database')
with open ('Citizenship_sub.csv', 'rb') as csvfile:
    citizenship = csv.reader(csvfile, delimiter=',')
    next(citizenship, None)
    for col in citizenship:
        employee = col[0].strip()
        citizen_status = col[1]
        os.chdir(employee)
        os.chdir('Citizenship')                                     #cd to the subdirectory Citizenship
        with open ('citizenship.txt', 'rb') as f:                   #reads txt file that contains all comma-separated citizenship information
            field = [x for x in f.read().split(",") if x != ""]     #parses the file using ',' as a delimiter 
            for i in range(0, 1):                                   #iterates through the 2 fields in text file
                field[i] = field[i].strip()                        
                for key in sorted(Citizenship_Dict):                #iterates through the dictionary values and finds if there is a match
                    if key == field[i]:
                        orig_stdout = sys.stdout                    #redirects output
                        out = file('../score.txt', 'a')    #defines file to print output
                        sys.stdout = out                            
                        score_citizenship = Citizenship_Dict[key]
                        print "citizenship",
                        print ":",
                        print score_citizenship                  #print the score according to the matching file in the dictionary and the field
                        sys.stdout = orig_stdout
                        out.close()
        
        
        if os.path.exists('score.txt'):
            os.chdir('..')
           # shutil.copy('./Citizenship/score.txt', './score.txt')
            os.chdir('..')
    
        else:
            os.chdir('..')
            os.chdir('..')
os.remove('Citizenship_sub.csv')
       
#**************************************************************************************
#shutil.copy('Employee_Info_sub.csv', 'Database/Employee_Info_sub.csv')

with open ('Employee_Info_sub.csv', 'rb') as csvfile:
    info = csv.reader(csvfile, delimiter=',')
    next(info, None)
    for col in info:
        employee = col[0].strip()
        os.chdir(employee)
        os.chdir('Employee_Info')
        with open ('employee_info.txt', 'rb') as f:
            field = [x for x in f.read().split(",") if x != ""]
            for i in range(0,11):
                field[i] = field[i].strip()

            date_birth = field[2].split("-")
            from datetime import date
            year_current = int(date.today().year)
            age = year_current - (int(date_birth[2])+int(1900))
            orig_stdout = sys.stdout
            out = file('../score.txt', 'a')
            sys.stdout = out
            if age < 30:
                score_age = 15
            elif age >= 30 and age < 40:
                score_age = 25
            elif age >= 40 and age < 50:
                score_age = 25
            elif age >= 50 and age < 60:
                score_age = 20
            elif age >= 60 and age < 70:
                score_age = 10
            elif age >= 70:
                score_age = 5
                
            print "age",
            print ":",
            print score_age 
            sys.stdout = orig_stdout
            out.close()
            
            date_employ = field[3].split("-")
            date_employ = int(date_employ[2])
            if date_employ <= (year_current - 2000):
                employment = year_current - (date_employ + int(2000))
            else:    
                employment = year_current - (date_employ + int(1900))
            
            orig_stdout = sys.stdout
            out = file('../score.txt','a')
            sys.stdout = out
            
            if employment < 5:
                score_employment = 30
            elif employment >= 5 and employment < 10:
                score_employment = 20
            elif employment >= 10 and employment < 20:
                score_employment = 15
            elif employment >= 20 and employment < 30:
                score_employment = 10
            elif employment >= 40 and employment < 50:
                score_employment = 5
            elif employment > 50:
                score_employment = 5

            print "date_employment",
            print ":",
            print score_employment  
            sys.stdout = orig_stdout
            out.close()

            for key in sorted(Marital_Dict):
                if key == field[10]:
                        orig_stdout = sys.stdout
                        out = file('../score.txt', 'a')
                        sys.stdout = out
                        score_marital = Marital_Dict[key]
                        print "marital_status",
                        print ":",
                        print score_marital 
                        sys.stdout = orig_stdout
                        out.close()

            for key in sorted(Gender_Dict):
                if key == field[9]:
                        orig_stdout = sys.stdout
                        out = file('../score.txt', 'a')
                        sys.stdout = out
                        score_gender = Gender_Dict[key]
                        print "gender",
                        print ":",
                        print score_gender 
                        sys.stdout = orig_stdout
                        out.close()


        if os.path.exists('score.txt'):
            os.chdir('..')
           # shutil.copy('./Employee_Info/score.txt', './score.txt')
            os.chdir('..')
    
        else:
            os.chdir('..')
            os.chdir('..') # Return to source directory

#**********************************************************************************************
#Calculating total score
if os.path.exists('score_info.csv'):
    os.remove('score_info.csv')
with open ('Employee_Info_sub.csv', 'rb') as csvfile:
    info = csv.reader(csvfile, delimiter=',')
    next(info, None)
    for col in info:
        employee = col[0].strip()
        os.chdir(employee)
        total_score = 0
        with open ('score.txt', 'rb') as f:
           for cols in (row.strip().split() for row in f):
              # print cols[2]
               total_score = (int(cols[2]) + total_score)/5
           
           orig_stdout = sys.stdout
           out = file('../score_info.csv', 'a')
           sys.stdout = out
           print employee,
           print ",",
           print total_score
           sys.stdout = orig_stdout
           out.close()

        os.chdir('..')
    
if os.path.exists('Employee_Info_sub.csv'):
        os.remove('Employee_Info_sub.csv')
