# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:13:11 2017

@author: aakash.chotrani
"""

import numpy as np
import pandas as pd


DataCsv = pd.read_csv("StudGradesInfo.csv")

Target_Course = "MAT150"



students = {}
courses = {}
for i in range(1,len(DataCsv)):
  row = DataCsv[i]
  ID = row[0]
  SectionCode = row[3]
  courses[SectionCode] = {}