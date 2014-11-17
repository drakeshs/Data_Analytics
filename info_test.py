#! /usr/bin/env python 

#version 0.2.
#******************************************************************************
# Scoring risk levels of the employee
#The code should be ran from the directory where the Database has been stored
#*******************************************************************************

import csv
import os
import sys
import shutil
import datetime

# Access_Log[NTID HOST_IP HOST_NAME DATE_AND_TIME]

# Air_Travel[TRIP_ID NAME EMPLOYEE_ID AIRLINES FLIGHT_NUMBER DEPARTURE_DATE DEPARTURE_TIME DEPARTURE_CITY ARRIVAL_DATE ARRIVAL_TIME ARRIVAL_CITY]

# Citizenship[Employee_ID Citizenship_Status Citizen_Country]

# Employee_Contact[Employee_ID Region Business_E-Mail Personal_E-Mail Bussiness Cell Bussiness_Phone Bussiness_Cell Bussiness_Phone Personal_Cell Fax ]

# EMployee_Info[Employee_ID Region Birth_Country Birth_Date Start_Date First_Name MI Last_Name First_Name Citizenship Gender Marital_Status]

# Job_HX[Employee_ID Region Action Reason Start_Date Area_Code City Location_Area_Code Department Status Job_Code Effective Area_Code City Address City State Zip Country NTID Domain]

# Phone_Call_Log[FAN Acct.Num Src_Num Caller_Name Date Time Source Destination Destination_Number In/Out Duration]

#************************************************************************************************************************************************
#Citizenship Score

Citizenship_Dict = {'Citizen of Costa Rica' : 15, 'Citizen of Eritrea' : 10, 'Citizen of Nepal' : 20, 'Citizen of Peru' : 20, 'Citizen of Sweden' : 30, 'Citizen of United States' : 20 }

Marital_Dict = {'M' : 5, 'D' : 50, 'S' : 45}

Gender_Dict = {'F' : 45, 'M' : 55}

Age_Dict = {'20-30' : 15, '30-40': 25, '40-50' : 25, '50-60' : 20, '60-70' : 10, '70-80' : 5}



#Creating the txt files.
shutil.copy('Employee_Info_sub.csv', 'Database/Employee_Info_sub.csv')
os.chdir('Database')
with open ('Employee_Info_sub.csv', 'rb') as csvfile:
    employee_info = csv.reader(csvfile, delimiter=',')
    next(employee_info, None)##
    for col in employee_info:                               
        emp_id = col[0].strip()
        os.chdir(emp_id)
        os.chdir('Employee_Info')
        if os.path.exists('score_info.txt'):
            os.remove('score_info.txt')
        os.chdir('..')
        os.chdir('Job_Hx')
        if os.path.exists('score.txt'):
                os.remove('score.txt')
        os.chdir('..')
        os.chdir('Access_Log')
        if os.path.exists('score.txt'):
                os.remove('score.txt')
        os.chdir('..')
        os.chdir('Air_Travel')
        if os.path.exists('score.txt'):
                os.remove('score.txt')
        os.chdir('..')
        os.chdir('Employee_Contact')
        if os.path.exists('score.txt'):
                os.remove('score.txt')
        os.chdir('..')
        os.chdir('Phone_Call_Logs')
        if os.path.exists('score.txt'):
                os.remove('score.txt')
        os.chdir('..')
        os.chdir('Citizenship')
        if os.path.exists('score_citizenship.txt'):
                os.remove('score_citizenship.txt')
        os.chdir('..')
        os.chdir('..')
os.chdir('..')
 

#***********************************************************************************************************************************************

shutil.copy('Citizenship_sub.csv', 'Database/Citizenship_sub.csv')

os.chdir('Database')
with open ('Citizenship_sub.csv', 'rb') as csvfile:
    citizenship = csv.reader(csvfile, delimiter=',')
    next(citizenship, None)##
    for col in citizenship:
        employee = col[0].strip()
        citizen_status = col[1]
        os.chdir(employee)
        os.chdir('Citizenship')
        with open ('citizenship.txt', 'rb') as f:
            field = [x for x in f.read().split(",") if x != ""]
            for i in range(0, 1):
                field[i] = field[i].strip()
                for key in sorted(Citizenship_Dict):
                    if key == field[i]:
                        orig_stdout = sys.stdout
                        out = file('score_citizenship.txt', 'a')
                        sys.stdout = out
                        print "citizenship",
                        print ":",
                        print Citizenship_Dict[key]
                        sys.stdout = orig_stdout
                        out.close()
        
        
        if os.path.exists('score_citizenship.txt'):
            os.chdir('..')
            shutil.copy('./Citizenship/score_citizenship.txt', './score_citizenship.txt')
            os.chdir('..')
    
        else:
            os.chdir('..')
            os.chdir('..')
os.remove('Citizenship_sub.csv')
       
#*******************************************************************************************************************************
#shutil.copy('Employee_Info_sub.csv', 'Database/Employee_Info_sub.csv')

with open ('Employee_Info_sub.csv', 'rb') as csvfile:
    info = csv.reader(csvfile, delimiter=',')
    next(info, None)##
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
            out = file('score_info.txt', 'a')
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
            out = file('score_info.txt','a')
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

            print "date employment",
            print ":",
            print score_employment 
            sys.stdout = orig_stdout
            out.close()

            for key in sorted(Marital_Dict):
                if key == field[10]:
                        orig_stdout = sys.stdout
                        out = file('score_info.txt', 'a')
                        sys.stdout = out
                        print "marital status",
                        print ":",
                        print Marital_Dict[key]
                        sys.stdout = orig_stdout
                        out.close()

            for key in sorted(Gender_Dict):
                if key == field[9]:
                        orig_stdout = sys.stdout
                        out = file('score_info.txt', 'a')
                        sys.stdout = out
                        print "gender",
                        print ":",
                        print Gender_Dict[key]
                        sys.stdout = orig_stdout
                        out.close()


        if os.path.exists('score_info.txt'):
            os.chdir('..')
            shutil.copy('./Employee_Info/score_info.txt', './score_info.txt')
            os.chdir('..')
    
        else:
            os.chdir('..')
            os.chdir('..')

