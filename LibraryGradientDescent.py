# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:56:28 2017

@author: aakash.chotrani
"""
import numpy as np
import pandas as pd

DataCsv = pd.read_csv("StudentData.csv")
X =DataCsv.iloc[:,:-1].values
y = DataCsv.iloc[:,3].values
Theta = np.array([0.0,0.0,0.0])

from sklearn.linear_model import LinearRegression
ols = LinearRegression()
regressor = ols.fit(X,y)

print(regressor.coef_)
print(regressor.intercept_)
regressor.get_params()
y_predict = regressor.predict([Theta])