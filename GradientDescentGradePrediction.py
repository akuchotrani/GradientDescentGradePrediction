# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:44:44 2017

@author: aakash.chotrani
"""
import numpy as np
import pandas as pd





def GradentDescent(X,y,Theta,alpha,m,numIterations):
    X_trans = X.transpose()
    print("X_transpose: ",X_trans)
    for i in range(0,numIterations):
        hypothesis = np.dot(X,Theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2)/(2*m)
        print("Iteration: ",i," | Cost: ", cost)
        print("Weights: ",Theta)
        gradient = np.dot(X_trans,loss)
        Theta = Theta - alpha*gradient
    return Theta
    


numIterations = 1000
alpha = 0.008
DataCsv = pd.read_csv("StudentData.csv")
X =DataCsv.iloc[:,:-1].values
y = DataCsv.iloc[:,3].values
Theta = np.array([0.1,0.5,0.8])
m = np.shape(X)
Theta = GradentDescent(X,y,Theta,alpha,m,numIterations)

student5 = [0.2,0.9,0.1]
predictedGrade = np.dot(Theta,student5)

print("PredictedGrade: ",predictedGrade)