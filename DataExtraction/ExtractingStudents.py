# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:13:11 2017

@author: aakash.chotrani
"""

import numpy as np
import pandas as pd


DataCsv = pd.read_csv("StudGradesInfo.csv")



def CSV_to_Array2D(filename):
  import csv
  csvfile = open(filename, 'r')
  reader = csv.reader(csvfile)
  result = []
  for row in reader:
    result.append(row)
  return result



#Return an object by parsing the course string and seperating it with keys: code , season, year
#Example:-
#course string = CS230S17-B
#code: CS230
#season: S
#year: 17
def courseString_to_Object(course):
  import re
  expression = r'(([A-Z]+)([0-9]+))([A-Z]+)([0-9]+)'
  match = re.match(expression, course)
  return { 'code': match.group(1), 'season': match.group(4), 'year': match.group(5) }



students = {}
def Create_Dictionary_of_Dictionary():
    #creating a dictionary of dictionary of all the 4102 students mapped by ID 
    StudGradesInfo = CSV_to_Array2D('StudGradesInfo.csv')
    print("Total Data Records Parsed: ",len(DataCsv))
    #creating a dictionary for 4102 students
    for i in range(1,len(DataCsv)):
        row = StudGradesInfo[i]
        ID = row[0]    
        students[ID] = {}
    
    #For each student mapping their ID to the course that they took.
    for i in range(1,len(DataCsv)):
        row = StudGradesInfo[i]
        ID = row[0]
        #Considering only the student who enrolled into the class. 
        #If status row[5] is 2 the student took it and did not drop the class
        #If Grade row[6] is zero. It indicates that student is enrolled and currently taking the class. The data is not avaialble. Hence we will skip it.
        if row[5] == '2' and row[6] != '0':
            SectionCode = courseString_to_Object(row[3])
            students[ID][SectionCode['code']] = row[7]
        

#Go through the whole students dictionary and check if the student has taken the target course
# If yes then record the grade and record the keys
def Check_Target_Course(target_course):

    ID_Prev_Students = []
    for keys in students:
        if target_course in students[keys]:
            ID_Prev_Students.append(keys)

    return ID_Prev_Students

def Create_Data_To_Train(Courses,StudentIDs):
    print("Creating Training Data....")
    
    #Creating lists of list of all the courses for recording the grade
    courseLists = [[] for i in Courses]
    #print("Course List: ",courseLists)
    
    #looping through all the students who previously took the course
    for ID in StudentIDs:
        if ID in students:
            #looping through and checking if the previous student also took similar courses as traget course.
            
            for index,course in enumerate(Courses):
                #if student also took the same course just record his grade for training
                if course in students[ID]:
                    courseLists[index].append(students[ID][course])
                #Student did not take this course then append -1
                else:
                    courseLists[index].append(-1)
    return courseLists


def main():
    print("Exectuing the code")
    Create_Dictionary_of_Dictionary()
    
    Target_Course = "CS529"
    Target_Student_Prev_Courses = ['CS525','CS541']
    
    ID_Prev_Students = Check_Target_Course(Target_Course)
    print("Students Who Previously Took The Target Course: ", len(ID_Prev_Students))
    
    Create_Data_To_Train(Target_Student_Prev_Courses, ID_Prev_Students)
    
if __name__ == "__main__":
    main()



